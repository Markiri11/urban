my_dict = {'Kirill': 2004, 'Katya': 1999, 'Max': 1986} # Создали переменную и присвоили словарь из нескольких пар.
print('Словарь:', my_dict) # Вывод словаря

print("Вывод по сущ. ключу", my_dict['Kirill']) # Вывод по существуюшему ключу
print(my_dict.get('Misha')) # Вывод без ошибки

my_dict.update({'Misha': 2003, 'Alex': 2000}) # Добавление новых пар
print(my_dict) # Обновленный словарь

del my_dict['Max'] # Удаляем один элемент
print(my_dict)

my_set = {1, 2, 3, False, 3, 'Max', 'Kirill', 'Max'} # Создаем переменную my_set и присвоем ей множество
print(my_set) # Выведем на экран множество (только уникальные значения)

my_set.add((4,5)) # Добавьте 2 произвольных элемента в множество
my_set.add('Множество') # Добавьте 2 произвольных элемента в множество
print(my_set) # Обновленное множество

print(my_set.remove('Kirill')) # Удаляем один эелемент Kirill
print(my_set) # Обновленное множество