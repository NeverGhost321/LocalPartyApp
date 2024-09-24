import sys
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QApplication,
    QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

class AuthWindow(QWidget):
    login_success = pyqtSignal(str)  # Передача имени пользователя при успешной авторизации

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sosi")
        self.setGeometry(100, 100, 400, 400)
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font_title = QFont('Segoe UI', 24)
        font_subtitle = QFont('Segoe UI', 16)
        font_button = QFont('Segoe UI', 10)
        font_input = QFont('Segoe UI', 14)

        self.label_subtitle = QLabel('LocalPartyChat', self)
        self.label_subtitle.setFont(font_subtitle)
        self.label_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_subtitle.setStyleSheet("color: #ffffff;")

        self.label_title = QLabel('Login', self)
        self.label_title.setFont(font_title)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setStyleSheet("color: #ffffff;")

        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText('Login')
        self.login_input.setFixedHeight(40)
        self.login_input.setStyleSheet("""
            QLineEdit {
                background-color: #222222; 
                color: #ffffff; 
                border: 1px solid #222222;  
                border-radius: 20px;  
                padding-left: 10px;  
                text-align: center;  
            }
        """)
        self.login_input.setFont(font_input)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText('Password')
        self.password_input.setFixedHeight(40)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet("""
            QLineEdit {
                background-color: #222222; 
                color: #ffffff; 
                border: 1px solid #222222; 
                border-radius: 20px;  
                padding-left: 10px;  
                text-align: center;  
            }
        """)
        self.password_input.setFont(font_input)

        self.button_login = QPushButton('Login', self)
        self.button_login.setFont(font_button)
        self.button_login.setFixedSize(150, 40)
        self.button_login.setStyleSheet("""
            QPushButton {
                background-color: #444444;  
                color: #ffffff;               
                border: none; 
                border-radius: 20px;  
            }
            QPushButton:hover {
                background-color: #555555;  
            }
        """)
        self.button_login.clicked.connect(self.on_login_clicked)

        self.button_reset = QPushButton('Reset Password', self)
        self.button_reset.setFont(font_button)
        self.button_reset.setFixedSize(120, 30)
        self.button_reset.setStyleSheet("""
            QPushButton {
                background-color: #444444;  
                color: #ffffff;               
                border: none; 
                border-radius: 20px;  
            }
            QPushButton:hover {
                background-color: #555555;  
            }
        """)
        self.button_reset.clicked.connect(self.on_reset_clicked)

        self.button_register = QPushButton('Registration', self)
        self.button_register.setFont(font_button)
        self.button_register.setFixedSize(120, 30)
        self.button_register.setStyleSheet("""
            QPushButton {
                background-color: #444444;  
                color: #ffffff;               
                border: none; 
                border-radius: 20px;  
            }
            QPushButton:hover {
                background-color: #555555;  
            }
        """)
        self.button_register.clicked.connect(self.on_register_clicked)

        layout.addWidget(self.label_subtitle)  
        layout.addWidget(self.label_title)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_input)

        layout.addWidget(self.button_login, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_reset)
        button_layout.addWidget(self.button_register)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setStyleSheet("""
            QWidget {
                background-color: #121212; 
                border-radius: 20px;  
            }
        """)

    def on_login_clicked(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if not login or not password:
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите логин и пароль.')
            return

        if login == "user" and password == "1":
            self.login_success.emit(login)  # Передача имени пользователя
        else:
            QMessageBox.warning(self, 'Ошибка', 'Неверный логин или пароль.')

    def on_reset_clicked(self):
        QMessageBox.information(self, 'Информация', 'Сброс пароля временно недоступен.')

    def on_register_clicked(self):
        QMessageBox.information(self, 'Информация', 'Регистрация временно недоступна.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    auth_window = AuthWindow()
    auth_window.show()
    sys.exit(app.exec())
