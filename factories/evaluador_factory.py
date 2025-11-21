class EvaluadorFactory:
    """
    Fábrica para crear configuraciones de evaluadores.
    Recibe un tipo (string) y devuelve el ROL y TIPO oficial para la BD.
    """
    @staticmethod
    def crear_perfil(tipo_evaluador):
        # Limpiamos la entrada
        tipo = tipo_evaluador.lower().strip()

        if tipo == "guia":
            return {
                "tipo": "Profesor Guía",
                "rol": "Supervisor Principal", # Este va a la columna 'rol'
                "permisos": "total"
            }
        
        elif tipo == "comision":
            return {
                "tipo": "Comisión Evaluadora",
                "rol": "Evaluador Externo", # Este va a la columna 'rol'
                "permisos": "lectura_nota"
            }
        
        elif tipo == "profesor":
            return {
                "tipo": "Profesor Informante",
                "rol": "Revisor Técnico", # Este va a la columna 'rol'
                "permisos": "lectura"
            }
        
        else:
            return None
            