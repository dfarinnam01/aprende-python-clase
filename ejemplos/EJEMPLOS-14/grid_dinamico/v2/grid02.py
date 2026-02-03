import random
import sys
from celda import Celda

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

        # cell=self.crear_celda(0,0)
        # grid_layout.addWidget(cell,0,0)
        # cell = self.crear_celda(1, 1)
        # grid_layout.addWidget(cell, 1, 1)

        for fila in range(ROWS):
            for col in range(COLS):
                cell = Celda(f"fila{fila}, col{col}")
                grid_layout.addWidget(cell, fila, col)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GridWindow()
    window.show()
    sys.exit(app.exec())