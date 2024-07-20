grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # Даны следующие данные
students = ('Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron') # Даны следующие данные

students_list = list(students) # Из множество превращаем в список
students_list.sort() # Этот список мы выставляем по алфавитном порядке

grades [0] =sum(grades[0]) / len(grades[0]) # Считаем средний бал каждого подсписка
grades [1] =sum(grades[1]) / len(grades[1])
grades [2] =sum(grades[2]) / len(grades[2])
grades [3] =sum(grades[3]) / len(grades[3])
grades [4] =sum(grades[4]) / len(grades[4])

dict = dict(zip(students_list, grades)) # Из списков grades и students_list мы составляем словарь, где ключом будет имя ученика, а значением - его средний балл.
print("Средний балл учеников: ",dict)

print(dict.get('Aaron')) # Проверка работоспособности кода