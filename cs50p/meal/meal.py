#Exercise: https://cs50.harvard.edu/python/2022/psets/1/meal/

def main():
    time = convert(input("What time is it? ").strip())

    print("breakfast time") if 7.0 <= time <= 8.0 else ""
    print("lunch time") if 12.0 <= time <= 13.0 else ""
    print("dinner time") if 18.0 <= time <= 19.0 else ""

def convert(time):
    hour, min = time.split(":")
    return float(int(hour) + int(min)/60)

if __name__ == "__main__":
    main()

"""
#Challenge - using time format 12h.

def main():
    time = convert(input("What time is it? ").strip())

    print("breakfast time") if 7.0 <= time <= 8.0 else ""
    print("lunch time") if 12.0 <= time <= 13.0 else ""
    print("dinner time") if 18.0 <= time <= 19.0 else ""

def convert(time):
    hour, part2 = time.split(":")
    min, ampm = part2.split(" ")

    if (ampm.lower() == "a.m." and hour != "12") or (ampm.lower() == "p.m." and hour == "12"):
        return float(int(hour) + int(min)/60)
    else:
        return float(int(hour) + 12 + int(min)/60)

if __name__ == "__main__":
    main()
"""