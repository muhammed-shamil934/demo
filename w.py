def count():
    b=("a,b,c,d,")
    a=("a,e,i,o,u")
    c.sort(a,b)
    print(c)
count()

def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def print_fibonacci(n):
    fib_sequence = generate_fibonacci(n)
    for i, num in enumerate(fib_sequence):
        print(f"Fibonacci({i}) = {num}")

    
