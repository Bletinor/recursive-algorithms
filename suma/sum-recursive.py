#Sumatoria de los números del 1 a n : Sum(n) CON RECURSIVIDAD NORMAL

def Sum(n):
    if n == 1:
        return 1
    else:
        return (n + Sum(n - 1))

print(Sum(4))
