#Factorial de N (1 * 2 * 3 ... * n) CON RECURSIVIDAD NORMAL

def fact(x, result = 1):
    if x == 1:
        return result
    else:
        return fact(x-1, result * x)

print(fact(10))