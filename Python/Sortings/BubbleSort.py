arr = list(map(int,input().split(" ")))
n = len(arr)
for i in range(0,n):
    for j in range(i,n):
        if(arr[i]>arr[j]):
            arr[i],arr[j] = arr[j],arr[i]
    print(arr)
print(arr)
