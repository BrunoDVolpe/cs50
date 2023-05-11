#Antes de enviar, mudar 'rd-leads.csv' para 'rd-leads-2911.csv' para enviar os leads com email já oculto.
import csv, sys, re
from tabulate import tabulate, SEPARATING_LINE
from hide_emails import hide_emails


def main():
    necessaryColumns = ['Tags', 'Estágio no funil', 'Data da última conversão', 'Email', 'Origem da última conversão']
    valid_months = validate_month()
    info(load_leads(validate_file(sys.argv, necessaryColumns), valid_months))


def validate_month():
    try:
        sys.argv[2]
    except IndexError:
        return []
    else:
        return sys.argv[2]


def validate_file(sys_arguments, necessaryColumns):
    if len(sys_arguments) > 3:
        sys.exit("Too many arguments, expected one RD Station '.csv' file and, optionally, list of months")
    elif len(sys_arguments) < 2:
        sys.exit("Too few arguments, expected one RD Station '.csv' file and, optionally, list of months")
    elif sys_arguments[1].endswith(".csv") == False:
        sys.exit("Not a '.csv' file")

    try:
        with open(sys_arguments[1]) as file:
            pass
    except FileNotFoundError:
        sys.exit(f"Could not find {sys_arguments[1]} in this folder")
    else:
        with open(sys_arguments[1]) as file:
            reader = csv.DictReader(file)
            for row_1 in reader:
                for item in necessaryColumns:
                    if item not in row_1:
                        sys.exit(f"Missing column '{item}' in the file. Necessary")
                break
    return sys_arguments[1]


def load_leads(file_, valid_months):
    new_file = hide_emails(file_)
    leads = []
    with open(new_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tags'] == "" and row['Estágio no funil'] != 'Cliente': #separating leads from clients
                row['Data da última conversão'] = cleaning_date(row['Data da última conversão'])
                if row['Data da última conversão'][:7] not in valid_months and valid_months != []:
                    pass
                else:
                    leads.append({"email":row['Email'], "data_conv":row['Data da última conversão'], "origem":row['Origem da última conversão'].strip().capitalize()})
    return leads


def cleaning_date(date):
    match_date = re.match(r'.*(\d{4}\-\d{1,2}\-\d{1,2})', date)
    if match_date:
        return match_date.group(1)
    else:
        return "--"


def get_origins(leads_dicts):
    origens = []
    for lead in leads_dicts:
        if lead["origem"] not in origens:
            origens.append(lead["origem"])
    return origens


def get_dates(leads_dicts):
    dates = []
    for lead in leads_dicts:
        if lead["data_conv"][:7] not in dates:
            dates.append(lead["data_conv"][:7])
    return dates


def info(leads):
    #How many origins? How many leads per origin?
    lista_valores_origens = []
    for origem in get_origins(leads):
        count = 0
        for lead in leads:
            if lead["origem"] == origem:
                count += 1
        lista_valores_origens.append({"origem":origem, "quantidade":count, "porcentagem":'{:.2f}%'.format(count/len(leads)*100)})

    tabela_info = []
    for origem in sorted(lista_valores_origens, key = lambda origem: origem["quantidade"], reverse=True):
        tabela_info.append([origem["origem"], origem["quantidade"], origem["porcentagem"]])

    tabela_info.append(SEPARATING_LINE)

    tabela_info.append([f"{len(get_origins(leads))} origins", f"{len(leads)} leads", '{:.2f}%'.format(100)])
    print("\n",tabulate(tabela_info, headers=["Conversion Origin","# leads", "% conv"]),"\n")

    #conversões por mês
    tabela_info = []
    lista_valores_conversoes = []
    for date in get_dates(leads):
        count = 0
        for lead in leads:
            if lead["data_conv"][:7] == date:
                count += 1
        lista_valores_conversoes.append({"data":date, "quantidade":count, "porcentagem":'{:.2f}%'.format(count/len(leads)*100)})

    for conversoes in sorted(lista_valores_conversoes, key = lambda conversoes: conversoes["data"]):
        tabela_info.append([conversoes["data"], conversoes["quantidade"], conversoes["porcentagem"]])

    tabela_info.append(SEPARATING_LINE)

    tabela_info.append(["", f"{len(leads)} conversions", '{:.2f}%'.format(100)])
    print(tabulate(tabela_info, headers=["Date","# conversions", "% conv"]),"\n")


if __name__ == "__main__":
    main()