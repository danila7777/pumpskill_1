student = {'first_name': 'Иван', 'cities': ['Лондон', 'Париж', 'Нью Йорк']}

print(student['first_name'])                  # Иван
print(f"посещал города: {student['cities']}") # посещал города: ['Лондон', 'Париж', 'Нью Йорк']

student['birthday'] = '23 июля'
student['birthday'] = '24 августа'
print(student) 