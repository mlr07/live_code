import random


def start():
    print("Welcome to Math Wizard! Hit enter to continue...")
    input("> ")

    print("How many problems would you like to do?")
    problems = get_input()

    print(f"Get ready for {problems} problems...")

    return problems


def problem():
    op = random.choice(["+", "-", "*"])
    a, b = sorted([random.randint(0, 9) for r in range(2)], reverse=True)
    answer = None

    print(f"What is {a} {op} {b}?")

    if op == "+":
        answer = a + b

    elif op == "-":
        answer = a - b

    elif op == "*":
        answer = a * b

    response = get_input()

    check = response == answer
    point = None

    if check is True:
        print("Correct!")
        input("> ")
        point = 1

    elif check is False:
        print(f"Wrong! The answer is {answer}.")
        input("> ")
        point = 0

    return point


def game(problems):
    points = 0

    for r in range(problems):
        points += problem()

    print("All problems complete!")

    return points


def end(points, problems):

    score = points / problems

    print(f"{points} out of {problems} correct.")

    if score >= 0.75:
        print("Great score. Keep it up!")

    elif score < 0.75:
        print("OK score. Give it another try! ")


def get_input():
    while True:
        try:
            value = int(input("> "))
            break
        except ValueError:
            print("Invalid entry. Try again!")

    return value


def main():
    probs = start()
    points = game(probs)
    end(points, probs)


if __name__ == "__main__":
    main()
