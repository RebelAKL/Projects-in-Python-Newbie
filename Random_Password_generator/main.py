import secrets
import string

def random_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(punctuation)
    ]

    all_characters = lowercase + uppercase + digits + punctuation
    password += [secrets.choice(all_characters) for _ in range(length - 4)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)

try:
    print(random_password(12))  
except ValueError as e:
    print(e)
