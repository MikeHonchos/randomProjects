#Password Generator
import random

#All characters that can be used in the password
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

def generate():
    input_length = int(input("Enter the length of password: "))
    password = []
    for i in range(input_length):
        password.append(random.choice(characters))
    print("".join(password))


if __name__ == "__main__":
    generate()