def bin(n):
    y = []
    while n>0:
        y.append(n%2)
        n = int(n/2)
    return y
x = int(input("Введите число: "))
res = bin(x)
res.reverse()
print(*res, sep="")