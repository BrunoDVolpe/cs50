from cs50 import get_int

# height in range 1 to 8, inclusive
while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break

# print pyramid
for i in range(height):
    print(" " * (height - 1 - i), "#" * (i + 1), "  ", "#" * (i + 1), sep="")