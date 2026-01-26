import sys

from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget, QLabel, QLineEdit
from ui import BotonMenu , LabelItem, EditItem

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
        label=LabelItem("Entrada",panel_nueva)
        label.move(20, 30)

        self.edit_entrada=EditItem(panel_nueva)
        self.edit_entrada.setGeometry(20, 60,150,30)

        boton_guardar = QPushButton("Guardar",panel_nueva)
        boton_guardar.setGeometry(200, 60,80,30)
        boton_guardar.clicked.connect(self.guardar)

        panel_listado= QWidget(self.panel_datos)
        panel_listado.setStyleSheet("background-color: #aa00aa;")
        label=LabelItem("Listado",panel_listado)
        label.move(20, 20)

        self.panel_datos.addWidget(panel_nueva)
        self.panel_datos.addWidget(panel_listado)
    def crear_botones_menu(self):
        panel_botones = QWidget(self)
        panel_botones.setGeometry(0,0,600,40)
        panel_botones.setStyleSheet("background-color:rgb(255,0,0);")

        self.boton_nueva=BotonMenu("Nueva",panel_botones)
        self.boton_nueva.setGeometry(0,0,80,30)
        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_botones)
        self.boton_listado.setGeometry(100, 0, 80, 30)
        self.boton_listado.clicked.connect(self.listado_entrada)

        self.boton_salir = BotonMenu("Salir", panel_botones)
        self.boton_salir.setGeometry(200, 0, 80, 30)
        self.boton_salir.clicked.connect(self.cerrar_app)

    def nueva_entrada(self):
        self.panel_datos.setCurrentIndex(0)
        self.boton_nueva.setChecked(True)
        self.boton_listado.setChecked(False)
    def listado_entrada(self):
        self.panel_datos.setCurrentIndex(1)
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(True)
    def cerrar_app(self):
        sys.exit()
    def guardar(self):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana=Entradas()
    ventana.show()
    sys.exit(app.exec())