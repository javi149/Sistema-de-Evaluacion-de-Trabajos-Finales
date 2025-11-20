class TrabajoFactory:
    @staticmethod
    def create_trabajo(titulo, tipo, estudiante_id):
        if tipo == "tesis":
            return {"tipo": "tesis", "titulo": titulo, "requisito": "Investigacion"}
        elif tipo == "proyecto":
            return {"tipo": "proyecto", "titulo": titulo, "requisito": "Software"}
        return None
        