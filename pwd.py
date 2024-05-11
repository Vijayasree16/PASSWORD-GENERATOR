import random
import string

def generate_password(length):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random.choice()
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    
    # Generate password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
