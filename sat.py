
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Disciplina de Complexidade de Algortimos
# Autores: Jose Luis, Vinicius Rocha e Vanderson Pontes
#

import copy
import sys, getopt
import time

"""
    Função resposável por resolver o problema SAT

    Args:
        param1: contém todas as clausulas as serem processadas em um formato
        de lista de listas
"""

def resolver_sat(clausulas):

    # Se não tem clausulas
    if not clausulas:
        return "sat"

    # Se alguma clausula é vazia, retorna unsat
    for c in clausulas:
       if None in c:
           return "unsat"

    elem = clausulas[0][0] # primeiro elemento

    estado_atual = copy.deepcopy(clausulas)

    for c in clausulas:
        if -elem in c and elem in c: # a clausula se torna falsa
            return "unsat"
        if -elem in c:
            c.clear()
        else:
            for e in c:
                if e == elem:
                    c.remove(e)
                if not c:
                    c.append(None)

    # Removando listas vazias: expressão verdadeira
    clausulas = [c for c in clausulas if len(c) != 0]

    # Primeira Parte: elemento receberá 0
    resultado = resolver_sat(clausulas)

    if resultado == "sat":
        return resultado

    clausulas = copy.deepcopy(estado_atual)

    for c in clausulas:
         if -elem in c and elem in c: # se clausula se torna falsa
             return "unsat"
         if elem in c:
             c.clear()
         else:
             for e in c:
                 if e == -elem:
                     c.remove(e)
                 if not c:
                     c.append(None)

    # Removendo listas vazias
    clausulas = [c for c in clausulas if len(c) != 0]
    # Segunda Parte: se for unsat, vamos tentar com 1
    resultado = resolver_sat(clausulas)

    return resultado

"""
    Função resposável por tratar linha e retornar uma lista de ints

    Args:
        param1: linha a ser processada.
"""
def processar_linha(linha):
    itens = linha.strip()
    while '  ' in itens:
        itens = itens.replace('  ', ' ')
    itens = itens.split(" ")
    return [int(n) for n in itens]


def executar(arquivo_entrada):

    clausulas = []
    primeira_linha = False

    # Lendo o arquivo teste de entrada;
    with open(arquivo_entrada, 'rt') as f:
        for linha in f:
            itens = processar_linha(linha)
            if primeira_linha and itens[0] > 4:
                proxima_linha = next(f)
                proxima_linha = processar_linha(proxima_linha)
                itens = itens + proxima_linha
            primeira_linha = True
            clausulas.append(itens)

    clausulas = [claus[2:] for claus in clausulas[1:]] # removendo dois primeiros
    return resolver_sat(clausulas)

# 3-sat.py
