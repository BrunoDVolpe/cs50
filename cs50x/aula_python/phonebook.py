from cs50 import get_string

people = {
    "Brian": "+1-617-495-1000",
    "David": "+1-949-468-2750"
}

print("caraca!")

name = get_string("Name: ")
#name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")