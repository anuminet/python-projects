import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    pool = string.ascii_lowercase

    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation

    password = "".join(random.choices(pool, k=length))
    return password

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("  Please enter y or n.")

def get_length():
    while True:
        try:
            length = int(input("How many characters long? (8-64): ").strip())
            if 8 <= length <= 64:
                return length
            else:
                print("  Please enter a number between 8 and 64.")
        except ValueError:
            print("  That wasn't a number. Try again.")

def main():
    print("=" * 40)
    print("       Password Generator")
    print("=" * 40)

    while True:
        length     = get_length()
        use_upper  = get_yes_no("Include uppercase letters? (y/n): ")
        use_digits = get_yes_no("Include numbers?          (y/n): ")
        use_symbols= get_yes_no("Include symbols?          (y/n): ")

        password = generate_password(length, use_upper, use_digits, use_symbols)

        print(f"\n  Your password: {password}\n")

        again = get_yes_no("Generate another? (y/n): ")
        if not again:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
