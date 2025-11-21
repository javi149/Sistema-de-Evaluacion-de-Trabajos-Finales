from database import db

class Evaluador(db.Model):
    __tablename__ = 'evaluadores'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100))
    
    # --- TUS COLUMNAS DE FACTORY (Benja) ---
    rol_asignado = db.Column(db.String(100)) # Para guardar "Profesor Guía"
    peso_voto = db.Column(db.Float)          # Para guardar "0.6"
    tipo = db.Column(db.String(50)) # Guia, Comision, Informante
    # ---------------------------------------

    # Relación con trabajos (opcional por ahora, pero útil a futuro)
    # trabajo_id = db.Column(db.Integer, db.ForeignKey('trabajos.id'))