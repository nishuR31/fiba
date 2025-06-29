from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 0:
        return "Negative not allowed"
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

num = int(input("Enter number: "))
print(f"Fibonacci({num}) =", fib(num))
