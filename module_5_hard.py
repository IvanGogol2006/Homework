import hashlib
from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    @staticmethod
    def hash_password(password):
        """Хэширование пароля."""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def __repr__(self):
        return f'<User(nickname="{self.nickname}", age={self.age})>'


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return f'<Video(title="{self.title}", duration={self.duration}, adult_mode={self.adult_mode})>'


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
            return f'{ur.current_user.nickname}'

    def log_in(self, nickname, password):
        """Авторизация пользователя."""
        password_hash = User.hash_password(password)
        for user in self.users:
            if user.nickname == nickname and user.password == password_hash:
                self.current_user = user
                break
        else:
            print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        """Регистрация нового пользователя."""
        new_user = User(nickname, password, age)
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.log_in(nickname, password)

    def log_out(self):
        """Выход из аккаунта."""
        if self.current_user is not None:
            self.current_user = None
            print("Вы вышли из аккаунта.")
        else:
            print("Вы не вошли в аккаунт.")

    def add(self, *new_videos):
        """Добавление новых видео."""
        for video in new_videos:
            if any(v.title == video.title for v in self.videos):
                continue
            self.videos.append(video)


    def get_videos(self, search_word):
        """Поиск видео по ключевому слову."""
        results = [video.title for video in self.videos
            if search_word.lower() in video.title.lower()]
        return results

    def watch_video(self, title):
        """Просмотр видео."""
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print(f"Видео с названием '{title}' не найдено.")
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу.")
            return

        print(f"Секунды воспроизведения: ", end='')
        while video.time_now <= video.duration:
            print(video.time_now, end=' ')
            sleep(1)
            video.time_now += 1
        print("\nКонец видео.")
        video.time_now = 0  # Сброс времени просмотра



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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')