def perform_string_operations(text):
    """Demonstrate various string operations."""
    print(f"Original Text: '{text}'\n")
    
    # 1. Length
    print(f"Length of the string: {len(text)}")
    
    # 2. Uppercase and Lowercase
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    
    # 3. Capitalize and Title
    print(f"Capitalize (first letter only): {text.capitalize()}")
    print(f"Title (first letter of each word): {text.title()}")
    
    # 4. Counting Occurrences
    search_char = 'o'
    print(f"Count of '{search_char}': {text.count(search_char)}")
    
    # 5. Finding Substrings
    search_sub = "World"
    pos = text.find(search_sub)
    if pos != -1:
         print(f"Found '{search_sub}' at index: {pos}")
    else:
         print(f"'{search_sub}' not found.")
         
    # 6. Replace
    new_text = text.replace("World", "Python")
    print(f"Replace 'World' with 'Python': {new_text}")
    
    # 7. Split
    words = text.split(", ")
    print(f"Split by ', ': {words}")

if __name__ == "__main__":
    sample_text = "Hello, World of Programming!"
    perform_string_operations(sample_text)
