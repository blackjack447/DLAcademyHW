# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname

    def get_short_name(self):
        return f'{self.surname.title()} {self.name[0].upper()}.{self.patronymic[0].upper()}'

class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, class_room):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.class_room = class_room

    def get_class_room(self):
        return self.class_room

    def get_parents(self):
        return self.dad.get_full_name(), self.mom.get_full_name()

class Teacher(People):
    def __init__(self, name, patronymic, surname, subject,classes):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
        self.classes = classes

    def get_subject(self):
        return self.subject

    def get_classes(self):
        return self.classes

class Class_rooms(Teacher):
    def __init__(self, teachers):
        self.teachersdict = {t.subject: t for t in teachers}

if __name__ == '__main__':
    class_rooms = ['11 А', '11 Б', '10 А']
    teachers = [Teacher('Федор', 'Васильевич', 'Иванов', 'Математика',[class_rooms[0], class_rooms[1]]),
                Teacher('Аркадий', 'Григорьевич', 'Петров', 'Литература',[class_rooms[2], class_rooms[1]]),
                Teacher('Степан', 'Юрьевич', 'Сидоров', 'Физика',[class_rooms[0], class_rooms[2]]),
                Teacher('Станислав', 'Сергеевич', 'Дмитриев', 'История',[class_rooms[1], class_rooms[0]]),
                Teacher('Николай', 'Даниилович', 'Никишин', 'Биология',[class_rooms[1], class_rooms[2]])]
    classes = [Class_rooms([teachers[0], teachers[1], teachers[2]]),
                Class_rooms([teachers[1], teachers[3], teachers[4]]),
                Class_rooms([teachers[3], teachers[1], teachers[0]])]
    parents = [People('Семен', 'Анатольевич', 'Семенов'),
                People('Ирина', 'Савельевна', 'Семенова'),
                People('Роман', 'Евгеньевич', 'Романов'),
                People('Римма', 'Тангизовна', 'Романова'),
                People('Сергей', 'Петрович', 'Сергеев'),
                People('Юлия', 'Викторвна', 'Сергеева')]
    students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], class_rooms[0]),
                Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], class_rooms[1]),
                Student('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], class_rooms[2])]

    # 1. Получить полный список всех классов школы
    st = set([i.get_class_room() for i in students])
    print('В школе есть классы:', ",".join(map(str,class_rooms)))

    # 2. Получить список всех учеников в указанном классе
    cl_room = '11 А'
    st_list = [i.get_short_name() for i in students if i.get_class_room() == cl_room]
    print(f'В {cl_room} классе  учится -', ",".join(map(str,st_list)))

    # 3. Получить список всех предметов указанного ученика
    #  (Ученик --> Класс --> Учителя --> Предметы)
    student = students[0]
    t_list = [i for i in teachers if student.get_class_room() in i.get_classes()]
    t_names = [i.get_full_name() for i in t_list]
    subj_list = [i for i in teachers if student.get_class_room() in i.get_classes()]
    subj = [i.get_subject() for i in subj_list]
    print(f'Ученик {student.get_full_name()} учится в {student.get_class_room()} у преподавателей - {",".join(map(str, t_names))} и изучает следующие предметы - {",".join(map(str,subj))}')

    # 4. Узнать ФИО родителей указанного ученика
    student = students[0]
    student_name = student.get_full_name()
    his_parents = student.get_parents()
    print(f'Родителей ученика {student_name} зовут - ',",".join(map(str, his_parents)))

    # 5. Получить список всех Учителей, преподающих в указанном классе
    teach_list = [i.get_full_name() for i in teachers if cl_room in i.get_classes()]
    print(f'В {cl_room} преподают следующие учетеля - ',",".join(map(str,teach_list)))


