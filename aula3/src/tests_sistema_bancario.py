import unittest
from hamcrest import assert_that, any_of, less_than, equal_to, contains_string, less_than_or_equal_to, has_items, is_not, instance_of, all_of, greater_than_or_equal_to, is_, has_length
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
        self.conta_principal = Conta(self.titular, self.codigo, self.agencia)

    def test_criar_banco(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        nome = "Itaú"
        moeda = Moeda.BRL
        # EXERCISE SUT
        banco = self.sistemaBancario.criar_banco(nome, moeda)
        # RESULT VERIFICATION
        assert_that(banco.nome, contains_string(nome))

    def test_obter_banco(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        moeda_brasil = Moeda.BRL
        # EXERCISE SUT
        banco_itau = self.sistemaBancario.criar_banco("Itaú", moeda_brasil)
        # RESULT VERIFICATION
        assert_that(banco_itau, instance_of(Banco))

    def test_obter_bancos(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        moeda_brasil = Moeda.BRL
        banco_itau = self.sistemaBancario.criar_banco("Itaú", moeda_brasil)
        banco_bradesco = self.sistemaBancario.criar_banco("Bradesco", moeda_brasil)
        # EXERCISE SUT
        bancos = self.sistemaBancario.obter_bancos()
        # RESULT VERIFICATION
        assert_that(bancos, has_items(banco_itau, banco_bradesco))

    def test_obter_bancos_10_bancos_criados(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        moeda_brasil = Moeda.BRL
        self.sistemaBancario.criar_banco("Itaú", moeda_brasil)
        self.sistemaBancario.criar_banco("Bradesco", moeda_brasil)
        self.sistemaBancario.criar_banco("Nubank", moeda_brasil)
        self.sistemaBancario.criar_banco("Banco Do Brasil", moeda_brasil)
        self.sistemaBancario.criar_banco("Unibanco", moeda_brasil)
        self.sistemaBancario.criar_banco("Santander", moeda_brasil)
        self.sistemaBancario.criar_banco("Caixa Econômica Federal", moeda_brasil)
        self.sistemaBancario.criar_banco("Banrisul", moeda_brasil)
        self.sistemaBancario.criar_banco("Mercado Pago", moeda_brasil)
        self.sistemaBancario.criar_banco("C6", moeda_brasil)
        # EXERCISE SUT
        bancos = self.sistemaBancario.obter_bancos()
        # RESULT VERIFICATION
        assert_that(bancos, has_length(10))

    def test_depositar(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia_depoisitada = Dinheiro(Moeda.BRL, 100, 0)
        # EXERCISE SUT
        self.sistemaBancario.depositar(self.conta_principal, quantia_depoisitada)
        # RESULT VERIFICATION
        assert_that(self.conta_principal.calcular_saldo(), equal_to(quantia_depoisitada))

    def test_sacar_conta_com_saldo_suficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia_depoisitada = Dinheiro(Moeda.BRL, 100, 0)
        quantia_esperada_apos_saque = Dinheiro(Moeda.BRL, 0, 0)
        self.sistemaBancario.depositar(self.conta_principal, quantia_depoisitada)
        # EXERCISE SUT
        self.sistemaBancario.sacar(self.conta_principal, quantia_depoisitada)
        # RESULT VERIFICATION
        quantia_sacada = self.conta_principal.calcular_saldo().obter_quantia()
        assert_that(quantia_sacada.inteiro, less_than_or_equal_to(quantia_esperada_apos_saque.inteiro))
        assert_that(quantia_sacada.inteiro, any_of(less_than(quantia_esperada_apos_saque.inteiro), equal_to(quantia_esperada_apos_saque.inteiro)))

    def test_sacar_conta_com_saldo_insuficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        # EXERCISE SUT
        operacao = self.sistemaBancario.sacar(self.conta_principal, quantia)
        # RESULT VERIFICATION
        assert_that(operacao.obter_estado(), is_not(EstadosDeOperacao.SUCESSO))

    def test_sacar_moeda_diferente_da_moeda_da_conta(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.USD, 100, 0)
        # EXERCISE SUT
        operacao = self.sistemaBancario.sacar(self.conta_principal, quantia)
        # RESULT VERIFICATION
        assert_that(operacao.obter_estado(), all_of(EstadosDeOperacao.MOEDA_INVALIDA))

    def test_transferir_de_conta_com_saldo_suficiente(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        self.sistemaBancario.depositar(self.conta_principal, quantia)
        conta_receptora = Conta("Fulano", 2, self.agencia)
        # EXERCISE SUT
        self.sistemaBancario.transferir(self.conta_principal, conta_receptora, quantia)
        # RESULT VERIFICATION
        saldo_resultante_conta_receptora = conta_receptora.calcular_saldo().obter_quantia()
        assert_that(saldo_resultante_conta_receptora.inteiro, greater_than_or_equal_to(quantia.inteiro))

    def test_saldo_ficara_negativo_se_deposito_igual_ao_saldo(self):
        # IMPLICIT FIXTURE SETUP
        # INLINE FIXTURE SETUP
        quantia = Dinheiro(Moeda.BRL, 100, 0)
        self.sistemaBancario.depositar(self.conta_principal, quantia)
        # EXERCISE SUT
        resultado = self.sistemaBancario.saldo_ficara_negativo(self.conta_principal.calcular_saldo(), quantia)
        # RESULT VERIFICATION
        assert_that(resultado, is_(False))


if __name__ == '__main__':
    unittest.main()

