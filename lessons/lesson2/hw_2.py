# ''' Реализуйте базовый класс Car.
# У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Реализовать метод для user-friendly вывода информации об автомобиле.'''
#
#
# class Car:
#     def __init__(self, speed, color, name, is_police, direction, current_speed):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         self.direction = direction
#         self.current_speed = current_speed
#
#     def __bool__(self):
#         return self.is_police == "Police car"
#
#     def go(self):
#         print("The car started moving")
#
#     def stop(self):
#         print("The car has stopped")
#
#     def turn(self):
#         print("The car turned " + self.direction)
#
#     def show_speed(self):
#         print("Current car's speed is" + self.current_speed)
#
#
# class TownCar(Car):
#     def restriction(self):
#         if self.current_speed > '40':
#             print("You have exceeded speed limit ")
#         else:
#             print("Have a safe way")
#
#
# class WorkCar(Car):
#     def restriction(self):
#         if self.current_speed > '60':
#             print("You have exceeded speed limit ")
#         else:
#             print("Have a safe way")
#
#
# a = WorkCar(40, "black", "jack", "no", "left", "50")
# a.restriction()


# Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
# создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
# оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
# полем.
# У заявки должны быть следующие методы:
# - метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
# - метод, изменяющий статус заявки
# - метод, возвращающий id заявки


# class Application:
#     __class_counter = 0
#
#     def __init__(self, name, equipment_id, status):
#         self.name = name
#         self.equipment_id = equipment_id
#         self.status = status
#         self.id = Application.__class_counter
#         Application.__class_counter += 1
#         import datetime
#         dt_now = datetime.datetime.now()
#         print(dt_now)
#
#     def call(self):
#         print(Application.__class_counter)
#
#     def status_change(self):
#         from datetime import time
#         now = dt_now.now(Application)
#         print( now - dt_now(Application))
#
# a = Application("ddd", 65, "active")
# a.call()
# b = Application("ddd", 65, "active")
# b.status_change()


class Matrices:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def display(self,C):
        print('Resultant Matrix is:')
        for i in range(0, m):
            print('\n')
            for j in range(0, n):
                print(' {}'.format(C[i][j]), end=" ")
    def Add(self,C):
        for i in range(0, m):
            for j in range(0, n):
                C[i][j] = A[i][j] + B[i][j]
    def Sub(self, C):
        for i in range(0, m):
            for j in range(0, n):
                C[i][j] = A[i][j] - B[i][j]
    def Mul(self, C):
        for i in range(0, m):
            for j in range(0, q):
                for k in range(0, n):
                    C[i][j] += A[i][k] * B[k][j]


if __name__ == '__main__':
    m = int(input('Enter no. of rows for Matrix 1:'))
    n = int(input('Enter no. of columns for Matrix 1:'))
    A = [[0 for j in range(0, n)] for i in range(0, m)]
    print('Enter Elements of Matrix A')
    for i in range(0, m):
        for j in range(0, n):
            A[i][j] = int(input('Enter element A{}{}:'.format(i, j)))
    p = int(input('Enter no. of rows for Matrix 2:'))
    q = int(input('Enter no. of columns for Matrix 2:'))
    B = [[0 for j in range(0, q)] for i in range(0, p)]
    print('Enter Elements of Matrix B')
    for i in range(0, p):
        for j in range(0, q):
            B[i][j] = int(input('Enter element B{}{}:'.format(i, j)))
    obj = Matrices(A,B)
    var = 1
    while var != '0':
        print('1.Add Matrices\n2.Subtract Matrices\n3.Multiply Matrices\n4.Exit')
        choice = int(input('Enter Choice:'))
        if choice == 1:
            if m == p and n == q:
                print('Matrices can be Added')
                C = [[0 for j in range(0, n)] for i in range(0, m)]
                obj.Add(C)
                obj.display(C)
            else:
                print('Matrices cannot be Added')
        elif choice == 2:
            if m == p and n == q:
                print('Matrices can be Subtracted')
                C = [[0 for j in range(0, n)] for i in range(0, m)]
                obj.Sub(C)
                obj.display(C)
            else:
                print('Matrices cannot be Subtracted')
        elif choice == 3:
            if n == p:
                print('Matrices can be Multiplied')
                C = [[0 for j in range(0, q)] for i in range(0, m)]
                obj.Mul(C)
                obj.display(C)
            else:
                print('Matrices cannot be Multiplied')
        elif choice == 4:
            exit(0)
        else:
            print('\nPlease enter a valid choice')
        var = (input('\nDo you want to Continue?(press 0 to stop)'))

class Matrix:
    def __init__(self, list_1, list_2):
        # self.matr = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))



my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())