from flask import Blueprint, jsonify, request
from app import db
from models import Trabajo

trabajos_bp = Blueprint('trabajos', __name__, url_prefix='/trabajos')

@trabajos_bp.route('/', methods=['GET'])
def listar_trabajos():
    trabajos = Trabajo.query.all()
    resultado = [{
        "id": t.trabajos_id, 
        "titulo": t.titulo, 
        "estado": t.estado,
        "estudiante_id": t.estudiante_id,
        "tipo_trabajo": t.tipo_id
    } for t in trabajos]
    return jsonify(resultado)

@trabajos_bp.route('/', methods=['POST'])
def crear_trabajo():
    data = request.get_json()
    nuevo = Trabajo(
        titulo=data.get('titulo'),
        estado="PENDIENTE", # Valor inicial por defecto
        fecha_entrega=data.get('fecha_entrega'),
        estudiante_id=data.get('estudiante_id'),
        tipo_id=data.get('tipo_id') # Esto define si es Tesis, Pasantía, etc.
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Trabajo registrado", "id": nuevo.trabajos_id}), 201
