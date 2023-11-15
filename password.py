import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_random_passwords(num_passwords, length):
    passwords = [generate_random_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == '__main__':
    try:
        length = int(input("Enter the length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        passwords = generate_multiple_random_passwords(num_passwords, length)

        print(f"\nGenerated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"Password {idx}: {password}")
    except ValueError:
        print("Please enter valid integer values for length and number of passwords.")