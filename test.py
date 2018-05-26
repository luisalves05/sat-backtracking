#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Disciplina de Complexidade de Algortimos
# Autores: Jose Luis, Vinicius Rocha e Vanderson Pontes
#

import unittest
import sat
import time


class Test3Sat(unittest.TestCase):
    def teste1(self):
        start = time.time()
        resultado = sat.executar("n50m275.txt")
        end = time.time()
        print("Tempo: {0}".format(end - start))
        self.assertEqual(resultado, "sat")

    def teste2(self):
        start = time.time()
        resultado = sat.executar("n50m300.txt")
        end = time.time()
        print("Tempo: {0}".format(end - start))
        self.assertEqual(resultado, "sat")

    #
    # Casos pequenos de testes feito por nós
    #
    def teste1(self):
        resultado = sat.executar("MeuTeste1-SAT.txt")
        self.assertEqual(resultado, "sat")

    def teste2(self):
        resultado = sat.executar("MeuTeste2-UNSAT.txt")
        self.assertEqual(resultado, "unsat")

    def teste3(self):
        resultado = sat.executar("MeuTeste3-UNSAT.txt")
        self.assertEqual(resultado, "unsat")

    def teste4(self):
        resultado = sat.executar("MeuTeste4-SAT.txt")
        self.assertEqual(resultado, "sat")


if __name__ == "__main__":
    unittest.main()
