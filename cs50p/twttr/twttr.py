text = input("Input: ")

print("Output: ", end="")
for char in text:
    match char:
        case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
            None
        case _:
            print(char, end="")

print()