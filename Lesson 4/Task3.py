# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1
# out
# Negative value of the number of numbers!
# []

# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

from random import uniform

def list_nums(count: int):
    list_nums = []
    
    for i in range(count):
        list_nums.append(round(uniform(1, count)))
    return list_nums


def non_recurring (list_first):
    list_unique = []
    for i in range(len(list_first)):
        if list_first.count(list_first[i]) == 1:
            list_unique.append(list_first[i])  
    return list_unique       


count = int(input("Insert the number: "))
if count <= 0:
    print("Negative value of the number of numbers!")
else:
    list_first = list_nums(count)
    print (list_first)
    print (non_recurring(list_first))