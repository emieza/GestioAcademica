
from models import *

from unittest import TestCase

class TestAlumne(TestCase):

    def test_creacio(self):
        classe = Classe()
        al = classe.crea_alumne( 3344 )
        assert isinstance(al,Alumne)

