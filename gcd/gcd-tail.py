#Máximo común divisor (GCD Euclid's algorithm) CON TAIL RECURSION

def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return gcd(y, x%y)


print(gcd(14, 49))
