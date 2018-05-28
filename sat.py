
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Disciplina de Complexidade de Algortimos
# Autores: Jose Luis, Vinicius Rocha e Vanderson Pontes
#

import copy


"""
    Função resposável por resolver o problema SAT

    Args:
        param1: contém todas as clausulas as serem processadas em um formato
        de lista de listas
"""


def resolver_sat(clausulas, solu, elem):

    # Se não tem clausulas
    if not clausulas:
        return "sat"

    # Se alguma clausula é vazia, retorna unsat
    for c in clausulas:
        if None in c:
            return "unsat"

    elemento = clausulas[0][0] # primeiro elemento
    estado_anterior = copy.deepcopy(clausulas)

    if elemento < 0:
        solu[-elemento] = 1
    else:
        solu[elemento] = 0

    for i in range(0, len(clausulas)):
        if -elemento in clausulas[i] and elemento in clausulas[i]: # a clausula se torna falsa
            return "unsat"
        elif -elemento in clausulas[i]:
            clausulas[i].clear()
        else:
            clausulas[i] = [e for e in clausulas[i] if e != elemento]
            if len(clausulas[i]) == 0:
                clausulas[i].append(None)

    # Removando listas vazias: expressões verdadeira
    clausulas = [c for c in clausulas if len(c) != 0]
    # Primeira Parte: elemento receberá 0

    if resolver_sat(clausulas, solu, elemento) == "sat":
        return "sat"

    clausulas = copy.deepcopy(estado_anterior)

    if elemento < 0:
        solu[-elemento] = 0
    else:
        solu[elemento] = 1

    for i in range(0, len(clausulas)):
        if -elemento in clausulas[i] and elemento in clausulas[i]: # a clausula se torna falsa
            return "unsat"
        elif elemento in clausulas[i]: # elemento é 1
            clausulas[i].clear()
        else:
            clausulas[i] = [e for e in clausulas[i] if e != -elemento]
            if len(clausulas[i]) == 0:
                clausulas[i].append(None)

    # Removendo listas vazias: expressões verdadeira
    clausulas = [c for c in clausulas if len(c) != 0]
    # Segunda Parte: se for unsat, vamos tentar com 1
    if resolver_sat(clausulas, solu, elemento) == "sat":
        return "sat"

    return "unsat"


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
    # primeira_linha = False

    # Lendo o arquivo teste de entrada;
    with open(arquivo_entrada, 'rt') as f:
        for linha in f:
            itens = processar_linha(linha)
            # if primeira_linha and itens[0] > 4:
            #    proxima_linha = next(f)
            #    proxima_linha = processar_linha(proxima_linha)
            #    itens = itens + proxima_linha
            # primeira_linha = True
            clausulas.append(itens)

    # clausulas = [claus[2:] for claus in clausulas[1:]] # removendo dois primeiros
    clausulas = clausulas[1:]

    solu = dict()
    resultado = resolver_sat(clausulas, solu, None)
    return resultado, solu

# 3-sat.py
