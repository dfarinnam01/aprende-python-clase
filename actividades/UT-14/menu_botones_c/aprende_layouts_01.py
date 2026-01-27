import sys

from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QStackedWidget


class Layout01(QWidget):
    def __init__(self):
        super().__init__()
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Aprende Layout01")
        self.resize(600, 500)
        self.crear_widgets()

    def crear_widgets(self):
        # layout_main=QHBoxLayout(self)

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)
        self.setLayout(layout_main)

        panel_menu = QWidget()
        panel_menu.setFixedHeight(50)
        panel_menu.setStyleSheet("background-color: #c71585;")
        layout_menu = QHBoxLayout()
        panel_menu.setLayout(layout_menu)

        self.panel_central = QStackedWidget()
        self.panel_central.setStyleSheet("background-color: #8B0000;")

        panel_estado = QWidget()
        panel_estado.setFixedHeight(50)
        panel_estado.setStyleSheet("background-color: #c71585;")
        layout_estado = QHBoxLayout()
        panel_estado.setLayout(layout_estado)



        layout_main.addWidget(panel_menu)
        layout_main.addWidget(self.panel_central,1)
        layout_main.addWidget(panel_estado)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Layout01()
    ventana.show()
    sys.exit(app.exec())