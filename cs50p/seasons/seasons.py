#pip install inflect
from datetime import date
import sys
import inflect


def main():
    print(f"{calculate(get_birth()).capitalize()} minutes")


def get_birth():
    birth_date = input("Date of birth: ")
    try:
        date.fromisoformat(birth_date)
    except ValueError:
        sys.exit("Invalid date")
    else:
        return birth_date


def calculate(date_to_convert):
    delta = date.today() - date.fromisoformat(date_to_convert)
    minutes = (delta.days) * 24 * 60
    p = inflect.engine()
    minutes = p.number_to_words(minutes, andword="")
    return minutes


if __name__ == "__main__":
    main()