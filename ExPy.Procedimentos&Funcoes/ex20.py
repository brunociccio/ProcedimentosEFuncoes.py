"""
5. Fazer uma função que passe 3 parâmetros e calcule x1 da equacao de baskara
x1 = x1_baskara(-1, 2, 3)
>> x1 valerá -1
"""
def x1_baskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1
    else:
        return None
x1 = x1_baskara(-1, 2, 3)
print(x1)
