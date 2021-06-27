"""1. Реализовать функцию, которая на вход принимает целое положительное число n и возвращает при вызове
 объект-генератор, который по запросу будет возвращать значение факториала всех чисел от 0 до n.
 5! = 1 * 2 * 3 * 4 * 5
 2. Создайте абстрактный класс «Оргтехника», который будет базовым для классов-наследников.
 Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс и т.д.). В базовом классе определите абстрактные
 методы, общие для приведённых типов. В классах-наследниках реализуйте их, а также добавьте уникальные для каждого
 типа оргтехники функциональные возможности.
 Также создайте класс «Склад», экземпляр которого будет способен принимать в себя объекты техники на хранение.
 Организуйте для него протокол итерации (чтобы объекты вашего склада можно было бы перебирать).
"""

# def factorial(n):
#     fact = int (1)
#     for num in range(2, n + 1):
#         fact *= num
#     yield print(fact)
#
# next(factorial(5))


# from abc import ABC, abstractmethod, ABCMeta
# from os import system
#
#
# class Equipment(ABC):
#
#     @abstractmethod
#     def printer_method(self):
#         print("Это отделение принтеров")
#
#     @abstractmethod
#     def scanner_method(self):
#         print("Это отдел сканнеров")
#
#     @abstractmethod
#     def xerox_1_method(self):
#         print("Это отдел ксерокопии")
#
#
# class Printer(Equipment):
#     def printed_method(self):
#         super().printer_method()
#
#     def __init__(self, status):
#         self.status = status
#         print("The current status of printer: " + self.status)
#
#
# class Scanner(Equipment):
#     def scanned_method(self):
#         super().scanner_method()
#
#     def __init__(self, status):
#         self.status = status
#         print("The current status of scanner: " + self.status)
#
#
# class Xerox(Equipment):
#     def xerox_method(self):
#         super().xerox_1_method()
#
#     def __init__(self, status):
#         self.status = status
#         print("The current status of xerox: " + self.status)
#
#
# class My_store(Equipment):
#     def __init__(self, my_type, my_status,):
#         self.my_type = my_type
#         self.my_status = my_status
#
#     def __iter__(self):
#         return iter(self.my_type, self.my_status)

