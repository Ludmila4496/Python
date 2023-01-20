# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3

# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0

import random

def main(k):
    coefficients=CoefficientssGeneration(k)
    polinomial=CreatePolynomial(coefficients)
    # print(coefficients)
    print(polinomial)


def CoefficientssGeneration(quantity):
    coefficientsArray=[]
    for i in range(quantity+1):
        coefficientsArray.append(random.randint(0,10))
    return coefficientsArray


def CreatePolynomial(coefficients):
    polynomial=''
    for i in range(len(coefficients)-1,-1,-1):
        polynomial+=(str(coefficients[i])+('*x^'+str(i))*(i!=0))*(coefficients[i]!=0)
        if i==0: polynomial += ' = 0'
        elif coefficients[i-1]!=0: 
            if random.randint(0,2)==0: polynomial += ' + '
            else: polynomial += ' - '
    return polynomial

main(9)
main(5)
main(3)