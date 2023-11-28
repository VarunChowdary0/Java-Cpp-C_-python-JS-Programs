def FindTheElement(List,x):
    mid = len(List)//2
    if len(List) == 1 and x != List[mid]:
        print("Search Completed ... and Not found !!")
        return
    if x == List[mid]:
        print("Found")
        return
    if mid > x:
        FindTheElement(List[:mid],x)
    else:
        FindTheElement(List[mid:],x)
print("Enter elements: ")
MyList = list(map(int,input().split()))
x = int(input("Enter value to be searched: "))
FindTheElement(sorted(MyList),x)                    