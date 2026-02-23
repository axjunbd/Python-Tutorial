def generate_fibonacci(n_terms):
    """Generate Fibonacci sequence up to n_terms."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

if __name__ == "__main__":
    terms = 10
    fib_sequence = generate_fibonacci(terms)
    print(f"Fibonacci sequence up to {terms} terms:")
    print(fib_sequence)
