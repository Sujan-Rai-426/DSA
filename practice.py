# Bubble sort
# NOTE: Even if we made swap once than we need to recheck the whole array if its sorted. 
# NOTE: And  IF while gone through whole array loop if no sawap is made than it says array is sorted
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
        


# Input:
# =======> USAGE FUNCTION CALL
raw_array_list = input("Enter list of number seperated by comma(',') : ")
array_list = [int(item.strip()) for item in raw_array_list.split(",")]
print(f'''
    Input array : {array_list}
    Output sorted array using bubble sort: {(bubble_sort(array_list))}
    ''')