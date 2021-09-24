class Student:
    name = ""
    surname = ""
    email = ""
    faculty = ""
    group = ""
    year_of_study = 0

    def __init__(self, name, surname, email, faculty, group, year_of_study):
        self.name = name
        self.surname = surname
        self.email = email
        self.faculty = faculty
        self.group = group
        self.year_of_study = year_of_study

    def display_info(self):
        print("Имя: ", self.name)
        print("Фамилия: ", self.surname)
        print("Электронная почта: ", self.email)
        print("Факультет: ", self.faculty)
        print("Группа: ", self.group)
        print("Курс: ", self.year_of_study)


shiroganari = Student("Вячеслав", "Тюрин", "shiroganari@gmail.com",
                      "Информационные системы и технологии",
                      "БИ - 33", "3 курс");
shiroganari.display_info();