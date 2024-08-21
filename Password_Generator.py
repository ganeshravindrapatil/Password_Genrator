import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        # Get user input for password length
        length = int(input("Enter the desired length for your password: "))

        # Check if the length is valid
        if length < 1:
            print("Password length should be at least 1.")
            return

        # Generate and display the password
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
