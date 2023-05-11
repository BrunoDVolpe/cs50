import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(
        r"^(1?\d?\d|2[0-4]\d|25[0-5])\.(1?\d?\d|2[0-4]\d|25[0-5]).(1?\d?\d|2[0-4]\d|25[0-5]).(1?\d?\d|2[0-4]\d|25[0-5])$",
        ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()