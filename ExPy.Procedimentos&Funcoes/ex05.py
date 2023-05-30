"""
Fazer um procedimento chamado exibe_lista(l), que exiba os elementos da lista
passadas por parametro
"""

def preenche_lista(l: lista) -> None:
    while True:
        x = input("Digite o elemento")
        if x != '.':
            l.append(x)
        else:
            break

def exibe_lista(l: list) -> None:
    for i in range(len(l)):
        print(l[i])

  #  for elem in l:
   #     print(f"{elem} ", end="")

lista = list()
print(lista)
preenche_lista(lista)
print("Exibindo lista bruta ", lista)
exibe_lista(lista)
