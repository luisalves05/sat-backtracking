#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Disciplina de Complexidade de Algortimos
# Autores: Jose Luis, Vinicius Rocha e Vanderson Pontes
#

import unittest
import sat

class Test3Sat(unittest.TestCase):
    
    def teste1(self):
        resultado = sat.executar("Teste1.txt")
        self.assertEqual(resultado, "unsat")

    def teste2(self):
        resultado = sat.executar("Teste2.txt")
        self.assertEqual(resultado, "unsat")

    def teste3(self):
        resultado = sat.executar("Teste3.txt")
        self.assertEqual(resultado, "unsat")

    def teste4(self):
        resultado = sat.executar("Teste4.txt")
        self.assertEqual(resultado, "unsat")

    #
    # Casos pequenos de testes feito por nós
    #
    def teste5(self):
        resultado = sat.executar("Teste5.txt")
        self.assertEqual(resultado, "sat")

    def teste6(self):
        resultado = sat.executar("Teste6.txt")
        self.assertEqual(resultado, "unsat")

if __name__ == "__main__":
    unittest.main()
