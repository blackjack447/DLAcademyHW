#EASY
# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    miles = km * 1.609
    print(miles)

convert(100)

print('\n')
# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    step = pow(10,ndigits)
    return int(number * step + 0.5) / step
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print('\n')
# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)
def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)
    ticket_number = list(map(int,ticket_number))
    if sum(ticket_number[:3]) == sum(ticket_number[3:]):
        return True
    else:
        return False
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

print('\n')
#NORMAL
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fib(n, m):
    i = 1
    fib_list=[1,1]
    while i < m:
        fib_list.append(fib_list[i-1] + fib_list[i])
        i += 1
    return fib_list[n:m]

print(fib(1,10))

print('\n')
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    n = len(origin_list)
    for i in range(0,n-1):
        for j in range(i  +1, n):
            if origin_list[i] > origin_list[j]:
                origin_list[i],origin_list[j] = origin_list[j], origin_list[i]
    return origin_list
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

print('\n')
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(a, b):
    result = []
    for i in b:
        if a(i):
            result.append(i)
        else:
            continue
    return result

#print((my_filter((lambda i: i < 25), b=[1, 100, 500, 7, 8, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

#print('\n')
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def paral(A1,A2,A3,A4):
    if (A1,A2) == (A3,A4) and (A1,A4) == (A2,A3):
        return 'являются вершинами'
    else:
        return 'не являются вершинами'

A1=[7,1]
A2=[8,4]
A3=[3,5]
A4=[1,2]
print(paral(A1,A2,A3,A4))
A1=[2,2]
A2=[2,2]
A3=[2,2]
A4=[2,2]
print(paral(A1,A2,A3,A4))

