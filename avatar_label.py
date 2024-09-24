from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt

class AvatarLabel(QLabel):
    def __init__(self, avatar_path, size, parent=None):
        super().__init__(parent)
        self.size = size
        self.avatar_pixmap = QPixmap(avatar_path).scaled(self.size, self.size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
        self.update_avatar()

    def update_avatar(self):
        # Создаем QPixmap с тем же размером, что и аватар
        rounded_pixmap = QPixmap(self.size, self.size)
        rounded_pixmap.fill(Qt.GlobalColor.transparent)

        # Используем QPainter для рисования скругленного аватара
        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, self.size, self.size)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, self.size, self.size, self.avatar_pixmap)
        painter.end()

        # Устанавливаем скругленную аватарку на виджет
        self.setPixmap(rounded_pixmap)
