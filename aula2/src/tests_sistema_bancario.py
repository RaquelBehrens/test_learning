import unittest
from conta import Conta
from dinheiro import Dinheiro, Moeda
from agencia import Agencia
from banco import Banco
from sistema_bancario import SistemaBancario
from operacao import EstadosDeOperacao

class TestSistemaBancario(unittest.TestCase):

    def setUp(self):
        # IMPLICIT FIXTURE SETUP
        self.sistemaBancario = SistemaBancario()
        self.titular = "Raquel"
        self.codigo = 1
        self.banco = Banco("Itaú", Moeda.BRL)
        self.agencia = Agencia("Trindade", 234, self.banco)
        self.conta = Conta(self.titular, self.codigo, self.agencia)

    def test_criar_banco(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Itaú"
        moeda = Moeda.BRL
        # EXERCISE SUT
        banco = self.sistemaBancario.criar_banco(nome, moeda)
        # RESULT VERIFICATION
        self.assertTrue(isinstance(banco, Banco))

    def test_depositar(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        # EXERCISE SUT
        operacao = self.sistemaBancario.depositar(self.conta, quantia)
        # RESULT VERIFICATION
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)

    def test_sacar_conta_com_saldo_suficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        self.sistemaBancario.depositar(self.conta, quantia)
        # EXERCISE SUT
        operacao = self.sistemaBancario.sacar(self.conta, quantia)
        # RESULT VERIFICATION
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)

    def test_sacar_conta_com_saldo_insuficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        # EXERCISE SUT
        operacao = self.sistemaBancario.sacar(self.conta, quantia)
        # RESULT VERIFICATION
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SALDO_INSUFICIENTE)

    def test_sacar_moeda_diferente_da_moeda_da_conta(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.USD, 100, 0)
        # EXERCISE SUT
        operacao = self.sistemaBancario.sacar(self.conta, quantia)
        # RESULT VERIFICATION
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.MOEDA_INVALIDA)

    def test_transferir_de_conta_com_saldo_suficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        self.sistemaBancario.depositar(self.conta, quantia)
        outra_conta = Conta("Fulano", 2, self.agencia)
        # EXERCISE SUT
        operacao = self.sistemaBancario.transferir(self.conta, outra_conta, quantia)
        # RESULT VERIFICATION
        self.assertEqual(operacao.obter_estado(), EstadosDeOperacao.SUCESSO)
        self.assertEqual(outra_conta.calcular_saldo(), quantia)


if __name__ == '__main__':
    unittest.main()

