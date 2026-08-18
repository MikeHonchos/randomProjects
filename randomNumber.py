import random


def numbers():
    x = random.randint(1,10)

    ans = int(input("Please pick a number between 1-10: "))
    while ans > 10 or ans < 1:
        ans = int(input("Please pick a number between 1-10: "))
    if ans == x:
        print("You Win!")
        return
    else:
        print("Try Again")
        main()


def main():
    numbers()



if __name__ == "__main__":
    main()