import random

def nm(n1):
    list = random.sample(range(n1), n1)
    return list

def sum(n_l, len):
    sm = 0
    for i in range(0, len, 2):
        sm = sm + n_l[i]
    return sm

x=int(input("Введите число: "))
num_list = nm(x)
print(num_list)
print(sum(num_list, x))
