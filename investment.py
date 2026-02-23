def compound_interest(principal, rate, time):
    """
    Calculate compound interest.
    A = P(1 + R/100)^t
    """
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci, amount

if __name__ == "__main__":
    p = 1000  # Principal amount
    r = 5     # Annual interest rate in %
    t = 2     # Time in years
    
    interest, future_value = compound_interest(p, r, t)
    
    print(f"Principal Amount: ${p}")
    print(f"Annual Interest Rate: {r}%")
    print(f"Time (Years): {t}")
    print(f"Compound Interest: ${interest:.2f}")
    print(f"Total Future Value: ${future_value:.2f}")
