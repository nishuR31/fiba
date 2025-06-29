def fib(n, memo={}):
    if n < 0:
        return "Negative not allowed"
    if n in memo:
        return memo[n]
    if n in [0, 1]:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

num = int(input("Enter number: "))
print(f"Fibonacci({num}) =", fib(num))
