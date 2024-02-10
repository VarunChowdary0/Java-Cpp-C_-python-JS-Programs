# find the length of all sub array of length 'k'
def WindowSum(nums,k):
    CurrentSubArr = sum(nums[:k])
    finalListOfSums = [CurrentSubArr]
    for i in range(1,len(nums)-k+1):
        CurrentSubArr = CurrentSubArr - nums[i-1] # - its previous element
        CurrentSubArr = CurrentSubArr + nums[i+k-1] # + its next element
        finalListOfSums.append(CurrentSubArr)
    return finalListOfSums
nums = list(map(int,input("Enter nums: ").split()))
k = int(input("Enter window Size"))
x = WindowSum(nums,k)
print(x)