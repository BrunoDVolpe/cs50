from sys import argv
import sys
import csv


def main():
    if len(argv) != 3:
        print("Usage: dna.py data.csv sequence.txt")
        sys.exit()

    database, sequence = load_info()

    str_list = []
    for str_seq in database[0]:
        if str_seq != 'name':
            str_list.append(str(repetition_count(str_seq, sequence)))

    name = match_individual(str_list, database)
    if name != None:
        print(name)
    else:
        print("No match")


# Loading info
def load_info():
    # Loading Database
    database = []
    with open(argv[1], 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # [['name', 'AGATC', 'AATG', 'TATC'], ['Alice', '2', '8', '3'], ...]
            database.append(row)

    # Loading Individual
    with open(argv[2], 'r') as file:
        # str
        sequence = file.read()

    return database, sequence


# Calcula a maior repetição
def repetition_count(STR, sequence):
    count = 0
    controle = 0
    maior = 0
    i = 0

    while i < (len(sequence) - len(STR) + 1):
        # Encontre uma sequência
        if STR in sequence[i:i + len(STR)] and controle == 0:
            count += 1
            controle = 1
            i += len(STR)

        # Continue contando numa sequência
        elif STR in sequence[i:i + len(STR)] and controle == 1:
            count += 1
            i += len(STR)

        # Não encontrou padrão
        else:
            if maior < count:
                maior = count
            controle = 0
            count = 0
            i += 1

    return maior


# Procura o match
def match_individual(lista, base):
    for row in base:
        if lista == row[1:]:
            return row[0]
    return None


if __name__ == "__main__":
    main()