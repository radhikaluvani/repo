import random
import string

def get_password(length):
    password = string.ascii_letters + string.digits + string.punctuation
    password1 = ''.join(random.choice(password) for i in range(length))
    print("Your random password is:", password1)

get_password(6)
