from sqlalchemy import text
from app import app, db

def sembrar_datos_definitivos():
    with app.app_context():
        print("--- SEMBRANDO DATOS (VERSIÓN FINAL) ---")
        
        try:
            # 1. INSTITUCIÓN
            print("1. Creando Institución...")
            db.session.execute(text("INSERT IGNORE INTO instituciones (id, nombre) VALUES (1, 'Universidad de Prueba')"))

            # 2. TIPO DE TRABAJO
            print("2. Creando Tipo de Trabajo...")
            db.session.execute(text("INSERT IGNORE INTO tipos_trabajo (id, nombre) VALUES (1, 'Tesis de Grado')"))

            # 3. ESTUDIANTE (¡Corregido: Agregamos RUT!)
            print("3. Creando Estudiante...")
            db.session.execute(text("""
                INSERT IGNORE INTO estudiantes (id, nombre, apellido, rut, email, carrera) 
                VALUES (1, 'Pepito', 'Pérez', '12.345.678-9', 'pepito@test.com', 'Ingeniería')
            """))

            # 4. TRABAJO (¡Corregido: Usamos 'tipo_id'!)
            print("4. Creando Trabajo #1...")
            # Usamos INSERT IGNORE para no duplicar si ya existe
            db.session.execute(text("""
                INSERT IGNORE INTO trabajos (id, titulo, tipo_id, estudiante_id, fecha_entrega, nota_aprobacion) 
                VALUES (1, 'Sistema de Evaluación Final', 1, 1, NOW(), 4.0)
            """))

            # 5. CRITERIOS (Para el cálculo de notas)
            print("5. Creando Criterios...")
            # Criterio 1: Informe (60%)
            db.session.execute(text("""
                INSERT INTO criterios (id, institucion_id, nombre, ponderacion) 
                VALUES (101, 1, 'Informe Escrito', 60.0) 
                ON DUPLICATE KEY UPDATE ponderacion=60.0
            """))
            # Criterio 2: Oral (40%)
            db.session.execute(text("""
                INSERT INTO criterios (id, institucion_id, nombre, ponderacion) 
                VALUES (102, 1, 'Sustentación Oral', 40.0) 
                ON DUPLICATE KEY UPDATE ponderacion=40.0
            """))

            # 6. EVALUADOR (¡Corregido: Agregamos ROL!)
            print("6. Creando Evaluador...")
            db.session.execute(text("""
                INSERT IGNORE INTO evaluadores (id, nombre, email, rol, tipo) 
                VALUES (1, 'Profesor X', 'profe@test.com', 'Docente', 'Interno')
            """))

            # 7. EVALUACIÓN (La cabecera)
            print("7. Creando Evaluación...")
            # Limpiamos evaluación previa para asegurar
            db.session.execute(text("DELETE FROM evaluaciones WHERE id = 999"))
            
            db.session.execute(text("""
                INSERT INTO evaluaciones (id, trabajo_id, evaluador_id, nota_final, comentarios, fecha_evaluacion) 
                VALUES (999, 1, 1, 0.0, 'Prueba Final Exitosa', NOW()) 
            """))

            # 8. NOTAS DETALLE (Lo que calcula tu Strategy)
            print("8. Insertando Notas...")
            # Limpiamos notas previas
            db.session.execute(text("DELETE FROM evaluacion_detalle WHERE evaluacion_id = 999"))
            
            # Nota 5.0 en Informe (60%)
            db.session.execute(text("INSERT INTO evaluacion_detalle (evaluacion_id, criterio_id, nota, subtotal) VALUES (999, 101, 5.0, 0)"))
            
            # Nota 3.0 en Oral (40%)
            db.session.execute(text("INSERT INTO evaluacion_detalle (evaluacion_id, criterio_id, nota, subtotal) VALUES (999, 102, 3.0, 0)"))

            db.session.commit()
            print("\n ¡LISTO! Base de datos poblada correctamente.")
            print("   Cálculo esperado: (5.0 * 0.6) + (3.0 * 0.4) = 4.2")
            print("VE AHORA AL NAVEGADOR: http://127.0.0.1:5000/api/calcular-nota/1")

        except Exception as e:
            db.session.rollback()
            print(f"\n ERROR: {e}")

if __name__ == "__main__":
    sembrar_datos_definitivos()