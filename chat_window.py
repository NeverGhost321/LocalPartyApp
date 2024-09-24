from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class ChatWindow(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()

        self.chat_label = QLabel(f"Чат с {username}", self)
        self.chat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chat_label.setStyleSheet("color: #ffffff; font-size: 24px;")

        layout.addWidget(self.chat_label)
        self.setLayout(layout)
