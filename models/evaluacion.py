from database import db

class Evaluacion(db.Model):
    __tablename__ = 'evaluaciones'
    id = db.Column(db.Integer, primary_key=True)
    trabajo_id = db.Column(db.Integer, db.ForeignKey('trabajos.id'), nullable=False)
    evaluador_id = db.Column(db.Integer, db.ForeignKey('evaluadores.id'), nullable=False)
    nota_final = db.Column(db.Float)
    comentarios = db.Column(db.Text)
    fecha_evaluacion = db.Column(db.Date)
    
    # Relaciones
    trabajo = db.relationship('Trabajo', backref='evaluaciones')
    evaluador = db.relationship('Evaluadores', backref='evaluaciones')

