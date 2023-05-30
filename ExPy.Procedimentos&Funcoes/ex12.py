#Procedimentos
def intervalo_fechado(inicio: int, fim: int) -> None:
    for i in range(inicio, fim + 1, 1):
        print(f"{i}", end="")
def intervalo_aberto(inicio: int, fim: int) -> None:
    for i in range(inicio + 1, fim, 1):
        print(f"{i}", end="")
def intervalo(inicio: int, fim: int, tipo: str) -> None:
    if tipo.upper() == 'A':
        intervalo_aberto(inicio, fim)
    else:
        intervalo_fechado(inicio, fim)
intervalo_fechado(3, 29)
print()
intervalo_aberto(3, 29)
print()
intervalo(3, 29, 'a')