from flask import request, url_for, render_template, redirect, Flask, jsonify, send_file, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from config import BaseConfig
from database import *
# GetICsAndWeight, GetBetasMktAndSpecVols, CalcStats
import json
from flask_cors import CORS, cross_origin
import pandas as pd
import os
import zipfile
import numpy as np

from sqlalchemy.orm import load_only

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# abosolute path of directory containing csv files for download
if not os.path.exists('files'):
    os.makedirs('files')

folder = os.path.join(os.path.dirname(app.instance_path), 'files')

cors = CORS(app, resources={r'/getweights/*': {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
import models


@app.route("/getweights", methods=["POST", "GET"])
@cross_origin()  # allow all origins all methods.
def weights_table():
    '''
    Function takes in dates and index codes from frontend
    and pushes weights and alpha values to the the database
    :return: redirects to betas_table function
    '''
    # delete tables as something is posted
    db.session.query(models.Result).delete()
    db.session.query(models.getweights).delete()
    db.session.query(models.marketvol).delete()
    db.session.commit()

    # date input form frontend
    data = request.get_json()
    rdate = data['rdate']

    # index code input from frontend
    indexCode = data['indexCode']

    # call function to get weights, alphas and market index code
    portframe, mktIndexCode = GetICsAndWeight(rDate=rdate, indexCode=indexCode)

    # convert dataframe to dictonary
    new_frame = portframe.to_dict('records')
    # loop through index and add to data frame
    for i in range(len(new_frame)):
        new_weights = models.getweights(alpha=new_frame[i]["Instrument"], weights=new_frame[i]['weights'])
        db.session.add(new_weights)
        db.session.commit()
    # Once post is completed, redirect to betas output
    return redirect(url_for('betas_table', rdate=rdate, mktIndexCode=mktIndexCode, indexCode=indexCode))


@app.route('/getweights/<rdate>/<mktIndexCode>/<indexCode>', methods=["GET"])
def betas_table(rdate, mktIndexCode, indexCode):
    IC_data = db.session.query(models.getweights.alpha)
    weight_data = db.session.query(models.getweights.weights)
    # create empty list to add Instruments from database in list form
    ICs = []
    weights = []
    for i in IC_data:
        ICs.append(i[0])
    for i in weight_data:
        weights.append(i[0])
    dict_list = {'Instrument': ICs, 'weights': weights}

    portframe = pd.DataFrame(dict_list)

    print(portframe)
    # use output for function 2 paramaters
    mktVol, df = GetBetasMktAndSpecVols(rDate=rdate, ICs=ICs, mktIndexCode=mktIndexCode, portframe=portframe)
    # convert data frame to dictionary
    new_data = df.to_dict('records')
    mktvol_data = mktVol.to_dict()

    # add to model and move to database
    for i in range(len(new_data)):
        my_new_result = models.Result(instrument=new_data[i]["Instrument"], beta=round(new_data[i]['Beta'], 3),
                                      unique_risk=round(new_data[i]['Unique Risk'], 3),
                                      total_risk=round(new_data[i]['Total Risk'], 3), weights=new_data[i]['weights'])
        db.session.add(my_new_result)
        db.session.commit()

    new_result = models.marketvol(mktvol=round(mktvol_data["Total Risk"], 3))
    db.session.add(new_result)
    db.session.commit()

    # create list of data
    results = models.Result.query.all()

    # serialize data
    output = models.result_schema.dump(results)

    return jsonify(output)


@app.route('/getweights/stats')
@cross_origin()
def calcstats():
    # access tables to get variables of function 3
    weights_data = db.session.query(models.Result.weights)
    betas_data = db.session.query(models.Result.beta)
    mktvol_data = db.session.query(models.marketvol.mktvol)
    specvol_data = db.session.query(models.Result.unique_risk)
    totalrisk_data = db.session.query(models.Result.total_risk)
    ics_data = db.session.query(models.Result.instrument)

    # create empty list for variables
    weights = []
    betas = []
    mktvol = []
    specvol = []
    totalrisk = []
    ics = []

    for i in weights_data:
        weights.append(i[0])
    for i in betas_data:
        betas.append(i[0])
    for i in mktvol_data:
        mktvol.append(i[0])
    for i in specvol_data:
        specvol.append(i[0])
    for i in totalrisk_data:
        totalrisk.append(i[0])
    for i in ics_data:
        ics.append(i[0])
    # call function 3
    pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat = CalcStats(weights=weights, betas=
    betas, mktVol=mktvol,
                                                                                      specVols=specvol,
                                                                                      totalRisk=totalrisk)

    # Download matrices to excel
    sysCov = pd.DataFrame(data=sysCov, index=ics, columns=ics)

    sysCov.to_csv(folder + '/' + 'Systematic Covariance.csv', float_format='%.3f')

    specCov = pd.DataFrame(data=specCov, index=ics, columns=ics)
    specCov.to_csv(folder + '/' + 'Specific Covariance.csv', float_format='%.3f')

    totCov = pd.DataFrame(data=totCov, index=ics, columns=ics)
    totCov.to_csv(folder + '/' + 'Total Covariance.csv', float_format='%.3f')

    CorrMat = pd.DataFrame(data=CorrMat, index=ics, columns=ics)
    CorrMat.to_csv(folder + '/' + 'Correlation.csv', float_format='%.3f')
    return jsonify([{'pfBetas': round(pfBetas, 4), 'pfSysVol': round(pfSysVol, 4), 'pfSpecVol': round(pfSpecVol, 4),
                     'pfVol': round(pfVol, 4)}])


@app.route("/getweights/getfiles", methods=["GET"])
def list_files():
    """Endpoint to list files on the server."""
    # Zip file Initialization
    zipfolder = zipfile.ZipFile('Matrices.zip', 'w', compression=zipfile.ZIP_STORED)  # Compression type

    # zip all the files which are inside in the folder
    for root, dirs, files in os.walk('files/'):
        for file in files:
            print(file)
            zipfolder.write('files/' + file)
    zipfolder.close()

    return send_file('Matrices.zip',
                     mimetype='zip',
                     attachment_filename='Matrices.zip',
                     as_attachment=True)


@app.route("/getweights/getfiles/<path:path>", methods=["GET"])
def get_file(path):
    """Download a file."""
    return send_from_directory(folder, path, as_attachment=True)


# Get weights
@app.route('/getweights/betas', methods=["GET"])
@cross_origin()
def weights():
    betas_data = db.session.query(models.Result.beta)
    # create empty list for variables
    betas = []

    for i in betas_data:
        betas.append(i[0])

    return jsonify(betas)


@app.route('/getweights/alpha', methods=["GET"])
@cross_origin()
def alpha():
    alpha_data = db.session.query(models.getweights.alpha)

    alpha = []
    for i in alpha_data:
        alpha.append(i[0])
    return jsonify(alpha)


@app.route("/getweights/piechart", methods=["GET"])
@cross_origin()
def piechart():
    alpha_data = db.session.query(models.getweights.alpha)

    alpha = []

    weights_data = db.session.query(models.getweights.weights)
    # create empty list for variables
    weights = []

    for i in weights_data:
        weights.append(i[0])
    for i in alpha_data:
        alpha.append(i[0])

    dict_list = {'name': alpha, 'value': weights}

    newdate = pd.DataFrame(dict_list)

    result = newdate.to_json(orient='records')
    parsedresult = json.loads(result)
    output = json.dumps(parsedresult, indent=4)

    return output


@app.route("/getweights/ics", methods=["POST"])
@cross_origin()
def timeseriesICs():
    data = request.get_json()

    mktIndexCode = data['mktIndex']
    ics = PortFolioIcs(mktIndexCode=mktIndexCode)

    output = json.dumps(ics)
    print(type(output))
    return output


@app.route("/getweights/ics/<mktIndex>", methods=["POST"])
@cross_origin()
def portfoliobetas(mktIndex):
    db.session.query(models.getweights).delete()
    db.session.query(models.BetasTime).delete()
    db.session.query(models.RiskTime).delete()
    db.session.query(models.marketvol).delete()

    db.session.commit()
    data = request.get_json()
    ics = data['selected']
    weights = data['weightslist']
    mktIndex = mktIndex

    for i in range(len(ics)):
        new_model = models.getweights(alpha=ics[i], weights=weights[i])
        db.session.add(new_model)
        db.session.commit()

    # dates, pfSysVols, pfSpecVols, pfVols = PortfolioRisk(ICs=ics, weights=weights, mktIndexCode=mktIndex)
    newframe, mktframe = PortfolioBetasMktAndSpecVols(ICs=ics, weights=weights, mktIndexCode=mktIndex)
    # betas_frame = PortfolioBetasMktAndSpecVol(ICs=ics, weights=weights, mktIndexCode=mktIndex)
    model_dict = newframe.to_dict('records')
    mktvol_dict = mktframe.to_dict('records')
    beta_data = []

    for i in range(len(model_dict)):
        new_model = models.BetasTime(dates=model_dict[i]['Dates'], beta=model_dict[i]['pfBeta'])
        beta_data.append(round(model_dict[i]['pfBeta'], 3))
        db.session.add(new_model)
        db.session.commit()
        # Once post is completed, redirect to betas output


    for i in range(len(mktvol_dict)):

        mkt_model = models.marketvol(mktvol=round(mktvol_dict[i]['Total Risk'], 3))
        db.session.add(mkt_model)
        db.session.commit()
    #
    output = json.dumps(beta_data)
    return output

@app.route("/getweights/ics/dates", methods=["GET"])
@cross_origin()
def portfoliobetadates():
    dates_data = db.session.query(models.BetasTime.dates)

    dates = []
    for i in dates_data:
        dates.append(i[0])
    return jsonify(dates)


@app.route("/getweights/ics/risk/<mktIndex>", methods=["POST"])
@cross_origin()
def portfolioRisk(mktIndex):
    db.session.query(models.RiskTime).delete()

    mktVol_data = db.session.query(models.marketvol.mktvol)
    ics_data = db.session.query(models.getweights.alpha)
    weights_data = db.session.query(models.getweights.weights)

    mktVol = []
    ics = []
    weights = []
    for i in mktVol_data:
        mktVol.append(i[0])
    for i in ics_data:
        ics.append(i[0])
    for i in weights_data:
        weights.append(i[0])

    dates, pfSysVols, pfSpecVols, pfVols = PortfolioRisk(ICs=ics, weights=weights,mktIndexCode=mktIndex, mkt_val=mktVol)


    for i in range(len(dates)):
        new_model = models.RiskTime(dates=dates[i], pfSysVols=pfSysVols[i],
                                    pfSpecVols=pfSpecVols[i], pfVols=pfVols[i])
        db.session.add(new_model)
        db.session.commit()

    results = dates.tolist()
    output = json.dumps(results)
    return output


@app.route("/getweights/ics/risk/sysvols", methods=["GET"])
@cross_origin()
def riskSysVol():
    sysvols_data = db.session.query(models.RiskTime.pfSysVols)

    sysvols = []


    for i in sysvols_data:
        sysvols.append(i[0])

    output = json.dumps(sysvols)
    return output

@app.route("/getweights/ics/risk/pfvols", methods=["GET"])
@cross_origin()
def riskpfVols():
    pfvols_data = db.session.query(models.RiskTime.pfVols)

    pfvols = []


    for i in pfvols_data:
        pfvols.append(i[0])

    output = json.dumps(pfvols)
    return output

@app.route("/getweights/ics/risk/pfspec", methods=["GET"])
@cross_origin()
def riskpfSpec():
    pfspec_data = db.session.query(models.RiskTime.pfSpecVols)

    pfspecs = []


    for i in pfspec_data:
        pfspecs.append(i[0])

    output = json.dumps(pfspecs)
    return output


@app.route("/getweights/portfolio", methods=["POST"])
@cross_origin()
def icsTime():

    db.session.query(models.getweights).delete()
    db.session.query(models.BetasTime).delete()
    db.session.query(models.RiskTime).delete()
    db.session.query(models.marketvol).delete()
    data = request.get_json()

    IndexCode = data['indexCode']
    icsFrame, mktIndexCode = GetICSTime(indexCode=IndexCode)
    new_frame, mkt_val = GetBetasTime(mktIndexCode=mktIndexCode, icsFrame=icsFrame)
    # mktvol_dict = mkt_val.to_dict('records')
    # new_data = new_frame.to_dict('records')

    # Get portfolio betas and dates and push to db
    betasframe = PortfolioBetasTime(new_frame=new_frame)
    new_data = betasframe.to_dict('records')
    beta_data = []

    for i in range(len(new_data)):

        new_model = models.BetasTime(dates=new_data[i]['Dates'], beta=round(new_data[i]['pfBeta'],4))
        beta_data.append(round(new_data[i]['pfBeta'], 4))
        db.session.add(new_model)
        db.session.commit()

    # Push  market volatility
    for i in range(len(mkt_val)):

        mkt_model = models.marketvol(mktvol=round(mkt_val[i], 3))
        db.session.add(mkt_model)
        db.session.commit()

    # Get portfolio risk values and push to db
    dates, pfSysVols, pfSpecVols, pfVols = RiskTime(new_frame=new_frame, mkt_val = mkt_val)

    for i in range(len(pfVols)):
        new_model = models.RiskTime(dates=dates[i], pfSysVols=round(pfSysVols[i],4),
                                    pfSpecVols=round(pfSpecVols[i],4), pfVols=round(pfVols[i],4))
        db.session.add(new_model)
        db.session.commit()

    output = json.dumps(beta_data)
    return output








if __name__ == '__main__':
    app.run(debug=True)
