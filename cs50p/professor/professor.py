import random


def main():
    level = get_level()
    problems = 0
    score = 0
    tries = 0

    while problems < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        while tries < 3:
            print(f"{x} + {y} = ", end="")
            try:
                result = int(input())
                if result == x + y:
                    score += 1
                    problems += 1
                    tries = 0
                    break
                else:
                    raise ValueError
            except ValueError:
                tries += 1
                print("EEE")
                continue
        if tries == 3:
            print(f"{x} + {y} = {x + y}")
            tries = 0
            problems += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level == 1:
            return 1
        elif level == 2:
            return 2
        elif level == 3:
            return 3

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()