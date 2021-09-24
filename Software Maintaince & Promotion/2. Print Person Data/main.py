class Person:
    name = ""
    surname = ""
    age = 0
    place_of_residence = ""
    
    def __init__(self):
        print("Ваше имя?")
        self.name = input()
        
        print("Ваша фамилия?")
        self.surname = input()
        
        print("Сколько вам лет?")
        self.age = input()
        
        print("Где вы живёте?")
        self.place_of_residence = input()
        

    def display_info(self):
        print("Ваши имя и фамилия: ", self.name, " ", self.surname)
        print("Ваш возраст: ", self.age)
        print("Вы живёте в: ", self.place_of_residence)


shiroganari = Person()
shiroganari.display_info()