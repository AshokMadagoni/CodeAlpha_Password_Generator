import random

def generate_password(length=12):
    # Define character sets for password generation
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"

    # Ensure the password length is at least 8 characters
    if length < 8:
        length = 8

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
