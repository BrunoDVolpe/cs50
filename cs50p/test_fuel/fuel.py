def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x,sep,y = fraction.partition("/")
    if int(y) == 0:
        raise ZeroDivisionError
    if int(x) > int(y):
        raise ValueError
    return (int(x)/int(y))*100


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()
