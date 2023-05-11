def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    plate = plate.upper()
    if plate[:2].isalpha() == False:
        return False
    if len(plate) < 2 or len(plate) > 6:
        return False
    if plate.isalnum() == False:
        return False
    for char in plate:
        if char.isdigit():
            if char == "0":
                return False
            if plate.partition(char)[-1] == "":
                return True
            if plate.partition(char)[-1].isdigit() == False:
                return False
            return True
    return True


if __name__ == "__main__":
    main()