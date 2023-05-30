"""
08 - Fazer uma função conta_inteiro que conte quantos elementos inteiros tem na lista
"""
import Aula14
# from Aula14 import ex04
from Aula14 import *

def conta_inteiro(l: list) -> int:
    cont = 0
    for elem in l:
        x = str(elem)
        if elem.isnumeric():
            cont = cont + 1
    return cont

lista = [10, 9, '_']
print(conta_inteiro(lista))
