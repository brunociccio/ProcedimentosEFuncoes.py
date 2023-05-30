"""
7 - Sabemos que a função count() do Python retorna a quantidade de um elemento especifico na lista.
Chame uma função chama busca(lista, elemento)
"""
def preenche_lista(l: list) -> None:
    while True:
        x = input("Digite o elemento: ")
        if x != '.':
            l.append(x)
        else:
            break

def busca(l: list, e: str) -> int:
    qtd = 0
    for elem in l:
        if elem == e:
            qtd = qtd +1
    return qtd

lista = list()
preenche_lista(lista)
x = input("Elemento: ")
qtd = busca(lista, x)
if qtd > 1:
    print(f"Existem '{qtd}' elemento {x} na lista")
elif qtd == 1:
    print(f"Existe '{qtd}' elemento '{x}' na lista")
else:
    print(f"O elemento {x} não existe na lista")