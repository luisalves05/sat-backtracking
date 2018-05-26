#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Disciplina de Complexidade de Algortimos
# Autores: Jose Luis, Vinicius Rocha e Vanderson Pontes
#

import unittest
import sat
import time, datetime


class Test3Sat(unittest.TestCase):
    def teste1(self):
        start = time.time()
        resultado = sat.executar("n50m275.txt")
        end = time.time()
        print("Solução: {0}".format(resultado[1]))
        print("Tempo: {0}".format(str(datetime.timedelta(seconds=end-start))))
        self.assertEqual(resultado[0], "sat")

    def teste2(self):
        start = time.time()
        resultado = sat.executar("n50m300.txt")
        end = time.time()
        print("Solução: {0}".format(resultado[1]))
        print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
        self.assertEqual(resultado[0], "sat")

    #
    # Casos pequenos de testes feito por nós
    #
    # def teste1(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste1-SAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "sat")
    #
    # def teste2(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste2-UNSAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "unsat")
    #
    # def teste3(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste3-UNSAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "unsat")
    #
    # def teste4(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste4-SAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "sat")def teste1(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste1-SAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "sat")
    #
    # def teste2(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste2-UNSAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "unsat")
    #
    # def teste3(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste3-UNSAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "unsat")
    #
    # def teste4(self):
    #     start = time.time()
    #     resultado = sat.executar("MeuTeste4-SAT.txt")
    #     end = time.time()
    #     print("Solução: {0}".format(resultado[1]))
    #     print("Tempo: {0}".format(str(datetime.timedelta(seconds=end - start))))
    #     self.assertEqual(resultado[0], "sat")


if __name__ == "__main__":
    unittest.main()
