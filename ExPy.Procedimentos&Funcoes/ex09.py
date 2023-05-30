"""
Subalgoritmos
Conceito - Pequenos trechos de código que podem ser executados em outros programas
Procedimento:
Trecho de código que só é executado dentro dele.
Função:
Idem ao procedimento, mas retorna um valor ao programa principal.
"""

#Construção dos Procedimentos:
def intervalo_fechado(inicio: int, fim: int) -> None:
    for i in range(inicio, fim + 1, 1):
        print(f"{i}", end="")
def intervalo_aberto(inicio: int, fim: int) -> None:
    for i in range(inicio + 1, fim, 1):
        print(f"{i}", end="")
def intervalo(inicio: int, fim: int, tipo: str) -> None:
    if tipo.upper() == 'A':
        intervalo_aberto(inicio, fim)
    else:
        intervalo_fechado(inicio, fim)

#Construção das funções:
def prox_numero(n: int) -> int:
    return n + 1

def prox_impar(n: int) -> int:
    if n % 2 == 1:
        n = n + 2
    else:
        n = n + 1
    return n

#Programa Principal:
x = int(input("Digite um número: "))
x = prox_numero(x)
print(x)
intervalo_fechado(3, 29)
print()
intervalo_aberto(3, 29)
print()
intervalo(3, 29, 'a')