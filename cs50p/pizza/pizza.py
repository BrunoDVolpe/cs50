#pip install tabulate
from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        pass
except FileNotFoundError:
    sys.exit("File does not exist")

table = []
with open(sys.argv[1]) as file:
    for row in file:
        table.append(row.rstrip().split(","))

print(tabulate(table, headers="firstrow", tablefmt="grid"))