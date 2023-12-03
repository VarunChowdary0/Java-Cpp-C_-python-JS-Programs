arr = list(map(int,input().split(" ")))
n = len(arr)
for i in range(0,n):
    for j in range(i,n):
        if(arr[i]>arr[j]):
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
print(arr)