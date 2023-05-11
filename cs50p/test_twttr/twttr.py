#Refazendo exercício do Problem Set 2 com uma reestruturação do código.

def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    shrt = ""
    for letter in word:
        if letter in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue
        else:
            shrt = shrt + letter
    return shrt


if __name__ == "__main__":
    main()