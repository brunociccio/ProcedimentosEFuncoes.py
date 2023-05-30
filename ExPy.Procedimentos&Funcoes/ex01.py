def exibe_negativos(vet: list) -> None:
    for i in range(len(vet)):
        if vet[i] < 0:
            print(f"{vet[i]}", end="")
v = [45, -89, 32, -12, 33]
print("Ex 1 - Vetor: ")
exibe_negativos(v)