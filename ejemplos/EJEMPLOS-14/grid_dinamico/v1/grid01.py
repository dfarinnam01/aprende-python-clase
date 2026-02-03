import random
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLabel

ROWS=4
COLS=6
CELLS_SPACING=5

class GridWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Dinámico")
        self.resize(800, 600)
        self.crear_ui()

    def crear_ui(self):
        self.panel_central = QWidget()
        self.setCentralWidget(self.panel_central)
        # self.panel_central.layout().addWidget()
        grid_layout = QGridLayout(self.panel_central)
        grid_layout.setSpacing(CELLS_SPACING)
        grid_layout.setContentsMargins(10,10,10,10)

        cell=self.crear_celda(0,0)
        grid_layout.addWidget(cell,0,0)
        cell = self.crear_celda(1, 1)
        grid_layout.addWidget(cell, 1, 1)

        for fila in range(ROWS):
            for col in range(COLS):
                cell = self.crear_celda(fila, col)
                grid_layout.addWidget(cell, fila, col)

    def crear_celda(self,fila,col):
        widget = QWidget()
        layout = QGridLayout(widget)
        layout.setContentsMargins(0,0,0,0)

        r=random.randint(50,200)
        g=random.randint(50,200)
        b = random.randint(50, 200)
        widget.setStyleSheet(f"""
            QWidget {{
                background-color:rgb({r},{g},{b});
                border-radius:8px;
                }}
        """)
        label = QLabel(f"Fila: {fila}, Col: {col}",widget)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color:#ffffff; font-size:16px; font-weight:bold;")
        layout.addWidget(label)
        return widget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec())