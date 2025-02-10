##Crea un programa el cual imprima una lista con los primeros 15 números de la sucesión de Fibonacci.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


print(fibonacci(15))