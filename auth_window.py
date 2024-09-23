from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class AuthWindow(QWidget):
    login_success = pyqtSignal()  # Сигнал для успешного логина

    def __init__(self):
        super().__init__()

        # Настройка окна
        self.setWindowTitle("Sosi")
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(400, 400)

        # Основной макет для элементов
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Стили и шрифты
        font_title = QFont('Arial', 16)
        font_button = QFont('Arial', 12)

        # Создаем заголовок "Login"
        self.label_title = QLabel('Login', self)
        self.label_title.setFont(font_title)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setStyleSheet("color: #ffffff;")

        # Поле для ввода логина
        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText('Login')
        self.login_input.setFixedHeight(30)

        # Поле для ввода пароля
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setFixedHeight(30)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        # Кнопка "Login"
        self.button_login = QPushButton('Login', self)
        self.button_login.setFont(font_button)
        self.button_login.setFixedSize(150, 30)
        self.button_login.setStyleSheet("""
            background-color: #1a1a1a;  
            color: #ffffff;               
            border: 1px solid #cccccc;    
        """)
        self.button_login.clicked.connect(self.on_login_clicked)  # Подключаем обработчик

        # Кнопка "Reset password"
        self.button_reset = QPushButton('Reset password', self)
        self.button_reset.setFont(font_button)
        self.button_reset.setFixedSize(150, 30)
        self.button_reset.setStyleSheet("""
            background-color: #1a1a1a;  
            color: #ffffff;               
            border: 1px solid #cccccc;    
        """)

        # Кнопка "Registration"
        self.button_register = QPushButton('Registration', self)
        self.button_register.setFont(font_button)
        self.button_register.setFixedSize(150, 30)
        self.button_register.setStyleSheet("""
            background-color: #1a1a1a;  
            color: #ffffff;               
            border: 1px solid #cccccc;    
        """)

        # Добавляем элементы на макет
        layout.addWidget(self.label_title)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.button_login)

        # Добавляем вертикальные отступы
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        layout.addWidget(self.button_reset)
        layout.addWidget(self.button_register)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #000000; 
            }
            QLineEdit {
                background-color: #333333; 
                color: #ffffff; 
                border: 1px solid #ffffff; 
            }
        """)

    def on_login_clicked(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login or not password:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите логин и пароль.')
            return

        # Пример проверки логина и пароля
        if login == "user" and password == "pass":  # Замените на вашу логику
            print("Успешный вход.")  # Отладочный вывод
            self.login_success.emit()  # Генерируем сигнал успешного входа
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль.')

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec())
