import sys

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget, QLabel, QLineEdit, QVBoxLayout, \
    QHBoxLayout
from ui import BotonMenu , LabelItem, EditItem,BotonAction

class Entradas(QWidget):
    def __init__(self):
        super().__init__()
        self.entradas=[]
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones -Entradas")
        self.resize(600, 500)
        self.crear_widgets()

    def crear_widgets(self):

        layout_main = QVBoxLayout()
        layout_main.setContentsMargins(0, 0, 0, 0)
        layout_main.setSpacing(0)
        self.setLayout(layout_main)

        panel_menu = QWidget()
        panel_menu.setFixedHeight(50)
        panel_menu.setStyleSheet("background-color: #c71585;")
        self.crear_menu(panel_menu)

        self.panel_central = QStackedWidget()
        self.panel_central.setStyleSheet("background-color: #8B0000;")
        self.crear_widgets_entrada(self.panel_central)
        self.crear_widgets_listado(self.panel_central)

        panel_estado = QWidget()
        panel_estado.setFixedHeight(50)
        panel_estado.setStyleSheet("background-color: #c71585;")

        layout_main.addWidget(panel_menu)
        layout_main.addWidget(self.panel_central,1)
        layout_main.addWidget(panel_estado)

    def crear_widgets_entrada(self,panel_central):
        panel_nueva = QWidget()
        #panel_nueva.setStyleSheet("background-color: #8B0000;")

        layout_panel_nueva = QVBoxLayout(panel_nueva)
        layout_panel_nueva.setContentsMargins(0, 0, 0, 0)
        layout_panel_nueva.setSpacing(15)

        layout_panel_nueva.addStretch(1)
        layout_fila_entrada = QHBoxLayout()
        layout_fila_entrada.setSpacing(10)

        label = LabelItem("Entrada")
        self.edit_entrada = EditItem()
        self.edit_entrada.setFixedWidth(200)


        layout_fila_entrada.addStretch(1)
        layout_fila_entrada.addWidget(label)
        layout_fila_entrada.addWidget(self.edit_entrada)
        layout_fila_entrada.addStretch(1)

        layout_panel_nueva.addLayout(layout_fila_entrada)

        layout_fila_entrada.addStretch(1)

        boton_layout = QHBoxLayout()
        boton_guardar = BotonAction("Guardar")
        boton_guardar.setFixedWidth(100)
        boton_guardar.clicked.connect(self.guardar)
        boton_layout.addStretch(1)
        boton_layout.addWidget(boton_guardar)

        layout_panel_nueva.addLayout(boton_layout)

        panel_central.addWidget(panel_nueva)
    def crear_widgets_listado(self,panel_central):
        pass
        # panel_listado= QWidget(self.panel_datos)
        # panel_listado.setStyleSheet("background-color: #aa00aa;")
        # label=LabelItem("Listado",panel_listado)
        # label.move(20, 20)
        #
        # label=QLabel("Listado",panel_listado)
        # label.setStyleSheet("color: #ffffff; font-size: 20px;")
        # label.move(20, 20)
        #
        # self.lbl_salida=QLabel(panel_listado)
        # self.lbl_salida.setGeometry(20, 50,570,400)
        # self.lbl_salida.setStyleSheet("background-color: #F5F5DC; padding:5 10 5 10; font-size:16px;")
        # self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        #
        #
        # self.panel_datos.addWidget(panel_nueva)
        # self.panel_datos.addWidget(panel_listado)

    def crear_menu(self,panel_menu):
        layout_menu=QHBoxLayout(panel_menu)


        self.boton_nueva=BotonMenu("Nueva",panel_menu)

        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_menu)
        self.boton_listado.clicked.connect(self.listado_entrada)

        self.boton_salir = BotonMenu("Salir", panel_menu)
        self.boton_salir.clicked.connect(self.cerrar_app)

        layout_menu.addWidget(self.boton_nueva)
        layout_menu.addWidget(self.boton_listado)
        layout_menu.addWidget(self.boton_salir)

    def nueva_entrada(self):
        self.panel_datos.setCurrentIndex(0)
        self.boton_nueva.setChecked(True)
        self.boton_listado.setChecked(False)
    def listado_entrada(self):
        self.panel_datos.setCurrentIndex(1)
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(True)
        self.listar()

    def cerrar_app(self):
        sys.exit()
    def guardar(self):
        entrada=self.edit_entrada.text()
        self.entradas.append(entrada)
        print(self.entradas)
        self.edit_entrada.clear()
    def listar(self):
        salida=' <span style = "color:#ff0000;">Listado de entradas</span><br>'
        for entrada in self.entradas:
            salida+=entrada+"<br>"
        self.lbl_salida.setText(salida)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana=Entradas()
    ventana.show()
    sys.exit(app.exec())