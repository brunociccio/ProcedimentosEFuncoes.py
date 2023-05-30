"""
Dados os digitos da placa de um carro, exibir (retornar) o dia da semana
de rodizio do veiculo
"""
def rodizio(placa: int) -> None:
    ultimo = placa % 10
    match ultimo:
        case 1 | 2:
            print("Segunda-feira")
        case 3 | 4:
            print("Terça-feira")
        case 5 | 6:
            print("Quarta-feira")
        case 7 | 8:
            print("Quinta-feira")
        case 9 | 0:
            print("Sexta-feira")
placa = int(input(f"Difite um número: "))
rodizio(placa)