from time import sleep


class User:
    def __init__(self, username, password, age):
        self.username: str = username
        self.password: int = hash(password)
        self.age: int = age


class Video:
    time_now: int = 0
    def __init__(self, title, duration, adult_mode=False):
        self.title: str = title
        self.duration: int = duration
        self.adult_mode: bool = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None
    def log_in(self, username, password):
        for i in self.users:
            if username == i.username:
                if hash(password) == i.password:
                    self.current_user = i

    def register(self, nickname, password, age):
        if self.users:  # если список пользователей не пустой
            for i in self.users:
                if i.username == nickname:
                    print(f"Пользователь {nickname} уже существует")
                    break
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for i in videos:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, search_title):
        search_data = []
        for i in self.videos:
            if search_title.lower() in i.title.lower():
                search_data.append(i.title)
        return search_data

    def watch_video(self, title):
        if self.current_user:  # если вход совершён
            if self.current_user.age >= 18:
                for i in self.videos:
                    if title == i.title:
                        while i.time_now < i.duration:
                            sleep(1)
                            i.time_now += 1
                            print(i.time_now, end=' ', flush=False)
                        print("Конец видео")
            else:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user.username)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
