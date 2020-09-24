from flask import request, url_for, render_template, redirect, Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from config import Config
from database import GetICsAndWeight, GetBetasMktAndSpecVols
import json

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
import models




####Models####
@app.route('/')
def home():
    return "home page"


@app.route("/getdata/<rdate>/<mktIndexCode>")
def betas_table(rdate, mktIndexCode):
    #Get alpha column from database
    IC_data = db.session.query(models.getweights.alpha).all()
    #create empty list to add Instruments from database in list form
    ICs = []
    for i in IC_data:
        ICs.append(i[0])
    ##use output for function 2 paramaters
    mktVol, df = GetBetasMktAndSpecVols(rDate=rdate, ICs=ICs, mktIndexCode=mktIndexCode)
    #convert data frame to dictionary
    new_data = df.to_dict('records')

    #add to model and move to database
    for i in range(len(new_data)):
        my_new_result = models.Result(instrument=new_data[i]["Instrument"], beta=new_data[i]['Beta'],
                                      unique_risk=new_data[i]['Unique Risk'],
                                      total_risk=new_data[i]['Total Risk'])
        db.session.add(my_new_result)
        db.session.commit()

    #create list of data
    results = models.Result.query.all()
    #serialize data
    output = models.result_schema.dump(results)



    return jsonify(output)



@app.route("/getweights", methods=['GET', "POST"])
def weights_table():

    if request.method == 'POST':
        #take inputs from front end form
        rdate = request.form['rdate']
        indexCode = request.form['indexcode']
        mktIndexCode = request.form['mktIndexCode']
        #add as parameters to getICS
        portframe = GetICsAndWeight(rDate=rdate, indexCode=indexCode)
        #convert dataframe to dictonary
        new_frame = portframe.to_dict('records')
        #loop through index and add to data frame
        for i in range(len(new_frame)):
            new_weights = models.getweights(alpha=new_frame[i]["Alpha"], weights=new_frame[i]['weights'])
            db.session.add(new_weights)
            db.session.commit()
        #Once post is completed, redirect to betas output
        return redirect(url_for('betas_table', rdate=rdate, mktIndexCode=mktIndexCode))
    else:

        return render_template('index.html')


# api.add_resource(PuppyResource, '/puppy/<string:name>')
# api.add_resource(AllPuppies, '/puppies')
if __name__ == '__main__':
    app.run(debug=True)
