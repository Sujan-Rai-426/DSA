# NOTE: Selection Sort

def selection_sort(array):
    for i in range(len(array)):
        # Assume the current position holds the minimum
        min_index = i
        # Find the index of the actual minimum element in the remaining unsorted array
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


# =======> USAGE FUNCTION CALL
raw_array_list = input("Enter list of number seperated by comma(',') : ")
array_list = [int(item.strip()) for item in raw_array_list.split(",")]
print(f'''
    Input array : {array_list}
    Output sorted array using Selection sort: {(selection_sort(array_list))}
    ''')