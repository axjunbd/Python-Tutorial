def reverse_string_slicing(text):
    return text[::-1]

def reverse_string_loop(text):
    """Reverse a string using a loop."""
    reversed_str = ""
    for char in text:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_join(text):
    """Reverse a string using reversed() and join()."""
    return "".join(reversed(text))

if __name__ == "__main__":
    original = "Hello Python"
    
    print(f"Original string: '{original}'")
    print("-" * 30)
    
    # Method 1
    rev1 = reverse_string_slicing(original)
    print(f"Reversed (Slicing): '{rev1}'")
    
    # Method 2
    rev2 = reverse_string_loop(original)
    print(f"Reversed (Loop):    '{rev2}'")
    
    # Method 3
    rev3 = reverse_string_join(original)
    print(f"Reversed (Join):    '{rev3}'")
