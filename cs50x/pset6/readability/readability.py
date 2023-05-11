from cs50 import get_string

text = get_string("Text: ")

# letras, palavras, sentenças
letras = 0
palavras = 1
sentencas = 0

for char in text:
    if char.isalpha():
        letras += 1
    if char == " ":
        palavras += 1
    elif char in ['.', '?', '!']:
        sentencas += 1

# número médio de letras por 100 palavras no texto
l = letras / palavras * 100

# número médio de sentenças por 100 palavras no texto
s = sentencas / palavras * 100

# índice Coleman-Liau
indice = round(0.0588 * l - 0.296 * s - 15.8)

# print(f"letras: {letras}, palavras: {palavras}, sentencas: {sentencas}")
# print(f"l: {l}, s: {s}, indice: {indice}")

if indice >= 16:
    print("Grade 16+")
elif indice < 1:
    print("Before Grade 1")
else:
    print(f"Grade {indice}")