from easygui import *

class Human:
    def __init__(self, name, surname, age, height, eye_color, hair_color):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.eye_color = eye_color
        self.hair_color = hair_color

    def get_info(self):
        msgbox(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Возраст: {self.age}\n'
               f'Цвет глаз: {self.eye_color}\n')


user_name = enterbox('Введите свое имя')
user_surname = enterbox('Введите свою фамилию')
user_age = enterbox('Введите возраст')
user_eye_color = enterbox('Введите свой цвет глаз')

user = Human(user_name, user_surname, user_age, 167, user_eye_color, 'Русый')
user.get_info()