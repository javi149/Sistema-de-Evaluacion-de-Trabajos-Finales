from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# 1. IMPORTAMOS LA DB DESDE TU ARCHIVO database.py
from database import db 
# 2. IMPORTAMOS LAS RUTAS
from routes.notas_routes import notas_bp 

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuración
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
dbname = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --- 3. INICIALIZAR LA APP CON LA DB QUE IMPORTAMOS ---
db.init_app(app) 
# ------------------------------------------------------

# Registrar rutas
app.register_blueprint(notas_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)