def getSum(n):
    if n == 0 : return 0
    return getSum(n-1) + n 

N = int(input("Enter N: "))
Res = getSum(N)
print("Sum :",Res)