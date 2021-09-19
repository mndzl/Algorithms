def bubbleSort():
    arr = [4,1,2,5,6,1,8,10]

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


bubbleSort()
    
