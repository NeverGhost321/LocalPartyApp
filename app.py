import sys
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow
from main_window import MainWindow


def show_main_window(auth_window):
    main_window = MainWindow()  # Создаем основное окно
    main_window.show()  # Показываем основное окно
    auth_window.close()  # Закрываем окно аутентификации


def main():
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    auth_window.login_success.connect(lambda: show_main_window(auth_window))  # Подключаем сигнал к функции
    auth_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
