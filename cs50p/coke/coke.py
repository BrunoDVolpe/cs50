due = 50

while due > 0:
    print("Amount Due:", due)
    value = int(input("Insert Coin: "))
    if value == 25 or value == 10 or value == 5:
        due = due - value
print("Change Owed:", 0 - due)