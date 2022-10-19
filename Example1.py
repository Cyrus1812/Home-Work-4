# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

number = int(input("Введите число: "))
count=2
while number > 1:
    if number % count == 0:
        print(count)
        number = number / count
    else: 
        count+=1



        
        
        
