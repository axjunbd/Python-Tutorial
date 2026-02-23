def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

if __name__ == "__main__":
    num = 5
    result = factorial(num)
    if result is not None:
        print(f"The factorial of {num} is {result}")
    else:
        print("Factorial does not exist for negative numbers")
