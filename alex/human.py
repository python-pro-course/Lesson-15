from easygui import  *
class Human:
    def __init__(self,name,secondname,age,rost,eyes_color,hair_color):
        self.name = name
        self.secondname = secondname
        self.age = age
        self.rost = rost
        self.eyes_color = eyes_color
        self.hair_color = hair_color
    def getinfo(self):
        msgbox(f"Имя: {self.name}\n"
               f"Фамилия: {self.secondname}\n"
               f"Возраст: {self.age}\n"
               f"Рост: {self.rost}\n"
               f"Цвет глаз: {self.eyes_color}\n"
               f"Цвет волос: {self.hair_color}\n")

human_name = enterbox("Введите свое имя")
human_secondname = enterbox("Введите свою фамилию")
human_age = enterbox("Введите свой возраст")
human_rost = enterbox("Введите свой рост")
human_eyes_color = enterbox("Введите свой цвет глаз")
human_hair_color = enterbox("Введите свой цвет волос")
the_human = Human(human_name, human_secondname, human_age, human_rost, human_eyes_color, human_hair_color)
the_human.getinfo()