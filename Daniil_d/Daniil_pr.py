from easygui import *

class Human():
    def __init__(self,name,sn,age,h,ey,heirs):
        self.name = name
        self.surname = sn
        self.age = age
        self.height = h
        self.eye = ey
        self.heirs = heirs
    def getInfo(self):
        msgbox(f'''
         name: {self.name}
         surname: {self.surname}
         age: {self.age} 
         height: {self.height} 
         eye: {self.eye} nn
         heirs: {self.heirs}
         ''')



man = Human(enterbox('введите имя'),enterbox('введите фамилию'),enterbox('введите возраст'),enterbox('введите рост'),enterbox('введите цвет глаз'),enterbox('введите цвет волос'))
man.getInfo()
