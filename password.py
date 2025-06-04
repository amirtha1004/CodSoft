import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character sets selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no_input(prompt):
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ('y', 'n'):
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            return

        use_digits = get_yes_no_input("Include numbers?")
        use_symbols = get_yes_no_input("Include symbols?")

        password = generate_password(length, use_digits, use_symbols)
        print("\nGenerated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
