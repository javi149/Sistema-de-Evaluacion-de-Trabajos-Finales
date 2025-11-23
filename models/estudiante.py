from database import db

class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    apellido = db.Column(db.String(120))
    rut = db.Column(db.String(20))
    email = db.Column(db.String(120))
    carrera = db.Column(db.String(120))
