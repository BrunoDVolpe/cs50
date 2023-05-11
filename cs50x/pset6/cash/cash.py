from cs50 import get_float

# getting change
while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

# calculating coins
change = change * 100
coins = int(change / 25)
coins += int(change % 25 / 10)
coins += int(change % 25 % 10 / 5)
coins += int(change % 25 % 10 % 5)
print(coins)