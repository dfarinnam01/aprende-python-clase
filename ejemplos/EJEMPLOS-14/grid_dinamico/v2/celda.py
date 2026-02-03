import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout


class Celda(QWidget):
    def __init__(self,titulo):
        super().__init__()
        self.titulo = titulo
        self.config_ui()
        self.crear_widget()
    def config_ui(self):
        r = random.randint(50, 200)
        g = random.randint(50, 200)
        b = random.randint(50, 200)
        self.setStyleSheet(f"""
                     QWidget {{
                         background-color:rgb({r},{g},{b});
                         border-radius:8px;
                         }}
                 """)
    def crear_widget(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel(self.titulo,self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color:#ffffff; font-size:16px; font-weight:bold;")
        label.setFixedHeight(20)
        layout.addWidget(label)

        label = QLabel("CÁMARA", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("background-color:#000000;")
        layout.addWidget(label)



