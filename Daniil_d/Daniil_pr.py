class Human():
    def __init__(self,name,sn,age,h,ey,heirs):
        self.name = name
        self.surname = sn
        self.age = age
        self.height = h
        self.eye = ey
        self.heirs = heirs
    def getInfo(self):
        print(self.name, self.surname, self.age, self.height, self.eye, self.heirs)

man = Human(input(),input(),input(),input(),input(),input())
man.getInfo()
