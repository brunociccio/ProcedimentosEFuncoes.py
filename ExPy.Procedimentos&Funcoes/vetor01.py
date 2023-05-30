v = [23, 65, 34, 98, 12, 75, 4, 8] #dados homogeneos
# procedimento exibe elementos do vetor
def exibe_vetor(vet: list) -> None:
    for i in range(0, len(vet), 1):
        print(f"v[{i}] = {vet[i]}")
# procedimento exibe numeros pares do vetor
def exibe_elementos_pares(vet: list) -> None:
    for i in range(0, len(vet), 1):
        if v[i] % 2 == 0:
            print(f"v[{i}] = {vet[i]} | ", end="")
# função que retorno ultimo elemento do vetor
def ultimo_elemento(vet: list) -> int:
    return vet[len(vet) - 1]
# função que soma os elementos do vetor
def soma_vetor(vet: list) -> int:
    soma = 0
    for i in range(0, len(vet), 1):
        soma = soma + vet[i]
    return soma

exibe_vetor(v)
exibe_elementos_pares(v)
ultimo = ultimo_elemento(v)
print(f"\n{ultimo}")
print(f"Somatoria = {soma_vetor(v)}")
"""
print(v) #quando colocamos somente o nome da var exibe o vetor na integra
print(v[0]) #quando colocamos colchetes exibi uma posição especifica
"""
