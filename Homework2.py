# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print('Введите вещественное число: ')
# a = int(input())
# sum = 0
# while a != 0:
#     p = a % 10
#     sum = sum + p
#     a = a // 10
# print(sum)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# a = int(input('Введите число:'))
# mult = 1
# for i in range(1, a):
#     mult = mult * i
#     print ((mult), end = ',')
# print(mult * (i + 1))    

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# list = []
# n = int(input('Введите число:'))
# sum = 0
# for i in range(1, n + 1):
#     sum = ((1+1/i)** i)
#     list.append(sum)    
# print(list)
# res = map(float, list)
# print(f'Сумма чисел: {sum(res)}') 

# 4. Реализуйте алгоритм перемешивания списка.

import random
new_list = [2, 5, 7, 0, 3.15, 'a']
print(new_list)
random.shuffle(new_list)
print(new_list)