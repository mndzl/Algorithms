# QuickSort selects a pivot and sets its greater values at its right and lower at its left
# After that, it does the same action with each side of the pivot

def quickSort(arr, begin,end):
    if begin<end:
        print()
        # Step 1
        pivot = partition(arr, begin, end)

        # Step 2
        quickSort(arr, begin, pivot-1)
        # Step 3
        quickSort(arr, pivot+1, end)


def partition(arr, begin, end):
    # Sets last element as pivot..
    i = begin-1
    pivot = arr[end]
    print(arr, pivot, begin, end)
    
    for j in range(begin,end):
        # If the element is less than the pivot, sum 1 to i, and swap it with i    
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
            print(arr)

    # Put the pivot in its right order (i+1)
    arr[i+1], arr[end] = arr[end], arr[i+1]
    print(arr)

    return i+1


arr = [5,1,3,2,6,7,5,4]
quickSort(arr, 0, len(arr)-1)
print(arr)

