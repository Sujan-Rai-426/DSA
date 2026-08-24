
# NOTE: BUBBLE Sort

def bubble_sort(array):
    made_swapped = True  # Need at least one pass or check
    
    while made_swapped:
        made_swapped = False  # Reset flag
        
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                # Swap if bigger
                array[i], array[i + 1] = array[i + 1], array[i]
                made_swapped = True  # Changes made, loop again
    
    return array


# =======> USAGE FUNCTION CALL
raw_array_list = input("Enter list of number seperated by comma(',') : ")
array_list = [int(item.strip()) for item in raw_array_list.split(",")]
print(f'''
    Input array : {array_list}
    Output sorted array using bubble sort: {(bubble_sort(array_list))}
    ''')