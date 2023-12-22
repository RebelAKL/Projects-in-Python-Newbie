import random
import string

def random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice