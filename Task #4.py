def task_31(n: int) -> str:
    """Функция для решения задачи 3.1"""
    fives = n // 5
    remainder = n % 5

    while fives >= 0:
        if remainder % 3 == 0:
            return f'Можно купить {n} шариков мороженого'
        else:
            fives -= 1
            remainder += 5
    return f'Нельзя купить {n} шариков мороженого'


# Открытие файлаd для чтения и записи
with open('input.txt', 'r', encoding='utf-8') as f, open('output.txt', 'w', encoding='utf-8') as out_file:
    print('Задача 1.1')
    # Считывание первой строки (первого числа)
    x = int(f.readline())

    print("Используем число: ", x)

    if 1 <= x <= 100 or 200 <= x <= 300:
        result = "Число попадает в диапазон от 1 до 100 или от 200 до 300"
    else:
        result = "Число не попадает в диапазон от 1 до 100 или от 200 до 300"
    print(result)
    out_file.write('Задача 1.1:\n' + result + "\n")

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
    out_file.write('Задача 1.2:\n' + result + "\n")

    print('Задача 1.3')
    # Считывание третьей строки (третьего числа)
    n = int(f.readline())

    print("Используем число: ", n)
    out_file.write('Задача 1.3:\n')

    for i in range(n):
        result = str(i + 1) + ": 000"
        print(result)
        out_file.write(result + "\n")

    print('Задача 1.4')
    # Считывание четвертой строки (высоты треугольника)
    h = int(f.readline())

    print("Используем число: ", h)
    out_file.write('Задача 1.4:\n')

    for i in range(h):
        result = "*" * (i + 1)
        print(result)
        out_file.write(result + "\n")

    print('Задача 2.1')
    out_file.write('Задача 2.1:\n')
    # Считывание значений A, B, C, M и K из файла input.txt
    a, b, c, m, k = (int(f.readline().strip().split('=')[1]) for _ in range(5))
    print(f'{a = }, {b = }, {c = }, {m = }, {k = }')

    # Проверка, пройдет ли коробка через дверь
    if a <= m and b <= k or b <= m and a <= k or c <= m and a <= k or a <= m and c <= k or c <= m and b <= k or b <= m and c <= k:
        result = "Коробка пройдет через дверь"
    else:
        result = "Коробка не пройдет через дверь"
    print(result)

    # Запись результата в файл output.txt
    out_file.write(result + "\n")

    print('Задача 2.2')

    # Считывание десятой строки (высоты треугольника)
    h = int(f.readline())

    print("Используем число: ", h)
    out_file.write('Задача 2.2:\n')

    # Вывод треугольника
    for i in range(h):
        result = " " * (h - i - 1) + "*" * (2 * i + 1)
        print(result)
        out_file.write(result + "\n")

    print('Задача 2.3')
    out_file.write("\nЗадача 2.3\n")
    # Чтение числа N
    N = int(f.readline())

    # Создание списка квадратов чисел до N
    squares = [i ** 2 for i in range(1, N)]

    # Вывод чисел меньше N
    for i in squares:
        if i < N:
            print(i)
            out_file.write(" " + str(i) + "\n")

    print('Задача 3.1')
    # Чтения числа K
    K = int(f.readline())

    # Проверяем, можем ли купить K шариков мороженого
    result = task_31(k)

    # Выводим ответ на экран и записываем в файл output.txt
    print(result)
    out_file.write("Задача 3.1:\n " + result + "\n")

    print('Задача 3.2')
    out_file.write('\nЗадача 3.2:\n')

    x, y, z = (int(f.readline().strip().split('=')[1]) for _ in range(3))

    years = 0
    while x < z:
        x = x * (1 + y / 100)
        years += 1
    result = "За " + str(years) + " лет(года) сумма вклада превысит " + str(z) + " тысяч гривен\n"
    print(result)
    out_file.write(result)

    print('Задача 3.3')
    out_file.write('\n\nЗадание 3.3:\n')
    N = f.readline().strip()
    digit_sum = sum(map(int, N))

    out_file.write("Сумма цифр числа " + str(N) + " равна " + str(digit_sum))
    print("Сумма цифр числа", N, "равна", digit_sum)
