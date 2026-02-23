def is_palindrome(text):
    """Check if a string or number is a palindrome."""
    # Convert to string and to lowercase for case-insensitive comparison
    # Remove any spaces
    cleaned_text = str(text).replace(" ", "").lower()
    
    # Check if the text reads the same forwards and backwards
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    test_cases = [
        "radar",
        "hello",
        "A man a plan a canal Panama",
        12321,
        12345
    ]
    
    for case in test_cases:
        if is_palindrome(case):
            print(f"'{case}' is a palindrome.")
        else:
            print(f"'{case}' is not a palindrome.")
