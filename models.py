from app import db, ma


####Models####
class getweights(db.Model):
    __tablename__ = 'getweights'

    id = db.Column(db.Integer, primary_key=True)
    alpha = db.Column(db.String())
    weights = db.Column(db.Float())

    def __init__(self, alpha: object, weights: object) -> object:
        self.alpha = alpha
        self.weights = weights

    def __repr__(self):
        return 'alpha: {}'.format(self.alpha), 'weights: {}'.format(self.weights)


class getweightsSchema(ma.ModelSchema):
    class Meta:
        model = getweights


class Result(db.Model):
    __tablename__ = 'betas'

    id = db.Column(db.Integer, primary_key=True)
    instrument = db.Column(db.String())
    beta = db.Column(db.Float())
    unique_risk = db.Column(db.Float())
    total_risk = db.Column(db.Float())

    def __init__(self, instrument: object, beta: object, unique_risk: object, total_risk: object) -> object:
        self.instrument = instrument
        self.beta = beta
        self.unique_risk = unique_risk
        self.total_risk = total_risk

    # def json(self):
    #     return {'instrument': self.instrument, 'beta': self.beta, 'unique risk': self.unique_risk,
    #             'total risk': self.total_risk}

    def __repr__(self):
        return 'instrument: {}'.format(self.instrument), 'beta: {}'.format(self.beta), \
               'unique risk:{}'.format(self.unique_risk), 'total risk: {}'.format(self.total_risk)


class ResultSchema(ma.ModelSchema):
    class Meta:
        model = Result
