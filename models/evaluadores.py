from database import db

class Evaluadores(db.model):
    __tablename__ = 'evaluadores'
    id = db.Column(db.Ineteger), primary_key=True)
    nombre = db.Column(db.String(150), notnull=True)
    email = db.Column(db.String(120))
    rol = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
