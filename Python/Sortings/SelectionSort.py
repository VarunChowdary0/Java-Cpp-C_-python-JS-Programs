arr = list(map(int,input("Enter: ").split()))
n = len(arr)
for i in range(n):
    min_idx = i
    for j in range(i,n):
        if arr[min_idx] > arr[j]:
            min_idx = j
    print(arr[min_idx]," swap ",arr[i],arr) 
    arr[min_idx] , arr[i] = arr[i] , arr[min_idx]
print(arr) 