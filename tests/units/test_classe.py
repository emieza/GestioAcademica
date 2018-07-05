
from models import *

from unittest import TestCase

class TestClasse(TestCase):

    def test_creacio(self):
        classe = Classe()
        assert isinstance(classe,Classe)
        del classe

    def test_llista_alumnes(self):
        NALUM = 100
        classe = Classe()
        for i in range( NALUM ):
            classe.crea_alumne(2000+i)
        assert len(classe.alumnes) == NALUM

