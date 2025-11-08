import unittest
from calculator_actors import CalculatorSystem

class TestCalculatorActors(unittest.TestCase):
    def setUp(self):
        self.system = CalculatorSystem()
        self.system.start()
    
    def tearDown(self):
        self.system.stop()
    
    def test_soma(self):
        """Teste soma usando ator"""
        result = self.system.calculate("soma", 5.0, 3.0)
        self.assertEqual(result["result"], 8.0)
        self.assertIn("request_id", result)
    
    def test_subtracao(self):
        """Teste subtração usando ator"""
        result = self.system.calculate("subtracao", 15.0, 7.0)
        self.assertEqual(result["result"], 8.0)
        self.assertIn("request_id", result)
    
    def test_multiplicacao(self):
        """Teste multiplicação usando ator"""
        result = self.system.calculate("multiplicacao", 4.0, 6.0)
        self.assertEqual(result["result"], 24.0)
        self.assertIn("request_id", result)
    
    def test_divisao(self):
        """Teste divisão usando ator"""
        result = self.system.calculate("divisao", 20.0, 4.0)
        self.assertEqual(result["result"], 5.0)
        self.assertIn("request_id", result)
    
    def test_divisao_por_zero(self):
        """Teste divisão por zero usando ator"""
        result = self.system.calculate("divisao", 10.0, 0.0)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Divisão por zero não permitida")
    
    def test_operacao_invalida(self):
        """Teste operação inválida"""
        result = self.system.calculate("potencia", 2.0, 3.0)
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Operação inválida")
    
    def test_request_id_unico(self):
        """Teste que request_id é único"""
        result1 = self.system.calculate("soma", 1.0, 1.0)
        result2 = self.system.calculate("soma", 1.0, 1.0)
        self.assertNotEqual(result1["request_id"], result2["request_id"])

if __name__ == '__main__':
    unittest.main()