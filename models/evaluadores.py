from database import db

class Evaluadores(db.Model):
    __tablename__ = 'evaluadores'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), notnull=True)
    email = db.Column(db.String(120))
    rol = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
