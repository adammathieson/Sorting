import random


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(merged_arr)
    # a_count = 0
    # b_count = 0

    for i in range(elements):
        print("+++++++>>>>>>>>", range(elements))
        print(i, arrA, arrB, merged_arr)
        if len(arrA) == 0:
            print('elements: ', elements)
            print("arrB[0])", arrB[0])
            merged_arr[i] = arrB.pop(0)
            print("merged_arr:", merged_arr[i])
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)


    # return sorted(arrA+arrB)
    return merged_arr
        # for a in len(arrA - 1):
        #     for b in len(arrB - 1):
        #         if arrA[a] > arrB[b]:

        # if arrA[0] < arrB[0]:
        #     merged_arr[i] == arrA[i]
        # else:
        #     merged_arr[i] == arrB[i]


        # if arrA[i] == None and arrB[i] != None:
        #     merged_arr[i] = arrB[i]
        # elif arrB[i] == None and arrA[i] != None:
        #     merged_arr[i] = arrA[i]
        # elif arrA[i] < arrB[i]:
        #     merged_arr[i] = arrA[i]
        # else:
        #     merged_arr[i] = arrB[i]
    # TO-DO

    # while elements > 0:
    #     if arrA[0] > arrB[0] or arrA[0] == None:
    #         merged_arr.append(arrB.pop([0]))
    #     elif arrA(0) < arrB[0] or arrB[0] == None:
    #         merged_arr.append(arrA.pop([0]))
    #     else:
    #         merged_arr.append(arrA.pop[0])
        





# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # print("----->", arr)
    # TO-DO
    if len(arr) > 1:
        # right = arr[(len(arr)//2):]# inclusive
        # left = arr[:(len(arr)//2)]
        right = merge_sort(arr[(len(arr)//2):])# inclusive
        # print('right: ', right)
        left = merge_sort(arr[:(len(arr)//2)])
        # print('left: ', left)
        # print("left:", left)
        # print("right:", right)
        # merge_sort(right)
        # print("right am:", right)
        # merge_sort(left)
        # print("left am:", left)

        return merge(left, right)
    
    return arr

l = list(range(10))
random.shuffle(l)
print("\noriginal_list:", l)
print("\noriginal_list_length:", len(l))

print("\nsorted:", merge_sort(l))
print("\nsorted_length:", len(merge_sort(l)))
# print("\nsorted:[10]", merge_sort(l)[10])

# print(l)
# print(l.pop(0))
# print(l)













# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


# cache = {}

# def fib(n):
#     if n < 2:
#         return n
#     elif n in cache:
#         return cache[n]
#     else:
#         cache[n] = fib(n-1) + fib(n-2)
#     return cache[n]


