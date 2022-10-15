# Task 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from operator import truediv
def CheckEnteredNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def SummarizeDigits(number):
    sumDigits=0
    for i in number:
        if i.isdigit():
            sumDigits=sumDigits+float(i)
        else:
            continue
    print(f"Sum of all digits of the entered number = {sumDigits}")

print("This program add up all digits of the entered number.")
mineNumber = input("Please enter your number: ")
if CheckEnteredNumber(mineNumber)==False:
    print(f"Wrong format of the entered number! Check the entered number!")
else:
    SummarizeDigits(mineNumber)
