from django.test import TestCase

#clase que heredamos clses con metodos cada una de nuestras pruebas

class PrimerTest(TestCase):
    def test_1(self,):
        self.assertEqual(1,1)