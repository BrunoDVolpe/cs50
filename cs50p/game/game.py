import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

rand_num = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess < 1:
        continue
    elif guess < rand_num:
        print("Too small!")
    elif guess > rand_num:
        print("Too large!")
    else:
        print("Just right!")
        break