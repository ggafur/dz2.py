# Task 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# from operator import truediv
# def CheckEnteredNumber(number):
#     try:
#         float(number)
#         return True
#     except ValueError:
#         return False

# def SummarizeDigits(number):
#     sumDigits=0
#     for i in number:
#         if i.isdigit():
#             sumDigits=sumDigits+float(i)
#         else:
#             continue
#     print(f"Sum of all digits of the entered number = {sumDigits}")

# print("This program add up all digits of the entered number.")
# mineNumber = input("Please enter your number: ")
# if CheckEnteredNumber(mineNumber)==False:
#     print(f"Wrong format of the entered number! Check the entered number!")
# else:
#     SummarizeDigits(mineNumber)

# Task 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def CheckEnteredNumber(number):
#     try:
#         int(number)
#         return True
#     except ValueError:
#         return False

# def MultiplyDigits(number):
#     result=1
#     for i in range(1,number+1):
#         result=result*i
#         print(result,end=" ")

# mineNumber = input("Enter your integer number: ")
# if CheckEnteredNumber(mineNumber)==False:
#     print(f"Wrong format of the entered number! Check the entered number!")
# else:
#     mineNumber=int(mineNumber)
#     MultiplyDigits(mineNumber)


#  Task 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# def dictionary(number):
#     diction = {}
#     for i in range(1, number+1):
#         diction[i] = (1+1/i)**i
#     return [diction, 'Сумма значений без ключей = {}'.format (round(sum(diction.values()), 2))]


# n = int(input("Введите число:"))
# print(dictionary(n))


