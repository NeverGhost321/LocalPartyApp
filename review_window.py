# review_window.py
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class ReviewWindow(QWidget):
    def __init__(self, username):
        super().__init__()

        # Настройка окна
        self.setWindowTitle(f'Оставить отзыв для {username}')
        self.setGeometry(150, 150, 300, 200)

        # Сохраняем имя пользователя
        self.username = username

        # Создаем виджеты для ввода оценок
        self.label_game = QLabel('Оцените уровень игры:')
        self.input_game = QLineEdit(self)

        self.label_friendliness = QLabel('Оцените дружелюбие:')
        self.input_friendliness = QLineEdit(self)

        self.label_language = QLabel('Оцените обращение с матами:')
        self.input_language = QLineEdit(self)

        # Кнопка для отправки отзыва
        self.submit_button = QPushButton('Отправить отзыв', self)
        self.submit_button.clicked.connect(self.submit_review)

        # Компоновка элементов интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.label_game)
        layout.addWidget(self.input_game)
        layout.addWidget(self.label_friendliness)
        layout.addWidget(self.input_friendliness)
        layout.addWidget(self.label_language)
        layout.addWidget(self.input_language)
        layout.addWidget(self.submit_button)

        # Устанавливаем компоновку
        self.setLayout(layout)

    def submit_review(self):
        try:
            # Получаем оценки из полей ввода
            game_rating = float(self.input_game.text())
            friendliness_rating = float(self.input_friendliness.text())
            language_rating = float(self.input_language.text())

            # Логика для дальнейшей обработки оценок (например, отправка в базу данных)
            # Пока просто показываем сообщение
            QMessageBox.information(self, 'Спасибо за отзыв!',
                                    f'Ваши оценки для {self.username}:\n'
                                    f'Уровень игры: {game_rating}\n'
                                    f'Дружелюбие: {friendliness_rating}\n'
                                    f'Обращение с матами: {language_rating}')
            self.close()  # Закрываем окно после отправки

        except ValueError:
            # Если введены нечисловые значения, вывести предупреждение
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите числовые значения для всех полей.')
