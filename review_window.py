from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIntValidator

class ReviewWindow(QWidget):
    rating_submitted = pyqtSignal(float)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Оценка профиля")
        self.setFixedSize(300, 200)

        self.setStyleSheet("""
            QWidget {
                background-color: #333333; 
                color: #ffffff;
                border-radius: 10px;
                background-image: url('bg_review.png');  /* Фон для окна оценки */
                background-position: center;
                background-repeat: no-repeat;
            }
        """)

        layout = QVBoxLayout()

        self.label = QLabel("Введите оценку (1-5):", self)
        layout.addWidget(self.label)

        self.rating_input = QLineEdit(self)
        self.rating_input.setValidator(QIntValidator(1, 5))  # Ввод только цифр от 1 до 5
        layout.addWidget(self.rating_input)

        self.submit_button = QPushButton("Подтвердить", self)
        self.submit_button.clicked.connect(self.submit_rating)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_rating(self):
        try:
            rating = float(self.rating_input.text())
            self.rating_submitted.emit(rating)
            self.close()
        except ValueError:
            pass  # Игнорируем ошибку
