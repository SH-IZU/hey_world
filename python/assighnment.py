def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Print the first 20 Fibonacci numbers
fibonacci_sequence = fibonacci(20)
for num in fibonacci_sequence:
    print(num)