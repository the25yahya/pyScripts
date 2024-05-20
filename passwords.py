import random
import string


def generate_password(length, criteria):
    characters = ""
    for criterion in criteria:
        if criterion == "uppercase":
            characters += string.ascii_uppercase
        elif criterion == "lowercase":
            characters += string.ascii_lowercase
        elif criterion == "digits":
            characters += string.digits
        elif criterion == "special_chars":
            characters += string.punctuation



    if not characters:
       raise ValueError("At least one character is required")

    password = ''.join(random.choice(characters) for _ in range(length))
    print("Your password is : ",password)
    return password

def main():
    length = int(input("Enter the length of password: "))
    criteria = []

    uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    if uppercase:
        criteria.append('uppercase')

    lowercase = input("include lowercase letters ? (y/n): ").lower() == "y"
    if lowercase:
        criteria.append('lowercase')

    digits = input("include digits ? (y/n): ").lower() == "y"
    if digits:
        criteria.append('digits')

    special_chars = input("include special characters ? (y/n): ").lower() == "y"
    if special_chars:
        criteria.append('special_chars')
    generate_password(length, criteria)

main()