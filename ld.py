# Создайте список из чисел 3, 5, 7, 9 и 10.5
# Выведите содержимое списка на экран
# Добавьте в конец списка строку "Python"
# Выведите длину списка на экран

# Выведите на экран начальный элемент списка
# Выведите на экран последний элемент списка
# Напечатайте элементы списка со второго по четвертый включительно
# Удалите из списка строку "Python"

numbers = [3, 5, 7, 9, 10.5]
numbers.append('Python')
print(numbers)
numbers_count = len(numbers)
print(numbers_count)

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
del numbers[-1]
print(numbers)
