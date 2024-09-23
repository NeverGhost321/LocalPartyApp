import sys
from PyQt6.QtWidgets import QApplication
from auth_window import AuthWindow
from main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    auth_window = AuthWindow()
    
    # Создаем основное окно
    main_window = MainWindow()  # Создаем экземпляр основного окна
    auth_window.login_success.connect(lambda: show_main_window(auth_window, main_window))  # Подключаем сигнал
    auth_window.show()

    sys.exit(app.exec())

def show_main_window(auth_window, main_window):
    print("Показ основного окна...")  # Отладочный вывод
    main_window.show()  # Показываем основное окно
    auth_window.close()  # Закрываем окно аутентификации

if __name__ == "__main__":
    main()
