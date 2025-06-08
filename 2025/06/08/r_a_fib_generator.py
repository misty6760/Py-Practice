def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 피보나치 수열에서 첫 10개 항 출력
fibonacci_gen = fib()
for _ in range(10):
    print(next(fibonacci_gen), end=" ")