#Sumatoria de los números del 1 a n : Sum(n) CON TAIL-RECURSION

def Sum(n, acumulador = 1):
    if n == 1:
        return acumulador
    else:
        return Sum(n - 1, acumulador + n)

print(Sum(10))