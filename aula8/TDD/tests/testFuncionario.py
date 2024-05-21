import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.funcionario import Funcionario

class TestFuncionario(unittest.TestCase):
    
    def setUp(self):
        self.funcionario = Funcionario("José", "123.456.789-10", "Analista", 2550.0)

    '''
        Teste 18
    '''
    def test_criar_funcionario(self):
        # Exercise SUT
        funcionario = Funcionario("João", "345.678.901-20", "Estagiário", 1200.0)
        # Result Verification
        self.assertEqual(funcionario.nome, "João")
        self.assertEqual(funcionario.cpf, "345.678.901-20")
        self.assertEqual(funcionario.cargo, "Estagiário")
        self.assertEqual(funcionario.salario, 1200.0)