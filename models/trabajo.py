from database import db

class Trabajo(db.Model):
    __tablename__ = 'trabajos'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    tipo = db.Column(db.String(100)) # Tesis, Proyecto, etc.
    estado = db.Column(db.String(50), default='PENDIENTE')
    fecha_entrega = db.Column(db.Date)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'))
    
    # Relación con Estudiante
    estudiante = db.relationship('Estudiante', backref='trabajos')
