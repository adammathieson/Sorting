
def quicksort(items):
    print(f"SORTING: {items}")
    if len(items) <= 1:
        return items
    # 1. Select the last element as the pivot.
    pivot = items[-1]
    left = []
    right = []
    for i in range(len(items) - 1):
        item = items[i]
        if item < pivot:
            # 2. Move all elements smaller than the pivot to the left.
            left.append(item)
        else:
            # 3. Move all elements greater than the pivot to the right.
            right.append(item)
    print(f"LEFT: {left}, PIVOT: {pivot}, RIGHT: {right}")
    # 4. While LHS and RHS are greater than 1, repeat steps 1-3 on each side.
    return quicksort(left) + [pivot] + quicksort(right)
​