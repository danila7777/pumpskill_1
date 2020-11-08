city_list = ['Москва', 100, 'Париж', 200, 'Лондон', 300, 'Нью Йорк', 400]

message1 = f'Население города {city_list[0]} = {city_list[1]}'
message2 = f'Население городов {city_list[2]} и {city_list[4]} = {city_list[3]+city_list[5]}'

print(message1) # Население города Москва = 100
print(message2) # Население городов Париж и Лондон = 500

len(city_list) # 8

city_list_2 = []
city_list_2.append('Москва')

a = input('Введите новый город: ')
city_list_2.append(a)
city_list_2.append(input('Введите новый город 2: '))

print(city_list_2) 
print(f'Выбранные города: {city_list_2[0]}, {city_list_2[1]}')

b = input('Какой город удалить? ')
city_list_2.remove(b)

print(city_list_2) 

c = input('Какой номер города удалить? ')
c = int(c) - 1
c = city_list_2[c]
city_list_2.remove(c)

print(city_list_2) 
