

class Alumne():
    def __init__(self,codi):
        self.estat = None
        self.__codi = codi
        # TODO: anem a BBDD i busquem alumne...
        self.nom = "Manolo"
        self.cognoms = "Perez"


class Profe():
    def __init__(self):
        self.logat = None
    def loga(self,usuari,contrasenya):
        self.usuari = usuari
        self.logat = True


class Classe():
    alumnes = []
    def __init__(self):
        pass
    def crea_alumne(self,codi):
        alumne = Alumne(codi)
        self.alumnes.append(alumne)
        return alumne
