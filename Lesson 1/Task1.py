# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
n = input("Введите номер дня недели: ")
if '6' <= n <= '7': 
    print ('Этот день выходной')
elif '1' <= n <= '5': 
    print ('Этот день будний')
else: 
    print("Такого дня не существует")