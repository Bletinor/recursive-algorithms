#Factorial de N (1 * 2 * 3 ... * n) CON RECURSIVIDAD NORMAL

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n - 1))

print(fact(10))