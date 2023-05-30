#Função
def prox_impar(n: int) -> int:
    if n % 2 == 1:
        n = n + 2
    else:
        n = n + 1
    return n
x = int(input("Digite um número: "))
x = prox_impar(x)