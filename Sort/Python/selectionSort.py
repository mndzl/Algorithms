def selectionSort():
    arr = [1,5,6,3,7,2,6]

    for i in range(len(arr)):
        lower = 99999999
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                arr[i],arr[j] = arr[j],arr[i]

    print(arr)


selectionSort()