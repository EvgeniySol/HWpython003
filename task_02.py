import random

def nm(n1):
    list = random.sample(range(n1), n1)
    return list

def mult(nl, len):
    a = []
    for i in range(len//2):
        a.append(nl[i]*nl[-(i+1)])
    if len % 2:
        a.append(nl[len//2])
    return a

    
x = int(input("Введите число: "))
num_list = nm(x)
print(num_list)
print(mult(num_list, x))
