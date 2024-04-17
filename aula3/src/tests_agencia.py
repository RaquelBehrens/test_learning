import unittest
from agencia import Agencia
from conta import Conta
from banco import Banco
from dinheiro import Moeda

class TestAgencia(unittest.TestCase):

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.nome = "Trindade"
        self.codigo = 234
        self.banco = Banco("Itaú", Moeda.BRL)
        self.agencia = Agencia(self.nome, self.codigo, self.banco)

    def test_get_nome(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        nome = self.agencia.nome
        # RESULT VERIFICATION
        self.assertEqual(nome, self.nome)

    def test_get_banco(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        banco = self.agencia.banco
        # RESULT VERIFICATION
        self.assertEqual(banco, self.banco)

    def test_obter_identificador(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        identificador = self.agencia.obter_identificador()
        # RESULT VERIFICATION
        self.assertEqual(identificador, str(self.codigo))

    def test_criar_conta(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        titular = "Raquel"
        # EXERCISE SUT
        conta = self.agencia.criar_conta(titular)
        # RESULT VERIFICATION
        self.assertTrue(isinstance(conta, Conta))

    def test_obter_contas(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        titular = "Raquel"
        self.agencia.criar_conta(titular)
        # EXERCISE SUT
        contas = self.agencia.obter_contas()
        # RESULT VERIFICATION
        self.assertTrue(contas)

    def test_obter_contas_com_3_contas(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        self.agencia.criar_conta("Raquel Conta 1")
        self.agencia.criar_conta("Raquel Conta 2")
        self.agencia.criar_conta("Raquel Conta 3")
        # EXERCISE SUT
        contas = self.agencia.obter_contas()
        # RESULT VERIFICATION
        self.assertTrue(len(contas) == 3)

    def test_obter_contas_com_0_contas(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        contas = self.agencia.obter_contas()
        # RESULT VERIFICATION
        self.assertFalse(contas)

    def test_obter_conta(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        titular = "Raquel"
        self.agencia.criar_conta(titular)
        conta_identificador: Conta = self.agencia.obter_contas()[0]
        identificador = conta_identificador.obter_identificador()
        # EXERCISE SUT
        conta = self.agencia.obter_conta(identificador)
        # RESULT VERIFICATION
        self.assertTrue(isinstance(conta, Conta))
        self.assertEqual(conta.obter_identificador(), identificador)

    def test_obter_conta_com_identificador_inválido(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        titular = "Raquel"
        self.agencia.criar_conta(titular)
        identificador = 1
        # EXERCISE SUT
        conta = self.agencia.obter_conta(identificador)
        # RESULT VERIFICATION
        self.assertIsNone(conta)


if __name__ == '__main__':
    unittest.main()

