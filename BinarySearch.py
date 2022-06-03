#BINARY SEARCH ALGORITHM
def binarySearch(arr, p, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == p:
            return mid
        elif arr[mid] < p:

            low = mid + 1
        else:

            high = mid - 1
    return -1


arr = [2, 3, 7, 5, 8]

p = 5
result = binarySearch(arr, p, 0, len(arr) - 1)
    
if result != -1:

    print("ELEMENT PRESENT AT INDEX: " + str(result))

else:

    print("FOUND NO ELEMENT")