
from flask import request, url_for ,render_template, redirect, Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config
from database import GetICsAndWeight, GetBetasMktAndSpecVols

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
        IC_data = db.session.query(models.getweights.alpha).all()
        ICs = []
        for i in IC_data:
            ICs.append(i[0])
        print(ICs)
        mktVol, df = GetBetasMktAndSpecVols(rDate=rdate, ICs=ICs, mktIndexCode=mktIndexCode)
        new_data = df.to_dict('records')
        for i in range(len(new_data)):
            my_new_result = models.Result(instrument=new_data[i]["Instrument"], beta=new_data[i]['Beta'],
                                          unique_risk=new_data[i]['Unique Risk'],
                                          total_risk=new_data[i]['Total Risk'])
            db.session.add(my_new_result)
            db.session.commit()
        return f'<h1>{rdate}</h1>'

@app.route("/getweights", methods=['GET', "POST"])
def weights_table():
    # row whole row
    # index

    if request.method == 'POST':
        rdate = request.form['rdate']
        indexCode = request.form['indexcode']
        mktIndexCode = request.form['mktIndexCode']
        portframe = GetICsAndWeight(rDate=rdate, indexCode=indexCode)
        new_frame = portframe.to_dict('records')
        for i in range(len(new_frame)):
            new_weights = models.getweights(alpha=new_frame[i]["Alpha"], weights=new_frame[i]['weights'])
            db.session.add(new_weights)
            db.session.commit()
        return redirect(url_for('betas_table', rdate = rdate, mktIndexCode=mktIndexCode))
    else:

        return render_template('index.html')






# api.add_resource(PuppyResource, '/puppy/<string:name>')
# api.add_resource(AllPuppies, '/puppies')
if __name__ == '__main__':
    app.run(debug=True)
