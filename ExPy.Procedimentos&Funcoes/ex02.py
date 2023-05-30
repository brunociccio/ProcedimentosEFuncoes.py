def soma_elementos (vet: list) -> int:
    soma = 0
    for i in range(len(vet)):
        soma = soma + v[i]
    return soma

print("Ex 2 - Vetor: ")
print(f"Somatória = {soma_elementos(v)}")
