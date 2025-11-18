import os
from flask import Flask
from database import db
from config.config import ConfiguracionGlobal
from routes.estudiantes import estudiantes_bp

# Intentar cargar dotenv si existe, sino continuar
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def create_app():
    app = Flask(__name__)
    
    # Configuración de Base de Datos (Prioridad: MySQL via .env, sino SQLite local)
    db_uri = os.getenv('DATABASE_URL')
    if db_uri:
        app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///evaluacion.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    # Inicializar Singleton de Configuración
    ConfiguracionGlobal()

    # Registrar Rutas
    app.register_blueprint(estudiantes_bp)

    @app.route("/ping")
    def ping():
        return {"msg": "pong", "status": "ok"}

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all() # Crea las tablas vacias si no existen
    app.run(debug=True)
