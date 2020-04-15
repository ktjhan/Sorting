# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):

    for i in range(len(arr)):
        current_index = i
        for something in range(i+1, len(arr)):
            if arr[something] < arr[current_index]:
                current_index = something

        arr[i], arr[current_index] = arr[current_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range(len(arr)):
        for something in range(i+1, len(arr)):
            if arr[something] < arr[i]:
                arr[something], arr[i] = arr[i], arr[something]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
