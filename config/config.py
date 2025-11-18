class ConfiguracionGlobal:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.APP_NAME = "Sistema de Evaluación de Trabajos Finales"
            cls._instance.VERSION = "1.0"
            cls._instance.INSTITUCION = "Universidad Ejemplo"
        return cls._instance
