class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, имеющий атрибуты: логин, пароль
    """
    def __init__(self, username, password, password_confirm):
        check_of_password = {'number': 0, 'character upper': 0, 'length of password': 0}
        for i in password:
            if i.isnumeric():
                check_of_password['number'] = 1
            if i.isupper():
                check_of_password['character upper'] = 1
        if len(password) >= 8:
            check_of_password['length of password'] = 1
        if sum(check_of_password.values()) != 3:
            print('Пароль не удовлетворяет условиям')
            if password_confirm == password:
                self.username = username
                self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice == 1:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choice == 2:
            user = User(input("Введите логин: "), password1 := input("Введите пароль: "),
                        password2 := input("Повторите пароль: "))
            if password1 != password2:
                print('Пароли не совпадают, попробуете ещй раз')
                continue
            database.add_user(user.username, user.password)
        print(database.data)
