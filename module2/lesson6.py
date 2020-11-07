str_length = len("абвгд")
print('Длина строки ' + str(str_length)) # 5

#

sentence = "Первое Второе И Салат"

print(sentence.upper()) # ПЕРВОЕ ВТОРОЕ И САЛАТ
print(sentence.lower()) # первое второе и салат

#

print("Первое Второе И Салат".upper()) # ПЕРВОЕ ВТОРОЕ И САЛАТ
print("Первое Второе И Салат".lower()) # первое второе и салат

#

last_name = "Иванов"
first_name = "Иван"
age = 38

print("Клиенту с фамилией {} и именем {} {} лет".format(last_name, first_name, age))
# Клиенту с фамилией Иванов и именем Иван 38 лет

result = f'Клиенту с фамилией {last_name} и именем {first_name} {age} лет'

print(result)
# Клиенту с фамилией Иванов и именем Иван 38 лет
