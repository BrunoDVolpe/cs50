from cs50 import get_int

number = get_int("Number: ")

# quantity of numbers 13, 15 or 16 numbers
if len(str(number)) in [13, 15, 16]:
    # Luhn's algorythm
    soma = 0
    for i in range(2, len(str(number)) + 1, 2):
        digit = (number % 10**i // 10**(i - 1)) * 2
        if digit > 9:
            soma += digit//10
            soma += digit % 10
        else:
            soma += digit

    for i in range(1, len(str(number)) + 1, 2):
        soma += number % 10**i // 10**(i - 1)

    if soma % 10 != 0:
        print("INVALID")

else:
    print("INVALID")

# AMEX, MASTERCARD, VISA or INVALID?
if len(str(number)) == 15 and (number//10**13 == 34 or number//10**13 == 37):
    print("AMEX")

elif len(str(number)) == 16 and (number//10**14 in [51, 52, 53, 54, 55]):
    print("MASTERCARD")

elif len(str(number)) in [13, 16] and (number//10**(len(str(number)) - 1) == 4):
    print("VISA")

else:
    print("INVALID")