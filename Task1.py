#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def power(number, exp):
    if (exp == 1):
        return (number)
    if (exp != 1):
        return (number * power(number, exp - 1))
number = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(number, exp))