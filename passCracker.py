#Password cracker
#This program will try and brute force a password and will time it to see how good your password is
from time import time
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"

def Passcracker():
    password = input("Enter the password to crack: ")
    start_time = time()
    attempts = 0
    cracked = False

    while not cracked:
        guess = ""
        for i in range(len(password)):
            guess += random.choice(characters)
        attempts += 1
        print(f"Attempt {attempts}: {guess}")
        if guess == password:
            cracked = True
            end_time = time()
            print(f"Password cracked: {guess}")
            print(f"Attempts: {attempts}")
            print(f"Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    Passcracker()
