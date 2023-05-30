"""
Fazer um procedimento que exiba os multiplos de 4 dentro de um intervalo (2 valores passados por parametro)
exibir_mult_4(5, 20)
8 12 16 20
"""
def exibir_mult_4(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 4 == 0:
            print(num, end=" ")

# Exemplo de uso
exibir_mult_4(5, 20)
