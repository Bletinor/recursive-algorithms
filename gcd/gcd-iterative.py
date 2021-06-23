#Máximo común divisor (GCD Euclid's algorithm) CON ITERTIVIDAD

def gcd(x, y):
    while (x != 0 and y != 0):
        result = x%y
        x = y
        y = result
        
    if x == 0:
        return y
    elif y == 0:
        return x

print(gcd(0, 270))
