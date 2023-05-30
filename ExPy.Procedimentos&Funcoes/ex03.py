def soma_elementos (vet: list) -> int:
    soma = 0
    for i in range(len(vet)):
        soma = soma + v[i]
    return soma

def media_elementos(vet: list) -> float:
    return soma_elementos(vet) / len(vet)

print("Ex 3 - Vetor")
print(f"Média = {media_elementos(v)}")