import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.projeto import Projeto
from src.funcionario import Funcionario


class TestProjeto(unittest.TestCase):
    def setUp(self):
        self.gerente = Funcionario("Fábio", "123.456.789-50", "Gerente", 5250.0)
        self.projeto = Projeto(1, "Projeto 1", 50000, "2024-05-30", self.gerente)

    '''
        Teste 19
    '''
    def test_criar_projeto(self):
        # Exercise SUT
        projeto = Projeto(2, "Projeto 2", 750000, "2025-05-15", self.gerente)
        # Result Verification
        self.assertEqual(projeto.id, 2)
        self.assertEqual(projeto.titulo, "Projeto 2")
        self.assertEqual(projeto.custo, 750000)
        self.assertEqual(projeto.prazo, "2025-05-15")
        self.assertEqual(projeto.gerente, self.gerente)
        self.assertEqual(projeto.equipe, [])
