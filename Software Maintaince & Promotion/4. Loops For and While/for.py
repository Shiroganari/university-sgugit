# Оценки по физике учеников первой группы
group_1 = [5, 5, 5, 4, 3, 4, 4]

# Оценки по физике учеников второй группы
group_2 = [2, 3, 3, 5, 4, 4, 3]


# Высчитываем средний балл по физике учеников первой группы
average_grade = 0

for grade in group_1:
    average_grade += grade

average_grade /= len(group_1)
print("Средний балл по физике учеников первой группы: ", average_grade)


# Высчитываем средний балл по физике учеников второй группы
average_grade = 0

for grade in group_2:
    average_grade += grade

average_grade /= len(group_2)
print("Средний балл по физике учеников второй группы: ", average_grade)