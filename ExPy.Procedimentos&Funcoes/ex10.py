#Função
def prox_mult_5(n: int) -> int:
    return n // 5 * 5 + 5
num = int(input(f"Digite um número: "))
print(f"Próximo múltiplo de 5 é = {prox_mult_5(num)}")