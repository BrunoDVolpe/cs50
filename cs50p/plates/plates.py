def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #"All vanity plates must start with at least two letters."
    if s[:2].isalpha() == False:
        return False

    #"… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters."
    if len(s) < 2 or len(s) > 6:
        return False

    #"Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
    # acceptable ...vanity plate; AAA22A would not be acceptable. The first number used cannot be a '0'."

    #check if all alphabetic
    if s.isalpha() == False:
        for char in s:
            if char.isnumeric():
                check = s[s.index(char):]
                break

        if check[0] == "0" or check.isnumeric() == False:
            return False

    #"No periods, spaces, or punctuation marks are allowed."
    if s.isalnum() == False:
        return False

    return True

main()