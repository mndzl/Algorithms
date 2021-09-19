def quickSort(arr, begin,end):
    if begin<end:
        print()
        pivot = partition(arr, begin, end)

        quickSort(arr, begin, pivot-1)
        quickSort(arr, pivot+1, end)


def partition(arr, begin, end):
    i = begin-1
    pivot = arr[end]
    print(arr, pivot, begin, end)
    for j in range(begin,end):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j], arr[i]
            print(arr)

    arr[i+1], arr[end] = arr[end], arr[i+1]
    print(arr)

    return i+1


arr = [5,1,3,2,6,7,5,4]
quickSort(arr, 0, len(arr)-1)
print(arr)

