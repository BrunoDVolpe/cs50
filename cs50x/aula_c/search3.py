#Vi isso na aula 3, mas apenas com pseudocode e exemplos visuais, mas não o código.
# Fiz aprendendo no YouTube com o exemplo recursion.py e refiz aqui por mim mesmo aplicando a lógica.
#Dúvida: Consigo retornar uma lista sem arrumar a original? Ainda não sei.

def main():
    lista_num = [20, 500, 10, 5, 100, 1, 50, 2]
    print(sort(lista_num))

def sort(lista):
    #Dividir a lista em 2 e merge colocando numa nova lista.
    if len(lista) > 1:
        middle_index = len(lista)//2
        lista_left = lista[:middle_index]
        lista_right = lista[middle_index:]
        sort(lista_left)
        sort(lista_right)

        #Quando ficarem duas arrays:
        i = 0
        j = 0
        k = 0
        while i < len(lista_left) and j < len(lista_right):
            if lista_left[i] < lista_right[j]:
                lista[k] = lista_left[i]
                i += 1
            else:
                lista[k] = lista_right[j]
                j += 1
            k += 1

        while i < len(lista_left):
            lista[k] = lista_left[i]
            i += 1
            k += 1

        while j < len(lista_right):
            lista[k] = lista_right[j]
            j += 1
            k += 1

        return lista


if __name__ == "__main__":
    main()