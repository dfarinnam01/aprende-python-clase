import sys

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget, QLabel


class Entradas(QWidget):
    def __init__(self):
        super().__init__()
        self.entradas=[]
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones -Entradas")
        self.setFixedSize(600, 500)
        self.crear_widgets()

    def crear_widgets(self):
        self.crear_botones_menu()
        self.panel_datos=QStackedWidget(self)
        self.panel_datos.setGeometry(0, 40, 600, 560)
        self.setStyleSheet("background-color: #E9967A")

        panel_nueva = QWidget(self.panel_datos)
        panel_nueva.setStyleSheet("background-color: #8B0000;")
        label=QLabel("Entrada",panel_nueva)
        label.move(20, 30)
        label.setStyleSheet("background-color: #ffffff;")

        panel_listado= QWidget(self.panel_datos)
        panel_listado.setStyleSheet("background-color: #aa00aa;")
        label=QLabel("Listado",panel_listado)
        label.move(20, 20)

        self.panel_datos.addWidget(panel_nueva)
        self.panel_datos.addWidget(panel_listado)
    def crear_botones_menu(self):
        panel_botones = QWidget(self)
        panel_botones.setGeometry(0,0,600,40)
        panel_botones.setStyleSheet("background-color:rgb(255,0,0);")

        self.boton_nueva=QPushButton("Nueva",panel_botones)
        self.boton_nueva.setGeometry(0,0,80,30)
        self.boton_nueva.setStyleSheet("background-color: #cccccc;"
                                       "border:1px solid black;"
                                       "padding:5px;"
                                       "border-radius:5px;")
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = QPushButton("Listado", panel_botones)
        self.boton_listado.setGeometry(100, 0, 80, 30)
        self.boton_listado.setStyleSheet("background-color: #cccccc;"
                                       "border:1px solid black;"
                                       "padding:5px;"
                                       "border-radius:5px;")
        self.boton_listado.clicked.connect(self.listado_entrada)

        self.boton_salir = QPushButton("Salir", panel_botones)
        self.boton_salir.setGeometry(200, 0, 80, 30)
        self.boton_salir.setStyleSheet("background-color: #cccccc;"
                                         "border:1px solid black;"
                                         "padding:5px;"
                                         "border-radius:5px;")
        self.boton_salir.clicked.connect(sys.exit)
    def nueva_entrada(self):
        self.panel_datos.setCurrentIndex(0)
    def listado_entrada(self):
        self.panel_datos.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana=Entradas()
    ventana.show()
    sys.exit(app.exec())