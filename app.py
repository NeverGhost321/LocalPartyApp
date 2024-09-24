import sys
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    
    # Создание главного окна
    main_window = MainWindow()

    # Передача имени пользователя в главное окно при успешной авторизации
    auth_window.login_success.connect(lambda username: show_main_window(auth_window, main_window, username))
    
    auth_window.show()

    sys.exit(app.exec())

def show_main_window(auth_window, main_window, username):
    main_window.update_profile(username)
    main_window.show()
    auth_window.close()

if __name__ == "__main__":
    main()
