print("""
Написать скрипт который решит задачи:
1 уровень
1) Пользователь вводит число а и число b. Возвести а в степень b
""")

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = a ** b

print("Результат возведения числа", a, "в степень", b, "равен", result)

print("""
2) Пользователь вводит 2 числа. Вывести наибольшее из них
""")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
if a > b:
    print("Наибольшее число: ", a)
else:
    print("Наибольшее число: ", b)

print("""
3) Пользователь вводит сумму в гривне и курс доллара. Нужно пересчитать сумму в долларе
""")
sum_ua = int(input("Сумма в гравне: "))
usd_rate = int(input("Курс доллара: "))

sum_usd = sum_ua/usd_rate
print("Сумма в долларах: ", sum_usd)

print("""
4) Пользователь вводит цифру от 1 до 7, нужно вывести соотвествующий день недели
""")
day_num = int(input("Введите номер дня недели (от 1 до 7): "))

if day_num == 1:
    print("Понедельник")
elif day_num == 2:
    print("Вторник")
elif day_num == 3:
    print("Среда")
elif day_num == 4:
    print("Четверг")
elif day_num == 5:
    print("Пятница")
elif day_num == 6:
    print("Суббота")
elif day_num == 7:
    print("Воскресенье")
else:
    print("Некорректный номер дня недели")

print("""
2 уровень

1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"
""")
num = int(input("Введите число: "))

if num % 2 == 0:
    print("четное")
else:
    print("нечетное")

print(""" 
2) Пользователь вводит 3 числа. Вывести наименьшее из них
""")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

if a <= b and a <= c:
    print("Наименьшее число:", a)
elif b <= a and b <= c:
    print("Наименьшее число:", b)
else:
    print("Наименьшее число:", c)

print("""
3) 3) Из Убудского чата Аня узнала, что рекомендуется спать хотя бы А часов в сутки, но пересыпать тоже вредно и не
стоит спать более В часов. Сейчас Аня спит Н часов в сутки.
Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите "Это нормально".
Если Аня спит менее А часов, выведите "Недосып", если же более В часов, то выведите "Пересып" Получаемое число
А всегда меньше либо равно В (то есть это проверять не надо).
""")
a = int(input("Введите минимально рекомендуемое количество часов сна: "))
b = int(input("Введите максимально рекомендуемое количество часов сна: "))
n = int(input("Введите количество часов сна, которое Аня спит в сутки: "))

if n >= a and n <= b:
    print("Это нормально")
elif n < a:
    print("Недосып")
else:
    print("Пересып")