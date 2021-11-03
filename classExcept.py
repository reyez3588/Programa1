"""
En este documento se crearan las clases de error propias
"""

class misErrores(Exception):
    """Clase base para las excepcines de este módulo."""
    pass

class fatalError(misErrores):
    """
    Este error es propio
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class myValueError(ValueError):
    """
    Este error es propio
    """
    def __init__(self):
        super().__init__()