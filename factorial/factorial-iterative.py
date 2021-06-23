#Factorial de N(1 * 2 * 3 ... * n) CON RECURSIVIDAD NORMAL

def fact(x):
    result = 1
    i = 1
    while i != x+1:
        result = result * i
        i += 1
    return result

#1 * 5 *  

print(fact(10))