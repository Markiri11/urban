immutable_var = 1, 2, "apple", True, # Создали переменную и присвоили ей кортеж из нескольких элементов разных типов данных.
print(immutable_var) # Вывод кортежа на экран.
# immutable_var [0] = [123]    # Нельзя изменить значения элементов кортежа, так как кортеж используется как хранилище, в котором невозможно отредактировать или заменить.
mutable_list = [1, 2, "apple", "banana"] # Создали переменную и присвоили ей список из нескольких элементов.
mutable_list [0] = 123 # Изменили элемент из списка
mutable_list [1] = 321 # Изменили элемент из списка
mutable_list [3] = "fish" # Изменили элемент из списка
print(mutable_list) # Вывод списка на экран.
