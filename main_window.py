import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem, QFrame, QStackedWidget
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from review_window import ReviewWindow
from avatar_label import AvatarLabel
from chat_window import ChatWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 1000, 600)
        self.setFixedSize(1000, 600)

        layout = QHBoxLayout()

        # Левая колонка с блоком чатов, занимающая 1/3 ширины страницы
        self.left_column = QFrame(self)
        self.left_column.setStyleSheet("background-color: #222222; border-radius: 10px; padding: 10px;")
        self.left_column.setFixedWidth(self.width() // 3)
        self.left_column_layout = QVBoxLayout(self.left_column)

        # Мини-профиль пользователя над блоком чатов
        self.mini_profile = QFrame(self.left_column)
        self.mini_profile_layout = QHBoxLayout(self.mini_profile)

        # Аватар в мини-профиле (увеличен до 60px)
        self.mini_avatar = AvatarLabel("avatar.png", 60, self)
        self.mini_profile_layout.addWidget(self.mini_avatar)

        # Имя пользователя в мини-профиле (увеличен размер текста)
        self.username_label = QLabel("Имя пользователя", self)
        self.username_label.setStyleSheet("color: #ffffff; font-size: 18px;")
        self.mini_profile_layout.addWidget(self.username_label)

        self.mini_profile.mousePressEvent = self.show_profile  # Клик по мини-профилю возвращает профиль
        self.left_column_layout.addWidget(self.mini_profile)

        # Список чатов с аватарами пользователей (увеличены аватары и размер текста)
        self.chat_list = QListWidget(self.left_column)
        self.chat_list.setStyleSheet("""
            QListWidget {
                background-color: #333333;
                color: #ffffff;
                border-radius: 10px;
                padding: 10px;
            }
            QListWidget::item {
                padding: 10px;
            }
        """)

        for i in range(10):
            item = QListWidgetItem(f"Пользователь {i + 1}")
            icon = QIcon(QPixmap("avatar.png").scaled(40, 40))  # Аватары размером 40x40
            item.setIcon(icon)
            self.chat_list.addItem(item)

        self.chat_list.itemClicked.connect(self.open_chat_window)
        self.left_column_layout.addWidget(self.chat_list)

        # Правая колонка с большим профилем и рейтингом
        self.right_column = QFrame(self)
        self.right_column.setStyleSheet("""
            QFrame {
                background-color: #222222; 
                border-radius: 10px;
                background-image: url('bg.png');
                background-position: center;
                background-repeat: no-repeat;
            }
        """)
        self.right_column_layout = QVBoxLayout(self.right_column)

        # Большой профиль пользователя
        self.profile_header = QFrame(self.right_column)
        profile_header_layout = QHBoxLayout(self.profile_header)

        self.avatar = AvatarLabel("avatar.png", 120, self)
        profile_header_layout.addWidget(self.avatar)

        self.profile_name = QLabel("Имя пользователя", self)
        self.profile_name.setStyleSheet("color: #ffffff; font-size: 24px;")
        profile_header_layout.addWidget(self.profile_name)

        self.right_column_layout.addWidget(self.profile_header)

        # Оценка пользователя
        self.user_rating = QLabel("Рейтинг: 4.8", self)
        self.user_rating.setStyleSheet("color: #ffffff; font-size: 18px;")
        self.right_column_layout.addWidget(self.user_rating)

        # Кнопка "Оценить"
        self.rate_button = QPushButton("Оценить", self)
        self.rate_button.setFixedSize(150, 40)
        self.rate_button.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)
        self.rate_button.clicked.connect(self.open_review_window)
        self.right_column_layout.addWidget(self.rate_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Кнопка выхода
        self.logout_button = QPushButton("Выйти", self)
        self.logout_button.setFixedSize(100, 40)
        self.logout_button.setStyleSheet("""
            QPushButton {
                background-color: #444444;
                color: #ffffff;
                border-radius: 20px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)
        self.right_column_layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignBottom)

        layout.addWidget(self.left_column)
        layout.addWidget(self.right_column)

        self.setLayout(layout)

    def open_review_window(self):
        self.review_window = ReviewWindow(self)
        self.review_window.rating_submitted.connect(self.update_rating)
        self.review_window.show()

    def update_rating(self, rating):
        self.user_rating.setText(f"Рейтинг: {rating:.1f}")

    def update_profile(self, username):
        self.username_label.setText(username)
        self.profile_name.setText(username)

    def open_chat_window(self, item):
        # Удаляем все виджеты из правой колонки
        for i in reversed(range(self.right_column_layout.count())):
            widget_to_remove = self.right_column_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        # Добавляем виджет чата вместо профиля
        chat_window = ChatWindow(item.text(), self)
        self.right_column_layout.addWidget(chat_window)

    def show_profile(self, event=None):
        # Восстанавливаем большой профиль
        for i in reversed(range(self.right_column_layout.count())):
            widget_to_remove = self.right_column_layout.itemAt(i).widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()

        self.right_column_layout.addWidget(self.profile_header)
        self.right_column_layout.addWidget(self.user_rating)
        self.right_column_layout.addWidget(self.rate_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.right_column_layout.addWidget(self.logout_button, alignment=Qt.AlignmentFlag.AlignBottom)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
