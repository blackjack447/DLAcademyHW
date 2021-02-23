import os
import sys



def print_help(): 
    print('help - получение справки')
    print('ls - отображение полного пути текущей директории')
    print('touch -  путь до нового файла - Создать файл')
    print('rm <file_name> - удаление файла')
    print('mkdir <dir_name> - создание директории')


def ls():# ls
    print(os.getcwd())

def tuch(file_name): #tuch
    if not file_name:
        print('Укажите имя файла вторым параметром: ')
        return
    try:
        with open(file_name,'w+'):
            print('Фйайл {} -  создан'.format(file_name))
    except NameError:
        print('файл {} с таким именем уже существует'.format(file_name))  

def rm(rm_file_name):  #rm
    if not rm_file_name:
        print('Что удалить ? - ')
        return
    try:
        os.remove(rm_file_name)
        print('Файл {} - удален'.format(rm_file_name))
    except FileNotFoundError:
        print('Файл не найден')

def mkdir(dir_name):  #mkdir
    if not dir_name:
        print('Укажите имя директории вторым параметром: ')
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.makedirs(dir_path)
        print('Директория {} - создана'.format(dir_name))
    except FileExistsError:
        print('Директори {} уже существует'.format(dir_name))
        
a = {
    'help': print_help,
    "ls": ls,
    'tuch': tuch,
    'rm': rm,
    'mkdir': mkdir
}


if __name__== '__main__':
    print('argv =', sys.argv)
    if sys.argv[1] == 'help':
        print_help()
    elif sys.argv[1]== 'ls':
        ls()
    elif sys.argv[1] == 'tuch':
        tuch(sys.argv[2])
    elif sys.argv[1] == 'rm':
        rm(sys.argv[2])
    elif sys.argv[1] == 'mkdir':
        mkdir(sys.argv[2])        
 