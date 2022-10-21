
def bin(n):
    y = []
    while n>0:
        a = x%2
        n = int(n/2)
        y.append(a)
    return y

x = int(input("Введите число: "))
res = bin(x)
res.reverse()
print(*res, sep="")