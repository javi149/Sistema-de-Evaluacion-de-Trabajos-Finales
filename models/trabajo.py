from database import db

class Trabajo(db.Model):
    __tablename__ = 'trabajos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    tipo = db.Column(db.String(100)) # Tesis, Proyecto, etc.
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
