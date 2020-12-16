import random


def start():
    print("-"*40)
    print("Welcome to Math Wizard!")
    print("How many problems do you want to do?")

    while True:
        try:
            problems = int(input("> "))
            break
        except ValueError:
            print("Entry is not valid. Try again.")

    print(f"Get ready for {problems} problems...")
    input("> ")

    return problems


def problem():
    # TODO: handle ZeroDivisionError
    # TODO: add montessori style problems
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = a + b

    elif op == "-":
        answer = a - b

    elif op == "*":
        answer = a * b

    print(f"What is {a} {op} {b}?")

    while True:
        try:
            response = int(input("> "))
            break
        except ValueError:
            print("Entry is not valid. Try again.")

    check = response == answer
    point = None

    if check is True:
        print("Correct!")
        input("> ")
        point = 1

    elif check is False:
        print(f"Incorrect! The answer is {answer}")
        input("> ")
        point = 0

    return point


def game(problems):
    score = 0
    for r in range(0, problems):
        score += problem()

    # TODO: make better score
    print("-"*40)
    print(f"Score: {score} out of {problems}. Good job math wizard!")


def end():
    print("Would you like to try again? (y or n)")

    # TODO: handle string entry
    return input("> ").lower()


def main():
    while True:
        problems = start()

        game(problems)

        choice = end()

        if choice == "y":
            print("ZAP! Start again!")

        elif choice == "n":
            print("ZORK! Good bye!")
            break


if __name__ == "__main__":
    main()
