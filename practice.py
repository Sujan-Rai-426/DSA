# Bubble sort
def bubble_sort(array):
    i=0    
    made_swap = True
    
    while made_swap:
        made_swap = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                made_swap = True
    return array
        

# Selection Sort
def selection_sort(array):
    for i in range(len(array)):
        min_char_index = i
        
        for j in range(i, len(array)):
            if array[j]<array[min_char_index]:
                min_char_index=j
        if min_char_index != i:
            array[i], array[min_char_index] = array[min_char_index], array[i]
    return array


# Input:
# =======> USAGE FUNCTION CALL
raw_array_list = input("Enter list of number seperated by comma(',') : ")
array_list = [int(item.strip()) for item in raw_array_list.split(",")]
print(f'''
    Input array : {array_list}
    Output sorted array using bubble sort: {(selection_sort(array_list))}
    ''')