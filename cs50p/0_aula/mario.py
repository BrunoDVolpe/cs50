def main():
    print_square(3)


def print_square(size):

    #for each row in square
    for i in range(size):
        print("#" * size)

main()

"""
OU

def main():
    print_square(3)


def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#", end="")

        print()


main()

"""