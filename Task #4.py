# Открытие файла для чтения и записи
with open('input.txt', 'r') as f, open('output.txt', 'w') as out_file:
    # Считывание первой строки (первого числа)
    x = int(f.readline())
    print("Используем число: ", x)

    print('Задача 1.1')
    if 1 <= x <= 100 or 200 <= x <= 300:
        result = "Число попадает в диапазон от 1 до 100 или от 200 до 300"
    else:
        result = "Число не попадает в диапазон от 1 до 100 или от 200 до 300"
    print(result)
    out_file.write(result + "\n")

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
    out_file.write(result + "\n")

    print('Задача 1.3')
    # Считывание третьей строки (третьего числа)
    n = int(f.readline())
    print("Используем число: ", n)

    for i in range(n):
        result = str(i + 1) + ": 000"
        print(result)
        out_file.write(result + "\n")
