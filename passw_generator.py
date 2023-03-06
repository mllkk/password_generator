import random

lowercase_letters="abcdefghijklmnopqrstuvwxyz"
uppercase_letters=lowercase_letters.upper()
symbols="#+$*-/!?()%&"
digits="0123456789"

while True:
    try:
        password_len = int(input("password length:"))
        if 7 < password_len < 15:
            break
        else:
            print("enter an integer number greater than 7 and smaller than 15")
    except ValueError:
        continue

def generate_password(password_len):
    password = ""
    for i in range(2):
        password += random.choice(digits)
    for i in range(2):
        password += random.choice(symbols)
    for i in range(2):
        password += random.choice(uppercase_letters)
    for i in range(password_len-6):
        password += random.choice(lowercase_letters)

    fpassword = list(password)
    random.shuffle(fpassword)
    return "".join(fpassword)

x = generate_password(password_len)
print(f"new password: {x}")