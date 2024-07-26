import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list of characters to a string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    
    # Get password length from user
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 8 characters): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate and display the password
    password = generate_password(length)
    print("\nYour generated password is:")
    print(password)
    print("\nMake sure to store this password securely and not share it with others.")

if __name__ == "__main__":
    main()
