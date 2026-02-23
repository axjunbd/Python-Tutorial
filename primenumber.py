import math

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    max_divisor = math.isqrt(n)
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
            
    return True

if __name__ == "__main__":
    number = 29
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

    print("\nPrime numbers between 1 and 50:")
    primes = [i for i in range(1, 51) if is_prime(i)]
    print(primes)
