class Numbers:
    x = 0
    y = 0
    arithmetic_mean = 0
    geometric_mean = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def find_arithmetic_mean(self):
        self.arithmetic_mean = (self.x + self.y) / 2
        return self.arithmetic_mean
    
    def find_geometric_mean(self):
        self.geometric_mean = pow(self.x * self.y, 1 / 2)
        return self.geometric_mean
        

geometric_answer = Numbers(1.2, 2.5)
arithmetic_answer = Numbers(-5.4, 10.2)


if (geometric_answer.x > 0 and geometric_answer.y > 0) or (geometric_answer.x < 0 and geometric_answer.y < 0):
    print("Среднее геометрическое чисел ", geometric_answer.x, " и ", geometric_answer.y, " = ",
          geometric_answer.find_geometric_mean())
else:
    print("Среднее арифметическое чисел ", geometric_answer.x, " и ", geometric_answer.y, " = ",
          geometric_answer.find_arithmetic_mean())


if (arithmetic_answer.x > 0 and arithmetic_answer.y > 0) or (arithmetic_answer.x < 0 and arithmetic_answer.y < 0):
    print("Среднее геометрическое чисел ", arithmetic_answer.x, " и ", arithmetic_answer.y, " = ",
          arithmetic_answer.find_geometric_mean())
else:
    print("Среднее арифметическое чисел ", arithmetic_answer.x, " и ", arithmetic_answer.y, " = ",
          arithmetic_answer.find_arithmetic_mean())