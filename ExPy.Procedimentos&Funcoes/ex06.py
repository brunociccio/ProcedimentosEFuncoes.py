"""
Sabemos que a função index() do Python  retorna o indicie do elemento passado
por parametro. Faça uma função parecida chamada retorna_indice(elemento)
"""
def preenche_lista(l: list) -> None:
    while True:
        x = input("Digite o elemento: ")
        if x != '.':
            l.append(x)
        else:
            break

def retorna_indice(l: list, e: str) -> int:
    for i in range(len(l)):
        if l[i] == e:
            return i
        return -1

lista = list()
preenche_lista(lista)

x = input("Elemento: ")
indice = retorna_indice(lista, x)
if indice == -1:
    print(f"O elemento {x} não existe na lista! :(")
else:
    print(f"O elemento {x} existe na lista, na posição {indice}! :)")
