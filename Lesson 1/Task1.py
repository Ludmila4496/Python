# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
n = input("Введите номер дня недели: ")
if '6'<=n<='7': print ('да')
elif '1'<=n<='5': print ('нет')
else: print("Такого дня не существует")