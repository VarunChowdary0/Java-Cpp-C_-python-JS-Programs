import heapq
input_Arr = list(map(int,input("Enter elements: ").split()))
sortedList = []
heapq.heapify(input_Arr) # heapify the list
for i in range(len(input_Arr)): # use length of the list only.
    sortedList.append(heapq.heappop(input_Arr))
print(sortedList)
