def encrypt(text, shift):
    """
    Encrypts a text using Caesar Cipher.
    """
    result = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep spaces and punctuation unchanged
        else:
            result += char
    return result


def decrypt(text, shift):
    """
    Decrypts a text using Caesar Cipher.
    """
    # Decryption is just encryption with a negative shift
    return encrypt(text, -shift)


if __name__ == "__main__":
    original_text = "Hello, World!"
    shift_amount = 4

    print(f"Original Text: {original_text}")
    print(f"Shift Amount: {shift_amount}")

    encrypted_text = encrypt(original_text, shift_amount)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, shift_amount)
    print(f"Decrypted Text: {decrypted_text}")
