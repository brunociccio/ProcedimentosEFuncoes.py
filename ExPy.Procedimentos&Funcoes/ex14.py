"""
Faça uma função que calcule a raiz quadrada de um número passado por parametro
x = raizquadrada(25)
x valerá 5
"""
def raiz_quadrada(numero):
    if numero == 0:
        return 0

    chute_inicial = numero / 2
    melhor_aproximacao = (chute_inicial + numero / chute_inicial) / 2

    while melhor_aproximacao != chute_inicial:
        chute_inicial = melhor_aproximacao
        melhor_aproximacao = (chute_inicial + numero / chute_inicial) / 2

    return melhor_aproximacao
x = raiz_quadrada(25)
print(x)  # Output: 5.0
