# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print("_i_", arr[i])
        cur_index = i
        # RESETS TO THE CURRENT INDEX!!!
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i, len(arr)):
            # print(j)
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                # print('j was smaller than ci')
        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
                # arr[j], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    count = len(arr)
    # check_count = len(arr)
    while count > 0:
        for i in range(0, len(arr) - 1):
            if arr[i] <= arr[i+1]:
                count -= 1
                # print(count)
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print("found one at: ", arr[i], arr[i+1])
                count = len(arr)
                # print(count)
                # print(arr[1])

    #Loop through the array
    # copy_array = []
    # for i in range(0, len(arr) - 1):
        # print(arr[i])
    #compare each element to its right hand neighbor
    #If it is smaller, swap it with the neighbor
        # if arr[i] < arr[i+1]:
        #     arr[i], arr[i+1] = arr[i+1], arr[i]
        # copy_array = arr
        # bubble_sort(copy_array)
    #repeat loop until no swap occurs
    return arr

test_array = [10, 7, 2, 1, 9, 5, 3, 8, -1]
print("----->", bubble_sort(test_array))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

    