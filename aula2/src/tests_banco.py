import unittest
from banco import Banco
from dinheiro import Moeda
from agencia import Agencia

class TestBanco(unittest.TestCase):

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.nome = "Itaú"
        self.moeda = Moeda.BRL
        self.banco = Banco(self.nome, self.moeda)

    def test_get_nome(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        nome = self.banco.nome
        # RESULT VERIFICATION
        self.assertEqual(nome, self.nome)

    def test_get_moeda(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        moeda = self.banco.moeda
        # RESULT VERIFICATION
        self.assertEqual(moeda, self.moeda)

    def test_criar_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        # EXERCISE SUT
        agencia = self.banco.criar_agencia(nome)
        # RESULT VERIFICATION
        self.assertTrue(isinstance(agencia, Agencia))
        self.assertTrue(agencia.nome, nome)

    def test_obter_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertTrue(agencias)

    def test_obter_agencias_com_3_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.banco.criar_agencia("Carvoeira")
        self.banco.criar_agencia("Pantanal")
        self.banco.criar_agencia("Itacorubi")
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertTrue(len(agencias) == 3)

    def test_obter_agencias_com_0_agencias(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        agencias = self.banco.obter_agencias()
        # RESULT VERIFICATION
        self.assertFalse(agencias)

    def test_obter_agencia(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        # EXERCISE SUT
        agencia = self.banco.obter_agencia(nome)
        # RESULT VERIFICATION
        self.assertTrue(agencia)

    def test_obter_agencia_com_nome_inexistente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Carvoeira"
        self.banco.criar_agencia(nome)
        outroNome = "Trindade"
        # EXERCISE SUT
        agencia = self.banco.obter_agencia(outroNome)
        # RESULT VERIFICATION
        self.assertFalse(agencia)


if __name__ == '__main__':
    unittest.main()

