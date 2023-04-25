print("1. Простий калькулятор:")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, /, *, mod, pow, div): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "/":
    result = num1 / num2
elif operation == "*":
    result = num1 * num2
elif operation == "mod":
    result = num1 % num2
elif operation == "pow":
    result = num1 ** num2
elif operation == "div":
    result = num1 // num2
else:
    print("Неверная операция")

print("Результат:", result)

print('2. Маємо 2 числа a і b. Визначте, чи ділиться a на b націло. Чи ділиться b на a?')
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a % b == 0:
    print("a делится на b нацело")
else:
    print("a не делится на b нацело")

if b % a == 0:

    print("b делится на a нацело")
else:
    print("b не делится на a нацело")

print ('3. Дано трицифрове число. Визначте, чи є серед його цифр однакові.')

num = input("Введите трехзначное число: ")

if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")
