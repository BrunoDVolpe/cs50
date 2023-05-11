answer = input("What's the answer? ").lower().strip()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

"""
if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")
    """