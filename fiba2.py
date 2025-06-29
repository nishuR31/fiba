def fib_series(n):
    x, y = 0, 1
    series = []
    for _ in range(n):
        series.append(x)
        x, y = y, x + y
    return series

num = int(input("\nHow many Fibonacci numbers? "))
print("Series:", fib_series(num))
