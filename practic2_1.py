""" n = "Маша"
age = 20
# print('Меня зовут %s. Мне  %d лет.' % (n, age))
# print('Меня зовут {}. Мне  {} лет.'.format(n, age))
print(f'Меня зовут {n}. Мне  {age} лет.')
"""
""" a = int(input())
if a % 2 == 0:
    print('число четное')
else:
    print('число нечетное') """

""" a = input()
# print(p)
if a.isdigit() or (a[0] == '-' and a[1:].isdigit()):
    a = int(a)
    if a < 0:
        print('Отрицательное')
    elif a > 0:
        print('Положительное')
    else:
        print('Ноль')
else:
    print('Не число') """

""" age = int(input())
if age < 0:
    print('Не родился')
elif age >= 0 and age <= 18:
    print('Не совершеннолетний')
elif 18 <= age <= 23:
    print('Студент')
elif 23 < age < 70:
    print('Работающий')
else:
    print('Пенсионер')
"""

""" s = input('Введите время года: ')
s = s.lower().capitalize()
if s == "Лето":
    print(f'{s} - Море, солнце, пляж')
elif s == "Осень":
    print(f'{s} - Дождь')
elif s == "Зима":
    print(f'{s} - Лыжи')
elif s == "Весна":
    print(f'{s} - Жизнь вернулась!')
else:
    print(f'{s} - Это не время года')
"""

""" s = input('Введите номер телефона, начиная с цифры 9: ')
if len(s) == 10 and s[0] == '9':
    print('Сотовый')
else:
    print('Это не верный формат')
"""
""" # Задание №1
x = int(input())
a = None
if x < 0:
    a = x + 1
    print(a)
elif x >= 0 and x < 10:
    a = 2 * x
    print(a)
elif x >= 10:
    a = 0
    print(a) """

""" # Задание №2
p = input('Введите пароль: ')
if p == 'груша':
    print('Доступ открыт')
else:
    print('Доступ запрещен') """

""" # Задание №3
wt = int(input('Введите ваш вес: '))
ht = int(input('Введите ваш рост: '))
owt = ht - 100
if wt < owt:
    print('Надо поправиться')
elif wt > owt:
    print('Надо похудеть')
else:
    print('У вас оптимальный вес!') """

""" # Задание №4
x1 = 0
x2 = 200
x3 = 200
if x2 < x1 > x3 or (x2 < x1 > x3 and x2 == x3):
    print("Наибольшее число: " + str(x1))
elif x3 < x2 > x1 or (x3 < x2 > x1 and x1 == x3):
    print("Наибольшее число: " + str(x2))
elif x2 < x3 > x1 or (x2 < x3 > x1 and x1 == x2):
    print("Наибольшее число: " + str(x3))
else:
    print('Числа равны') """

""" # Задание №5
stage = int(input('Введите стаж: '))
age = int(input('Введите возраст: '))
if stage >= 5 and age <= 40:
    print('Кандидат подходит')
else:
    print('Кандидат не подходит') """

""" # Задание №6
corner1 = int(input('Введите первый угол: '))
corner2 = int(input('Введите второй угол: '))
corner3 = 180 - corner1 - corner2
if corner2 < corner1 > corner3 or (corner2 < corner1 > corner3 and corner2 == corner3):
    if corner1 > 90:
        print('Треугольник тупоугольный')
    elif corner1 == 90:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник остроугольный')
elif corner3 < corner2 > corner1 or (corner3 < corner2 > corner1 and corner1 == corner3):
    if corner2 > 90:
        print('Треугольник тупоугольный')
    elif corner2 == 90:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник остроугольный')
elif corner2 < corner3 > corner1 or (corner2 < corner3 > corner1 and corner1 == corner2):
    if corner3 > 90:
        print('Треугольник тупоугольный')
    elif corner3 == 90:
        print('Треугольник прямоугольный')
    else:
        print('Треугольник остроугольный')
else:
    print('Треугольник равносторонний и равноугольный') """
