import random

def get_pass():
    letters_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    for i in range(7):
        password += random.choice(letters_numbers)
    return password

print(get_pass())
