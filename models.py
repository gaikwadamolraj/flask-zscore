import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()   
class Score(db.Model):
    __tablename__ = 'zscore'
    id = db.Column(db.Integer, primary_key=True)
    isoCode = db.Column(db.String(100))
    companyId = db.Column(db.Integer)
    score = db.Column(db.JSON())