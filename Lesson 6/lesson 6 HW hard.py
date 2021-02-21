# ПРИМЕЧАНИЕ Для решения задачи необходимо познакомиться с модулями os, sys, argparse!
#     СМ. httpspythonworld.rumodulimodul-os.html,
#     httpspythonworld.rumodulimodul-sys.html,
#     httpshabr.comrucompanyruvdsblog440654
#
#     Задача похожа на задачу 2 из normal, однако, имеет особенности. Вы можете использовать решения из задачи 2.
#
#     Задача
#     Напишите небольшую консольную утилиту, позволяющую работать с папками и файлами.
#     Утилита должна работать с помощью параметров и флагов, передаваемых скрипту в командной строке.
#     Примеры
#         python hw06_hard.py -touch ..dir1test.txt -ls ..dir1
#         python hw06_hard.py -rm ..dir1test.txt -ls ..dir1
#         python hw06_hard.py -mkdir ..dir1newdir -ls ..dir1
#         python hw06_hard.py -ls ..dir1
#         python hw06_hard.py -touch ..dir1test.txt
#
#         и.т.д.
#
#     Используйте модули argparse (для разбора аргументов), os, sys.
#
#     Утилита должна принимать следующие флаги и выполнять следующие действия
#     -ls путь до папки - Посмотреть все файлы и подпапки в папке
#     -touch путь до нового файла - Создать файл
#     -rm путь до файла - Удалить файл
#     -mkdir путь до папки - Создать папку
#
#     Каждый из представленных параметров не обязательный, но если не указать никакой, то утилита должна вывести
#     уведомление, которая предлагает посмотреть --help.
#     Предусмотреть обработку исключений, например, если пытаются посмотреть все файлы не у папки, а у файла и.т.д.


import os
import sys
print('sys.argv = ', sys.argv)

def see_way():# ls
    print(os.getcwd())

def new_file(): #tuch
    if not file_name:
        print('Укажите имя файла вторым параметром: ')
        return
    try:
        with open('file_name','w+'):
            print('Фйайл {} -  создан'.format(file_name))
    except NameError:
        print('файл {} с таким именем уже существует'.format(file_name))

def rm_file():  #rm
    if not rm_file_name:
        print('Что удалить ?: ')
        return
    try:
        os.remove(rm_file_name)
    except FileNotFoundError:
        print('Файл не найден')

def make_dir():  #mkdir
    if not dir_name:
        print('Укажите имя директории вторым параметром: ')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.makedirs(dir_path)
        print('Директория {} - создана'.format(dir_name))
    except FileExistsError:
        print('Директори {} уже существует'.format(dir_name))

help_dict = {'touch':new_file,'rm':rm_file,'mkdir':make_dir}

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    rm_file_name = sys.argv[2]
except IndexError:
    rm_file_name = None

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None


for key in help_dict:
    if help_dict.get(key):
        help_dict[key]()
    else:
        print('введен неверный параметр ! ')
        print('Для получения справки введите -  print_help')

def print_help():
    print('help - получение справки')
    print('ls - отображение полного пути текущей директории')
    print('touch -  путь до нового файла - Создать файл')
    print('rm <file_name> - удаление файла')
    print('mkdir <dir_name> - создание директории')

# if __name__ == '__main__':
#     print('sys.argv = ', sys.argv)
#     if sys.argv[0] == 'help':
#         print_help()
#     if sys.argv[0] == 'ls':
#         see_way()
#     if sys.argv[0] == 'touch':
#         new_file()
#     if sys.argv[0] == 'rm':
#         rm_file()
#     if sys.argv[0] == 'mkdir':
#         make_dir()
















