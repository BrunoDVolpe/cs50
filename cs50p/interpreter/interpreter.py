def main():
    x, y, z = input("Expression: ").split(" ")
    print(f"{float(calculator(int(x),y,int(z))):.1f}")

def calculator(n1, op, n2):
    if op == "+":
        return n1+n2
    elif op == "-":
        return n1-n2
    elif op == "*":
        return n1*n2
    else:
        return n1/n2

main()

"""
def main():
    x, y, z = input("Expression: ").split(" ")
    print(f"{float(calculator(int(x),y,int(z))):.1f}")

def calculator(n1,op,n2):
    match op:
        case "+":
            return n1+n2
        case "-":
            return n1-n2
        case "*":
            return n1*n2
        case "/":
            return n1/n2
"""