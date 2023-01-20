# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# in
# 54
# out
# [2, 3, 3, 3]

# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# in
# 650
# out
# [2, 5, 5, 13]

import math 

def prime_numbers(numb):
    while numb != 1:
        list_nums = []
        while numb % 2 == 0:
            numb /= 2
            list_nums.append(2)
        for i in range(3, int(math.sqrt(numb)) + 1, 2):         
            while numb % i == 0:
                numb /= i
                list_nums.append(i)
    print(list_nums) 

num = int(input("Введите число: "))
prime_numbers(num)       