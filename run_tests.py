#!/usr/bin/env python3
import unittest
import sys

if __name__ == '__main__':
    try:
        # Teste calculadora com modelo de atores
        suite = unittest.TestLoader().loadTestsFromName('test_calculator_actors')
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Exit com código baseado no resultado
        sys.exit(0 if result.wasSuccessful() else 1)
    except Exception as e:
        print(f"Erro ao executar testes: {e}")
        sys.exit(1)