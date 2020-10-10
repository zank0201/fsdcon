from flask import request, url_for, render_template, redirect, Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from config import BaseConfig
from database import GetICsAndWeight, GetBetasMktAndSpecVols, CalcStats
import json
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np

app = Flask(__name__)
app.config.from_object('config.BaseConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
cors = CORS(app, resources={r'/getweights/*': {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
import models


####Models####
@app.route('/')
def home():
    return "home page"


@app.route("/getweights", methods=["POST"])
@cross_origin()  # allow all origins all methods.
def weights_table():
    # delete tables as something is posted
    db.session.query(models.Result).delete()
    db.session.query(models.getweights).delete()
    db.session.query(models.marketvol).delete()
    db.session.commit()

    # take inputs from front end form
    data = request.get_json()
    rdate = data['rdate']
    indexCode = data['indexCode']
    mktIndexCode = data['mktIndex']
    # add as parameters to getICS
    # call function one
    portframe = GetICsAndWeight(rDate=rdate, indexCode=indexCode)

    # convert dataframe to dictonary
    new_frame = portframe.to_dict('records')
    # loop through index and add to data frame
    for i in range(len(new_frame)):
        new_weights = models.getweights(alpha=new_frame[i]["Alpha"], weights=new_frame[i]['weights'])
        db.session.add(new_weights)
        db.session.commit()
    # Once post is completed, redirect to betas output
    return redirect(url_for('betas_table', rdate=rdate, mktIndexCode=mktIndexCode))


@app.route('/getweights/<rdate>/<mktIndexCode>', methods=["GET"])
def betas_table(rdate, mktIndexCode):
    IC_data = db.session.query(models.getweights.alpha)
    # create empty list to add Instruments from database in list form
    ICs = []
    for i in IC_data:
        ICs.append(i[0])

    # use output for function 2 paramaters
    mktVol, df = GetBetasMktAndSpecVols(rDate=rdate, ICs=ICs, mktIndexCode=mktIndexCode)
    # convert data frame to dictionary
    new_data = df.to_dict('records')
    mktvol_data = mktVol.to_dict()

    # add to model and move to database
    for i in range(len(new_data)):
        my_new_result = models.Result(instrument=new_data[i]["Instrument"], beta=round(new_data[i]['Beta'], 3),
                                      unique_risk=round(new_data[i]['Unique Risk'], 3),
                                      total_risk=round(new_data[i]['Total Risk'], 3))
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
    weights_data = db.session.query(models.getweights.weights)
    betas_data = db.session.query(models.Result.beta)
    mktvol_data = db.session.query(models.marketvol.mktvol)
    specvol_data = db.session.query(models.Result.unique_risk)
    totalrisk_data = db.session.query(models.Result.total_risk)

    # create empty list for variables
    weights = []
    betas = []
    mktvol = []
    specvol = []
    totalrisk = []

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
    print(mktvol)

    # call function 3
    pfBetas, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, CorrMat = CalcStats(weights=weights, betas=
    betas, mktVol=mktvol,
                                                                                      specVols=specvol,
                                                                                      totalRisk=totalrisk)

    return jsonify([{'pfBetas': round(pfBetas, 4), 'pfSysVol': round(pfSysVol,4), 'pfSpecVol': round(pfSpecVol,4), 'pfVol': round(pfVol,4)}])


if __name__ == '__main__':
    app.run(debug=True)
