from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QGridLayout, QSizePolicy
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, username="Guest", ratings={}, is_own_profile=True):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Профиль пользователя")
        self.setGeometry(100, 100, 800, 600)

        # Сохраняем имя пользователя и его оценки
        self.username = username
        self.ratings = ratings  # Словарь с оценками
        self.is_own_profile = is_own_profile  # Показываем кнопку отзыва только для чужих профилей

        # Основной макет
        grid_layout = QGridLayout()

        # -------- Левая колонка --------
        # Маленький аватар
        small_avatar_label = QLabel(self)
        small_avatar_label.setPixmap(QPixmap('avatar.png').scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        grid_layout.addWidget(small_avatar_label, 0, 0)

        # Имя пользователя
        small_username_label = QLabel(self.username, self)
        grid_layout.addWidget(small_username_label, 0, 1)

        # Список чатов
        chat_list = QListWidget(self)
        chat_list.addItems(['User 1', 'User 2', 'User 3'])  # Пример чатов
        chat_list.itemClicked.connect(self.open_chat)  # Открываем чат при клике
        grid_layout.addWidget(chat_list, 1, 0, 2, 2)

        # Кнопка для поиска пользователей
        search_button = QPushButton('Search Users', self)
        grid_layout.addWidget(search_button, 3, 0, 1, 2)

        # Кнопка "Start game"
        start_game_button = QPushButton('Start game', self)
        grid_layout.addWidget(start_game_button, 4, 0, 1, 2)  # На всю ширину

        # Кнопка "Exit"
        exit_button = QPushButton('Exit', self)
        exit_button.clicked.connect(self.exit_to_login)  # Связываем с функцией выхода
        grid_layout.addWidget(exit_button, 5, 0, 1, 2)  # На всю ширину

        # -------- Правая колонка --------
        # Здесь будет отображаться либо свой профиль, либо профиль другого пользователя
        profile_info = QLabel(self)
        profile_info.setText(f"Profile Information for {self.username}")  # Пример текста профиля
        grid_layout.addWidget(profile_info, 0, 2, 1, 1)  # Вторая колонка, первая строка

        # Кнопка "Write review" только для чужих профилей
        if not self.is_own_profile:
            write_review_button = QPushButton('Write Review', self)
            grid_layout.addWidget(write_review_button, 1, 2, 1, 1)  # Вторая колонка, вторая строка

        # Добавляем макет в главное окно
        self.setLayout(grid_layout)

    def open_chat(self, item):
        print(f"Open chat with: {item.text()}")  # Отладочный вывод

    def exit_to_login(self):
        print("Выход из системы.")  # Отладочный вывод
        self.close()  # Закрываем главное окно
