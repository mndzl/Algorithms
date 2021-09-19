def selectionSort():
    arr = [1,5,6,3,7,2,6]

    # For every i, find min value starting from it and then swap
    for i in range(len(arr)):
        lower = 99999999
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]

    print(arr)


selectionSort()