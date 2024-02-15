def quickSort(arr,l,n):
    if n-l <= 1:
        return arr[l:n]
    yellow = l + 1
    pivote = arr[l]
    for green in range(l+1,n):
        if arr[green] <= pivote:
            arr[green],arr[yellow] = arr[yellow],arr[green]
            yellow+=1
    arr[l],arr[yellow-1] = arr[yellow-1],arr[l]
    left =  quickSort(arr,l,yellow-1)
    right = quickSort(arr,yellow,n)
    return left+[arr[yellow-1]]+right

arr = list(map(int,input("Enter: ").split()))
print(quickSort(arr,0,len(arr)))
