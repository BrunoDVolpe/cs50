from cs50 import get_int

# height between 1 and 8 inclusive
while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break

# printing piramid
for i in range(height):
    print(" " * (height - 1 - i), "#" * (i + 1), sep="")