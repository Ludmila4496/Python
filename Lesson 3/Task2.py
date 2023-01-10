# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample


def list_rand_nums(count: int) -> list:
    list_nums = sample(range(1, count * 10), count)
    return list_nums


def product_of_numbers(list_nums: list):
    list_proiz = []
    for k in range(0, len(list_nums)//2):
        list_proiz.append (list_nums[k]*list_nums[len(list_nums)-1-k])
    if len(list_nums) % 2:
        list_proiz.append(list_nums[len(list_nums) // 2])
    return list_proiz


numb = int(input("Введите количество чисел: "))
if numb < 0:
    print("Введите число больше 0!")
else:
    all_list = list_rand_nums(numb)
    print(all_list)
    print(product_of_numbers(all_list))