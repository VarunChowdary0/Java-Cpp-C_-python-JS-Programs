MyList = list(map(int,input().split()))
X = int(input("Enter search value: "))
temp = MyList
flag = False
for i in temp:
    if X == i:
        print("Found at postion ",temp.index(i)+1)
        temp[temp.index(i)] = 'Done'
        flag = True
if not flag:
    print("Element Not Found")
print(temp)