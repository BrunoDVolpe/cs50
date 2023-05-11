import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(0?\d|1[0-2])(:[0-5]\d)? (AM|PM) to (0?\d|1[0-2])(:[0-5]\d)? (AM|PM)",s, flags=0):
        hour_1 = int(matches.group(1))
        min_1 = matches.group(2)
        hour_2 = int(matches.group(4))
        min_2 = matches.group(5)
        if matches.group(3) == "PM":
            hour_1 = hour_1 + 12
            if hour_1 == 24:
                hour_1 = 12
        else:
            if hour_1 == 12:
                hour_1 = 00
        if min_1 == None:
            min_1 = ":00"
        if matches.group(6) == "PM":
            hour_2 = hour_2 + 12
            if hour_2 == 24:
                hour_2 = 12
        else:
            if hour_2 == 12:
                hour_2 = 00
        if min_2 == None:
            min_2 = ":00"
        return f"{hour_1:02}{min_1} to {hour_2:02}{min_2}"
    else:
        raise ValueError()



if __name__ == "__main__":
    main()