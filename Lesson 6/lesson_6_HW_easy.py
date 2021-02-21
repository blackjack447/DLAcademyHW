import os
import shutil
# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5
print('\n')
#Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def makedir(i):
    try:
        os.mkdir('{}'.format(i))
    except FileExistsError:
        print('Папка', i, 'существует')

def removedir(i):
    os.rmdir('{}'.format(i))
print('\n')
# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

def showall():
    print('Директория содержит следующие папки и файлы - :', os.listdir())
print('\n')

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy(file_original, file_copy):
    shutil.copy(file_original, file_copy)
print('\n')




if __name__ == '__main__':
    try:
        a = float(input("a = "))
        b = float(input("b = "))
    except ValueError:
        print('Введите число!')
    try:
        c = avg(a, b)
    except NameError:
        print('Вы ввели не числа')
    try:
        print("Среднее геометрическое = {:.2f}".format(c))
    except NameError:
        print('Функция работает только с числами')

    for r in range(9):
        makedir('dir_{}'.format(r + 1))

    for r in range(9):
        removedir('dir_{}'.format(r + 1))

    copy('lesson 6 HW.py', 'lesson_6_HW_copy.py')

    showall()