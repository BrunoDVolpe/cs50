import csv
import re
import sys

def hide_emails(file_to_fix):
    new_file_name = "rd-leads.csv"

    if file_to_fix == new_file_name:
        exit("Arquivo não pode se chamar 'rd-leads.csv'")

    with open(file_to_fix) as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count == 0:
                count += 1
                with open(new_file_name, "w") as file_2:
                    writer = csv.writer(file_2)
                    writer.writerow(row)
            else:
                fixed_mails = re.sub(r'(?:\w*\.|\w*-)*\w+@', "hidden_email@", row[0])
                new_line = row
                new_line[0] = fixed_mails
                with open(new_file_name, "a") as file_2:
                    writer = csv.writer(file_2)
                    writer.writerow(new_line)

    return new_file_name

def main():
    hide_emails(sys.argv[1])


if __name__ == "__main__":
    main()