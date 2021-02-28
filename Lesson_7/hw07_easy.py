# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt

class Triangel():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Площадь треугольника
    def triangel_square(self):
        p = (self.a + self.b + self.c) / 2 #находим полупериметр
        print(f'Полупериметр треугольника равен - {p}')
        square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) # находим площадь по формуле Герона
        print(f'Площадь треугольника равна - {round(square,2)}')

# Высота треугольника
    def triangel_height(self):
        p = (self.a + self.b + self.c) / 2 #находим полупериметр
        square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)) # находим площадь по формуле Герона
        height = (2 * square) / self.a # находим высоту через сторону и площадь
        print(f'Высота треугольника равна - {round(height,2)}')

#Периметр треугольника
    def triangel_perimetr(self):
        p = self.a + self.b + self.a
        print('Периметр треугольника равен - ',p )

tri = Triangel(10,10,10)
tri.triangel_square()
tri.triangel_height()
tri.triangel_perimetr()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

