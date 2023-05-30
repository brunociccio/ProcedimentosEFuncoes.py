"""
Fazer um procedimento que passe os numeros do intervalo por parametro e a ordem:
'd' para decrescente e 'c' para crescente, exibindo os numeros
intervalo_ordem(6, 17, 'd')
17 16 15 14 13 12 11 10 9 8 7 6
intervalo_ordem(6, 17 , 'c')
6 7 8 9 10 11 12 13 14 15 16 17
"""
def intervalo_ordem(inicio, fim, ordem):
    if ordem == 'c':
        for num in range(inicio, fim + 1):
            print(num, end=" ")
    elif ordem == 'd':
        for num in range(fim, inicio - 1, -1):
            print(num, end=" ")
    else:
        print("Ordem inválida! Use 'c' para crescente ou 'd' para decrescente.")

# Exemplos de uso
intervalo_ordem(6, 17, 'd')
print()
intervalo_ordem(6, 17, 'c')
