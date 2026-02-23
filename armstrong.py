def is_armstrong(num):
    if num < 0:
        return False
        
    num_str = str(num)
    num_len = len(num_str)
    
    total = sum(int(digit) ** num_len for digit in num_str)
    
    return num == total

if __name__ == "__main__":
    # Check a specific number
    number_to_check = 153
    if is_armstrong(number_to_check):
        print(f"{number_to_check} is an Armstrong number.")
    else:
        print(f"{number_to_check} is not an Armstrong number.")

    # Find all Armstrong numbers within a specific range
    print("\nArmstrong numbers between 1 and 1000:")
    for num in range(1, 1001):
        if is_armstrong(num):
            print(num)
