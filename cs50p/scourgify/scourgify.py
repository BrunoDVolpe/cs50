import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

students = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        house = row["house"]
        last, first = row["name"].split(", ")
        students.append({"first":first, "last":last, "house":house})

with open(sys.argv[2], "w") as new:
            writer = csv.DictWriter(new, fieldnames=["first","last","house"])
            writer.writeheader()
            for dict in students:
                writer.writerow(dict)