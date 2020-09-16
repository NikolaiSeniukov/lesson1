# Создайте словарь:
# {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
# Уменьшите значение "temperature" на 5
# Выведите на экран весь словарь

# Проверьте, есть ли в словаре ключ country
# Выведите значение по-умолчанию "Россия" для ключа country
# Добавьте в словарь элемент date со значением "27.05.2019"
# Выведите на экран длину словаря

towntemp = {
    'city': 'Москва',
    'temperature': '20'
     }
print(towntemp['city'])
towntemp['temperature'] = towntemp['temperature'] = 15
print(towntemp['temperature'])

print(towntemp.get('country', 'Россия'))
towntemp['date'] = '27.05.2019'
print(towntemp)

print(len(towntemp))
