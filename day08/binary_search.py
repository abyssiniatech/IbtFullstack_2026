def binary_search(items, target):
    """
    Binary Search Algorithm

    Returns:
        index if found
        -1 if not found
    """


    low = 0

    high = len(items)-1



    while low <= high:


        mid = (low + high) // 2



        if items[mid] == target:

            return mid



        elif items[mid] < target:

            low = mid + 1



        else:

            high = mid - 1



    return -1