def binary_to_decimal(binary_str):
    """Converts a binary string to a decimal integer using Python's built-in int() function."""
    try:
        # The int() function takes a base as the second argument
        return int(binary_str, 2)
    except ValueError:
        return None

def binary_to_decimal_manual(binary_str):
    """Converts a binary string to a decimal integer using manual calculation."""
    decimal_value = 0
    # Reverse string to start from Least Significant Bit (LSB)
    for i, digit in enumerate(reversed(binary_str)):
        if digit == '1':
            decimal_value += 2 ** i
        elif digit != '0':
            return None # Invalid character
    return decimal_value

if __name__ == "__main__":
    test_binary = "10110"
    
    print(f"Binary Number: {test_binary}")
    
    # Method 1: Built-in int()
    result_builtin = binary_to_decimal(test_binary)
    if result_builtin is not None:
        print(f"Decimal (Built-in Method): {result_builtin}")
    else:
        print("Invalid binary input.")
        
    # Method 2: Manual Calculation
    result_manual = binary_to_decimal_manual(test_binary)
    if result_manual is not None:
        print(f"Decimal (Manual Method): {result_manual}")
    else:
        print("Invalid binary input.")
