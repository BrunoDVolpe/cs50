def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    print(text)

def main():
    convert(input("What's your sentence? "))

main()