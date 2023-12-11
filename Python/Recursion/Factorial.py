def Fact(n):
    if n == 1 or n == 0 : return 1
    return Fact(n-1) * n 

N = int(input("Enter N: "))
Res = Fact(N)
print(f"{N}! = {Res}")