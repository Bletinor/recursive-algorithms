#Máximo común divisor (GCD Euclid's algorithm) CON RECURSIVIDAD NORMAL

def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        resultado = gcd(y, x%y)
        return resultado

print(gcd(270, 192))
