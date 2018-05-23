
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

def resolver_sat(clausulas):

    # Se não tem clausulas
    if not clausulas:
        return "sat"

    # Se alguma clausula é vazia, retorna unsat
    for c in clausulas:
        if not c:
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
                if e == elem and len(c) == 1: # se torna falsa
                    return "unsat"
                if e == elem:
                    c.remove(e)

    # Removando listas vazias
    clausulas = [c for c in clausulas if c]
    # Primeira Parte: elemento receberá 0
    resultado = resolver_sat(clausulas)

    if resultado == "unsat":
        clausulas = copy.deepcopy(estado_atual)
        for c in clausulas:
             if -elem in c and elem in c: # se clausula se torna falsa
                 return "unsat"
             if elem in c:
                 c.clear()
             else:
                 for e in c:
                     if e == -elem and len(c) == 1: # se torna falsa
                         return "unsat"
                     if e == -elem:
                         c.remove(e)

        # Removendo listas vazias
        clausulas = [c for c in clausulas if c]
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


def main():

    clausulas = []
    primeira_linha = False

    # Lendo o arquivo teste de entrada;
    with open('Teste0.txt', 'rt') as f:
        for linha in f:
            itens = processar_linha(linha)
            if primeira_linha and itens[0] > 4:
                proxima_linha = next(f)
                proxima_linha = processar_linha(proxima_linha)
                itens = itens + proxima_linha
            primeira_linha = True
            clausulas.append(itens)

    clausulas = [claus[2:] for claus in clausulas[1:]] # removendo dois primeiros
    print(resolver_sat(clausulas))

if __name__ == "__main__":
    main()

# 3-sat.py
