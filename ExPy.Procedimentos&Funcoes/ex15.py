"""
Fazer uma função que calcule o valor de delta a partir de 3 valores passados por parametro
x = calculo_delta(-1, 2, 3)
x valerá 8
"""
def calculo_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta
x = calculo_delta(-1, 2, 3)
print(x) 
