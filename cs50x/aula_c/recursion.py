def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

       #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

        return arr

arr_test = [1, 9, 6, 0, 4, 5, 3, 2]
print(merge_sort(arr_test))

"""
#Aqui ele altera a própria lista ao invésde criar uma nova.
def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

       #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

arr_test = [1, 9, 6, 0, 4, 5, 3, 2]
merge_sort(arr_test)
print(arr_test)
"""