password = input('Введите пароль: ')

try:
    result = int(password) / 2
    print('Ваш пароль состоит только из цифр')
except:
    try:
        result = password[1]
        print('Требования к паролю соблюдены')
    except:   
        print('Вы ввели пустой пароль')

