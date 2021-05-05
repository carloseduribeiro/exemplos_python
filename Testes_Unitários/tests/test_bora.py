from unittest import TestCase
from funcoes.bora import soma, raiz


class TestantoBora(TestCase):

    def test_soma_is_work(self):
        n1, n2 = 10, 12
        # Testa se uma coisa é igual a outra:
        self.assertEqual(22, soma(n1, n2))

    def test_raiz_is_work(self):
        type_test = "A"
        # Testa se lança uma excessão do tipo TypeError:
        with self.assertRaises(TypeError):
            raiz(type_test)

        test_value = -9
        # Testa se lança uma excessão do tipo ValueError:
        with self.assertRaises(ValueError):
            raiz(test_value)

        # Testa o retorno é o que deve retornar:
        self.assertEqual(12, raiz(144))
