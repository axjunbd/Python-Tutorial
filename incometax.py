def calculate_tax(income):
    """
    Calculate income tax based on simple brackets:
    - 0 to 10000: 0%
    - 10001 to 50000: 10%
    - 50001 and above: 20%
    """
    tax = 0
    if income <= 10000:
        tax = 0
    elif income <= 50000:
        tax = (income - 10000) * 0.10
    else:
        tax = (40000 * 0.10) + ((income - 50000) * 0.20)
    return tax

if __name__ == "__main__":
    income_amount = 60000
    tax_amount = calculate_tax(income_amount)
    print(f"Income: ${income_amount}")
    print(f"Calculated Tax: ${tax_amount}")
