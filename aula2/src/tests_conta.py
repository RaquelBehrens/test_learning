import unittest
from conta import Conta
from dinheiro import Dinheiro, Moeda
from agencia import Agencia
from banco import Banco
from transacao import Entrada

class TestConta(unittest.TestCase):

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.titular = "Raquel"
        self.codigo = 1
        self.banco = Banco("Itaú", Moeda.BRL)
        self.agencia = Agencia("Trindade", 234, self.banco)
        self.conta = Conta(self.titular, self.codigo, self.agencia)

    def test_get_titular(self):
        # INLINE FIXTURE SETUP
        # EXERCISE SUT
        titular = self.conta.titular
        # RESULT VERIFICATION
        self.assertEqual(titular, self.titular)

    def test_get_moeda(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        agencia = self.agencia
        # RESULT VERIFICATION
        self.assertEqual(agencia, self.agencia)

    def test_adicionar_transacao(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        transacao = Entrada(100)
        # EXERCISE SUT
        self.conta.adicionar_transacao(transacao)
        # RESULT VERIFICATION

    def test_calcular_saldo_com_0_transacoes(self):
        # IMPLICIT FIXTURE SETUP
        # EXERCISE SUT
        saldo = self.conta.calcular_saldo()
        # RESULT VERIFICATION
        self.assertEqual(saldo.formatado(), "0,00")

if __name__ == '__main__':
    unittest.main()

