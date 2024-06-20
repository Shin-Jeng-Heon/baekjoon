n = int(input())

if n < 0 or n > 20:
    exit()
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)

print(fib(n))