import csv

#from cs50 import get_string

file = open("phonebook.csv", "a")

#name = get_string("Name: ")
#number = get_string("Number: ")
name = input("Name: ")
number = input("Number: ")

writer = csv.writer(file)

writer.writerow([name, number])

file.close()

"""
OU desta forma:
with open("phonebook.csv", "a") as file:

    name = input("Name: ")
    number = input("Number: ")

    writer = csv.writer(file)

    writer.writerow([name, number])
"""