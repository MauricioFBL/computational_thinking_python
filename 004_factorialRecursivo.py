
def factorial(n):
    """Calucla el factorial de n
    n int>0,return n!
    """
    print(n)
    if n == 1:
        return 1
    return n * factorial(n -1)

n = int(input('Digite un numero entero: '))

print(factorial(n))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def memo_fibonacci(n, memo=None):
    if memo == None:
        memo = [0, 1, 1, 2]
    
    for i in range(n+1):
        if i > len(memo)-1:
            memo.append(memo[i-1] + memo[i-2])
        else:
            continue

    return memo