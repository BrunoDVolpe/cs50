def main():
    converted = frac_to_perc("Fraction: ")
    if converted <= 0.01:
        print("E")
    elif converted >= 0.99:
        print("F")
    else:
        print(f"{converted:.0%}")

def frac_to_perc(prompt):
    while True:
        try:
            frac = input(prompt).partition("/")
            x = int(frac[0])
            y = int(frac[-1])
            if x > y:
                pass
            else:
                return x/y
        except (ValueError, ZeroDivisionError):
            pass

main()

# Porcentagem sem casa decimal f"{[va]:.0%}"
#ValueError if int(str)
#ZeroDivisionError if divided by 0