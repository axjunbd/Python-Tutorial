import math

def calculate_square_root(num):
    """Calculate the square root of a number."""
    if num < 0:
        return None  # Square root is complex for negative numbers
    
    # Method 1: Using math.sqrt()
    sqrt_math = math.sqrt(num)
    
    # Method 2: Using exponentiation
    sqrt_exp = num ** 0.5
    
    return sqrt_math, sqrt_exp

if __name__ == "__main__":
    number = 144
    results = calculate_square_root(number)
    
    if results is not None:
        math_res, exp_res = results
        print(f"The square root of {number} is:")
        print(f"  Using math.sqrt(): {math_res}")
        print(f"  Using exponentiation (num ** 0.5): {exp_res}")
    else:
        print(f"Cannot calculate real square root for {number}. It is a negative number.")
