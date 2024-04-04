def generate_fibonacci_up_to_number(limit):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= limit:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)

    return fib_sequence


limit = int(input("Enter the upper limit for the Fibonacci series: "))

fibonacci_series = generate_fibonacci_up_to_number(limit)


print(f"The Fibonacci series up to {limit} is:")
print(fibonacci_series)
