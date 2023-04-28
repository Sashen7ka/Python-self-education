import pandas as pd
import matplotlib.pyplot as plt
import subprocess

# Открытие файла для чтения и записи
with open('input.txt', 'r') as f, open('output.txt', 'w') as out_file:

    print('Задача 1.1')
    # Считывание первой строки (первого числа)
    x = int(f.readline())

    print("Используем число: ", x)


    if 1 <= x <= 100 or 200 <= x <= 300:
        result = "Число попадает в диапазон от 1 до 100 или от 200 до 300"
    else:
        result = "Число не попадает в диапазон от 1 до 100 или от 200 до 300"
    print(result)
    out_file.write('Задача 1.1:\n'+ result +"\n")

    print('Задача 1.2')
    # Считывание второй строки (второго числа)
    y = int(f.readline())

    print("Используем число: ", y)


    time = 0
    while y < 100:
        y += 1
        time += 2
    result = "Вода закипит через " + str(time) + " минут"
    print(result)
    out_file.write('Задача 1.2:\n'+ result +"\n")

    print('Задача 1.3')
    # Считывание третьей строки (третьего числа)
    n = int(f.readline())

    print("Используем число: ", n)
    out_file.write('Задача 1.3:\n')

    for i in range(n):
        result = str(i + 1) + ": 000"
        print(result)
        out_file.write(result +"\n")


    print('Задача 1.4')
    # Считывание четвертой строки (высоты треугольника)
    h = int(f.readline())

    print("Используем число: ", h)
    out_file.write('Задача 1.4:\n')

    for i in range(h):
        result = "**" * (i + 1)
        print(result)
        out_file.write(result +"\n")



    print('Задача 2.1')
    out_file.write('Задача 2.1:\n')
# Считывание значений A, B, C, M и K из файла input.txt
with open('input.txt', 'r') as f:
    lines = f.readlines()
    a = int(lines[4].strip().split('=')[1])
    b = int(lines[5].strip().split('=')[1])
    c = int(lines[6].strip().split('=')[1])
    m = int(lines[7].strip().split('=')[1])
    k = int(lines[8].strip().split('=')[1])

# Проверка, пройдет ли коробка через дверь
if a <= m and b <= k or b <= m and a <= k or c <= m and a <= k or a <= m and c <= k or c <= m and b <= k or b <= m and c <= k:
    result = "Коробка пройдет через дверь"
else:
    result = "Коробка не пройдет через дверь"
print(result)

# Запись результата в файл output.txt
with open("output.txt", "a") as f:
    f.write(result + "\n")

print('Задача 2.2')

# Считывание десятой строки (высоты треугольника)
with open("input.txt") as f:
    for i in range(9):
        f.readline()
    h = int(f.readline())

print("Используем число: ", h)
with open("output.txt", "a") as f:
    f.write('Задача 2.2:\n')

# Вывод треугольника
for i in range(h):
    result = " " * (h - i - 1) + "*" * (2 * i + 1)
    print(result)
    with open("output.txt", "a") as out_file:
        out_file.write(result + "\n")

print('Задача 2.3')
# Открытие файла output.txt на запись
with open("output.txt", "a") as out_file:
    out_file.write("\nЗадача 2.3\n")

# Открытие файла input.txt на чтение
with open("input.txt") as in_file:

    # Считывание 11 строки (число N)
    N = int(in_file.readlines()[10])

    # Создание списка квадратов чисел до N
    squares = [i**2 for i in range(1, N)]

    # Вывод чисел меньше N
    for i in squares:
        if i < N:
            print(i)
            with open("output.txt", "a") as out_file:
                out_file.write(" " + str(i) + "\n")


print('Задача 3.1')
# Открываем файл для чтения и чтения числа K
with open('input.txt', 'r') as f:
    K = int(f.readline())

# Проверяем, можем ли купить K шариков мороженого
if K % 3 == 0 or K % 5 == 0 or K % 8 == 0:
    result = "да"
else:
    result = "нет"

# Выводим ответ на экран и записываем в файл output.txt
with open('output.txt', 'a') as out_file:
    print(result)
    out_file.write("Задача 3.1:\n " + result + "\n")

with open('output.txt', 'a') as out:
    out.write('\nЗадача 3.2:\n')
with open('input.txt', 'r') as f:
    for i in range(12):
        f.readline()
    X = int(f.readline().strip().split('=')[1])
    Y = int(f.readline().strip().split('=')[1])
    Z = int(f.readline().strip().split('=')[1])

years = 0
x = X
while x < Z:
    x = x * (1 + Y / 100)
    years += 1

with open('output.txt', 'a') as out:
    out.write("За " + str(years) + " лет(года) сумма вклада превысит " + str(Z) + " тысяч гривен")

with open('output.txt', 'a') as out:
    out.write('\n\nЗадание 3.3:\n')
with open('input.txt', 'r') as f:
    for i in range(15):
        f.readline()
    N = int(f.readline().strip())
digit_sum = 0
for digit in str(N):
    digit_sum += int(digit)
with open('output.txt', 'a') as out:
    out.write("Сумма цифр числа " + str(N) + " равна " + str(digit_sum))
print("Сумма цифр числа", N, "равна", digit_sum)
