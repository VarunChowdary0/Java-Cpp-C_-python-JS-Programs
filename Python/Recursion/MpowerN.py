def getPower(base,power):
    if power == 0 : return 1
    return getPower(base,power-1) * base

base , power = map(int,input("Enter base and power: ").split())
Res = getPower(base,power)
print(f"{base}^{power} = {Res}")