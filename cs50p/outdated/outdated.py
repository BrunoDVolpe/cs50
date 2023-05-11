month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ]

def main():
  #User's date input
  while True:
    date = input("Date: ")
    try:
      month, day, year = date.split("/")
      month = int(month)
      day = int(day)
      year = int(year)
    except ValueError:
      pass
    else:
      if month < 1 or month > 12:
        pass
      elif day < 1 or day > 31:
        pass
      else:
        print(f"{year}-{month:02}-{day:02}")
        break
    try:
      month, day, year = date.split()
      year = int(year)
    except ValueError:
      pass
    else:
      if day[-1] == ",":
        day = day[:-1]
        if day.isnumeric() == False:
          pass
        elif int(day) < 1 or int(day) > 31:
          pass
        elif check_month(month) == False:
          pass
        else:
          print(f"{int(year)}-{(month_list.index(month)+1):02}-{int(day):02}")
          break
      else:
        continue

def check_month(m):
  for months in month_list:
    if months == m:
      return True
  return False

main()