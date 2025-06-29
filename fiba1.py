
def fib(n):
    if n < 0:
        return "Negative not allowed"
    x, y = 0, 1
    for _ in range(n):
        print(x)
        x, y = y, x + y
    return x

num = int(input("\nEnter number: "))
print(f"Fibonacci({num}) =", fib(num))
