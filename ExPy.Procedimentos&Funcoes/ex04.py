"""
4 - Fazer um procedimento chamado "preencher_lista(l)", que preenche uma lista passada
por parametro. Preenche lista(lista). Para terminar digite ".".
"""
def preenche_lista(l: lista) -> None:
    while True:
        x = input("Digite o elemento")
        if x != '.':
            l.append(x)
        else:
            break

lista = list()
print(lista)
preenche_lista(lista)