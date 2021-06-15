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


# class Matrix():
#     def __init__(self, list_of_lists1, list_of_lists2, list_of_lists3):
#         self.list_of_lists = list(list_of_lists1)
#         self.list_of_lists2 = list(list_of_lists2)
#         self.list_of_lists3 = list(list_of_lists3)
#
#
# a = Matrix([1, 2, 4], [2], [3])

