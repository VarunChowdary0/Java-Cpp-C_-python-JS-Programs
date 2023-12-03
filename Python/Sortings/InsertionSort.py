arr = list(map(int,input("Enter elements :").split(" ")))
n = len(arr)
for i in(range(1,n)):
    j = i 
    while (j>0 and (arr[j-1]>arr[j])):
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j-=1
print(f"Elements sorted using insertion: {arr}")