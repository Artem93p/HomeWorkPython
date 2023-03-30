# Найдите сумму цифр трехзначного числа. (Случай числа с плавающей точкой и не обязательно 3-х значного)
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
import math
print("Введите трехзначное число: ")
number = str(input())
sum = 0
number = int(number.replace ('.','0'))
while (number != 0):
    x = number % 10
    sum = sum + x
    number = number // 10
print(sum)