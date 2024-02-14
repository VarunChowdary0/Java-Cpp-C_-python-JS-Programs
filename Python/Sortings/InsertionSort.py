arr = list(map(int,input("Enter elements :").split(" ")))
n = len(arr)
for i in(range(1,n)):
    j = i 
    while (j>0 and (arr[j-1]>arr[j])):
        print(arr[j],"swap",arr[j-1],end=" - ")
        arr[j],arr[j-1] = arr[j-1] , arr[j]
        j-=1
        print(arr)
    print(arr)
print(f"Elements sorted using insertion: {arr}")