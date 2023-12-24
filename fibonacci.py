# python3 fibonacci.py

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
        
    if n in [1, 2]:
        result = 1
    else:
        result = fibonacci(n - 2) + fibonacci(n - 1)

    memo[n] = result

    return result

for i in range(1, 10):
    print(fibonacci(i))
