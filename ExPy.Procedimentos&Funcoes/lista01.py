#lista dados heterogeneos
#criando uma lista vazia
lista1 = ("Fiap", 45, True, 98.7, False, "CTP")
lista2 = [54, 23, 56, 83, 12, 67]

#del - desaloca a variavel da memoria
"""print(lista1)
del(lista1)
print(lista1)
"""

#clear - limpa os elementos da lista
"""print(lista1)
lista1.clear()
print(lista1)
"""

#reverse - inverte o nome da lista
"""print(lista1)
lista1.reverse()
print(lista1)
"""

#sort - ordena a lista em ordem crescente ou decrescente
"""print(lista2)
lista2.sort()
print(lista2)
"""

#copy - cria uma copia da lista
"""lista2.copy(lista1)
print(lista1)
print(lista2)
"""

# cuidado ao usar o igual para listas!!
"""print(lista1)
print(lista2)

lista2 = lista1

print(lista1)
print(lista2)
lista1[0] = "mudou"
print(lista1)
print(lista2)
lista2[3] = 111111
print(lista1)
print(lista2)
"""

#extended - adiciona uma lista no final da outra
"""print(lista1)
print(lista2)
lista1.extend(lista2)
print(lista1)
print(lista2)
"""

# + - concatena listas
"""print(lista1 + lista2)
lista3 = lista1 + lista2
print(lista3)
"""

#sum - soma os elementos numéricos da lista, se houver algum dados não numérico = erro
"""
print(sum(lista))
"""

#len - conta a quantidade de elementos em um estrutura

#insert - inserir o elemento em alguma posição
"""
print(lista)
lista.insert(2, "meio")
print(lista)
"""

#pop - remove um elemento da lista
"""print(lista)
lista.pop(2)
print(lista)"""

#remove - remove um elemento especifico
"""print(lista)
lista.remove(98.7)
print(lista)"""

#append - adiciona um item na lista
"""print(lista)
lista.append("Novo")
print(lista)"""

#index - retorna o inidice do elemento a partir do conteudo fornecido por parametro
"""print(lista)
x = lista.index(98.7)
print(x)"""

#count - retorna a incidencia de um elemento no vetor
"""
elem = 45
x = lista.count(elem)
print(f"A lista tem {x} elementos {elem}")
"""





