account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

key = input('Введите ключ (name или account): ')
key = key.lower()

i = 1
while i <= 1:
    current_account = 'account' + str(i) + "['login'].lower()" 
    print(current_account)
    # account1['login'].lower()
    if key == current_account:
        print(user1)
    else:
        if key == user1['name'].lower():
            print(user1)
        else: 
            print('Введенный ключ не найден')
    i = i + 1
