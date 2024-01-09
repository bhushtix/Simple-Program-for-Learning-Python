import re
import secrets
import string


# Function to generate a password with specified constraints
def generate_password():
    # Ask the user for the desired length
    length = int(input("Enter the desired password length: "))

    # Define the possible characters for the password
    letters = string.ascii_letters  # All alphabetical characters
    digits = string.digits  # All numeric digits
    symbols = string.punctuation  # All special characters

    # Combine all characters
    all_characters = letters + digits + symbols

    # Loop until a valid password is generated
    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)  # Choose a random character from all_characters

        # Constraints to be satisfied by the password
        constraints = [
            (1, r'\d'),  # Require at least 1 numeric character
            (1, fr'[{symbols}]'),  # Require at least 1 special character
            (1, r'[A-Z]'),  # Require at least 1 uppercase letter
            (1, r'[a-z]')  # Require at least 1 lowercase letter
        ]

        # Check if the generated password satisfies all constraints
        if all(
                constraint <= len(re.findall(pattern, password))
                for constraint, pattern in constraints
        ):
            break  # Exit the loop if the password meets all constraints

    return password


# Check if the script is run as the main program
if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
