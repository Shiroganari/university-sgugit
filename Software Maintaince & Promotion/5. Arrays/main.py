# Нахождение наименьшего нечетного элемента в массиве
A = [10, 11, 15, 6, 3, 7, 4]
smallest_odd = 100000

for num in A:
    if (num % 2 != 0) and num < smallest_odd:
        smallest_odd = num
        
print("Наименьшее нечетное число: ", smallest_odd)
print("")


# Поменять массивы местами
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Массив A изначально: ", A)
print("Массив B изначально: ", B)

for index in range(0, 10):
    temp = A[index]
    A[index] = B[index]
    B[index] = temp

print("Массив A после перестановки: ", A)
print("Массив B после перестановки: ", B)