import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.empresa import Empresa
from src.funcionario import Funcionario

class TestEmpresa(unittest.TestCase):
    def setUp(self):
        self.empresa = Empresa('Empresa 1')

    '''
        Teste 1
    '''
    def test_criar_empresa(self):
        # Inline Fixture Setup
        nome_empresa = 'Empresa 1'
        # Exercise SUT
        empresa = Empresa(nome_empresa)
        # Result Verification
        self.assertEqual(nome_empresa, empresa.nome)

    '''
        Teste 2
    '''
    def test_cadastrar_funcionario(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(1, len(self.empresa.funcionarios))

    '''
        Teste 3
    '''
    def test_nao_cadastrar_funcionario_nome_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario(123, '12345678900', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Nome inválido.")

    '''
        Teste 4
    '''
    def test_nao_cadastrar_funcionario_cpf_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as e:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(e.exception.args[0], "CPF inválido.")

    '''
        Teste 5
    '''
    def test_nao_cadastrar_funcionario_cargo_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 123, 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Cargo inválido.")

    '''
        Teste 6
    '''
    def test_nao_cadastrar_funcionario_salario_invalido(self):
        # Implicit Fixture Setup
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '12345678900', 'Gerente', 1000)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Salário inválido.")

    '''
        Teste 7
    '''
    def test_cadastrar_dois_funcionarios(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        self.empresa.cadastrarFuncionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(2, len(self.empresa.funcionarios))

    '''
        Teste 8
    '''
    def test_nao_cadastrar_funcionario_que_ja_esta_cadastrado(self):
        # Implicit Fixture Setup
        # Exercise SUT
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        with self.assertRaises(ValueError) as error:
            self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        # Result Verification
        self.assertEqual(error.exception.args[0], "Funcionário já cadastrado.")

    '''
        Teste 9
    '''
    def teste_encontra_funcionario_registrado(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        cpf = '123.456.789-00'
        self.empresa.cadastrarFuncionario('Fulano', cpf, 'Gerente', 1000.0)
        # Exercise SUT
        funcionario = self.empresa.encontrarFuncionario('123.456.789-00')
        # Result Verification
        self.assertEqual(cpf, funcionario.cpf)

    '''
        Teste 10
    '''
    def teste_nao_encontra_funcionario_nao_registrado(self):
        # Implicit Fixture Setup
        # Exercise SUT
        funcionario = self.empresa.encontrarFuncionario('123.456.789-00')
        # Result Verification
        self.assertEqual(None, funcionario)

    '''
        Teste 11
    '''
    def teste_cria_projeto_sem_equipe(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario = self.empresa.encontrarFuncionario('123.456.789-00')
        # Exercise SUT
        # A project must have name, cost, due date, responsible, and employees
        self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario, [])
        # Result Verification
        self.assertEqual(1, len(self.empresa.projetos))

    '''
        Teste 12
    '''
    def teste_cria_projeto_com_equipe_com_funcionario_registrado(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario_gerente = self.empresa.encontrarFuncionario('123.456.789-00')
        self.empresa.cadastrarFuncionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        funcionario_registrado = self.empresa.encontrarFuncionario('009.876.543-21')
        # Exercise SUT
        novo_projeto_id = self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario_gerente, [funcionario_registrado])
        # Result Verification
        self.assertEqual(1, len(self.empresa.projetos))
        self.assertTrue(novo_projeto_id)

    '''
        Teste 13
    '''
    def teste_nao_cria_projeto_com_equipe_com_funcionario_nao_registrado(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario_gerente = self.empresa.encontrarFuncionario('123.456.789-00')
        funcionario_nao_registrado = Funcionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario_gerente, [funcionario_nao_registrado])
        # Result Verification
        self.assertEqual(error.exception.args[0], f"Funcionário de cpf {funcionario_nao_registrado.cpf} não registrado.")

    '''
        Teste 14
    '''
    def teste_encontra_projeto_registrado(self):
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario_gerente = self.empresa.encontrarFuncionario('123.456.789-00')
        novo_projeto_id = self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario_gerente, [])
        # Exercise SUT
        projeto = self.empresa.encontrarProjeto(novo_projeto_id)
        # Result Verification
        self.assertEqual(novo_projeto_id, projeto.id)

    '''
        Teste 14
    '''
    def teste_nao_encontra_projeto_nao_registrado(self):
        # Inline Fixture Setup
        novo_projeto_id = 1
        # Exercise SUT
        projeto = self.empresa.encontrarProjeto(novo_projeto_id)
        # Result Verification
        self.assertEqual(None, projeto)

    '''
        Teste 16
    '''
    def teste_insere_funcionario_em_projeto(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario_gerente = self.empresa.encontrarFuncionario('123.456.789-00')
        novo_projeto_id = self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario_gerente, [])
        self.empresa.cadastrarFuncionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        funcionario_registrado = self.empresa.encontrarFuncionario('009.876.543-21')
        # Exercise SUT
        self.empresa.adicionarAoProjeto(novo_projeto_id, funcionario_registrado)
        # Result Verification
        projeto = self.empresa.encontrarProjeto(novo_projeto_id)
        self.assertEqual(len(projeto.equipe), 1)

    '''
        Teste 17
    '''
    def teste_nao_insere_funcionario_nao_registrado_em_projeto(self):
        # Implicit Fixture Setup
        # Inline Fixture Setup
        self.empresa.cadastrarFuncionario('Fulano', '123.456.789-00', 'Gerente', 1000.0)
        funcionario_gerente = self.empresa.encontrarFuncionario('123.456.789-00')
        novo_projeto_id = self.empresa.novoProjeto('Projeto1', 30.000, '2024/12/22', funcionario_gerente, [])
        funcionario_nao_registrado = Funcionario('Ciclano', '009.876.543-21', 'Gerente', 1000.0)
        # Exercise SUT
        with self.assertRaises(ValueError) as error:
            self.empresa.adicionarAoProjeto(novo_projeto_id, funcionario_nao_registrado)
        # Result Verification
        self.assertEqual(error.exception.args[0], f"Funcionário de cpf {funcionario_nao_registrado.cpf} não registrado.")

