import random

def add(lives, ques_completed):
    if lives == 0:
        print("Game over! You completed", ques_completed, "questions.")
        return
    else:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        asnwer = num_1 + num_2
        question = f"{num_1} + {num_2} = ?"
        user_answer = input(f"{question} ")
        if user_answer == str(asnwer):
            print("Correct!")
            ques_completed += 1
            random_controller(lives, ques_completed)
        else:
            print("Incorrect! The correct answer is:", asnwer)
            lives -= 1
            print(f"You have {lives} lives left.")
            random_controller(lives, ques_completed)

def subtract(lives, ques_completed):
    if lives == 0:
        print("Game over! You completed", ques_completed, "questions.")
        return
    else:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        asnwer = num_1 - num_2
        question = f"{num_1} - {num_2} = ?"
        user_answer = input(f"{question} ")
        if user_answer == str(asnwer):
            print("Correct!")
            ques_completed += 1
            random_controller(lives, ques_completed)
        else:
            print("Incorrect! The correct answer is:", asnwer)
            lives -= 1
            print(f"You have {lives} lives left.")
            random_controller(lives, ques_completed)

def multiply(lives, ques_completed):
    if lives == 0:
        print("Game over! You completed", ques_completed, "questions.")
        return
    else:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        asnwer = num_1 * num_2
        question = f"{num_1} * {num_2} = ?"
        user_answer = input(f"{question} ")
        if user_answer == str(asnwer):
            print("Correct!")
            ques_completed += 1
            random_controller(lives, ques_completed)
        else:
            print("Incorrect! The correct answer is:", asnwer)
            lives -= 1
            print(f"You have {lives} lives left.")
            random_controller(lives, ques_completed)

def divide(lives, ques_completed):
    if lives == 0:
        print("Game over! You completed", ques_completed, "questions.")
        return
    else:
        num_1 = random.randint(1,10)
        num_2 = random.randint(1,10)
        asnwer = num_1 / num_2
        asnwer = round(asnwer, 2)
        print("Round to 2 decimal places")
        question = f"{num_1} / {num_2} = ?"
        user_answer = input(f"{question} ")
        if user_answer == str(asnwer):
            print("Correct!")
            ques_completed += 1
            random_controller(lives, ques_completed)
        else:
            print("Incorrect! The correct answer is:", asnwer)
            lives -= 1
            print(f"You have {lives} lives left.")
            random_controller(lives, ques_completed)
        

def random_controller(lives, ques_completed):
    operator = random.randint(1,4)
    if operator == 1:
        add(lives, ques_completed)
    elif operator == 2:
        subtract(lives, ques_completed)
    elif operator == 3:
        multiply(lives, ques_completed)
    elif operator == 4:
        divide(lives, ques_completed)

def main(lives, ques_completed):

    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    operator = random.choice(["+", "-", "*", "/"])

    print("-" * 60)
    print("Welcome to the math game")
    print("You get 3 lives to answer as many math questions as possible")
    a = input("Ready to start? (y/n): ")
    if a.lower() == "y":
        random_controller(lives, ques_completed)
        
    else:
        print("Goodbye!")
        return



if __name__ == "__main__":
    main(3,0)