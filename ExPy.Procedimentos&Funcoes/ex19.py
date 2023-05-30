"""
6. Fazer uma função que passe 3 parâmetros e calcule x2 da equacao de baskara
x2 = x2_baskara(-1, 2, 3)
>> x2 valerá 3
"""
def x2_baskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x2
    else:
        return None
x2 = x2_baskara(-1, 2, 3)
print(x2)  
