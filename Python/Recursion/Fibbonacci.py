def Fibbo(n):
    if n == 1 : return 1
    elif n == 0 : return 0
    return Fibbo(n-1) +  Fibbo(n-2) 

N = int(input("Enter N: "))
Res = Fibbo(N)
print(f"{N}th Fibbonacci Term = {Res}")