from flask import Blueprint, jsonify
from models import Estudiante

estudiantes_bp = Blueprint('estudiantes', __name__, url_prefix='/estudiantes')

@estudiantes_bp.route('/', methods=['GET'])
def listar_estudiantes():
    # Retorna lista vacia o datos si existen
    alumnos = Estudiante.query.all()
    resultado = [{"id": a.id, "nombre": a.nombre, "carrera": a.carrera} for a in alumnos]
    return jsonify(resultado)
