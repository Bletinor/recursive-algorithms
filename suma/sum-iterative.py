#Sumatoria de los números del 1 a n : Sum(n) CON ITERATIVIDAD

def Sum(n):
    result = 0
    i = 1

    while i != n + 1:
        result = result + i
        i += 1
    return result

print(Sum(7))
