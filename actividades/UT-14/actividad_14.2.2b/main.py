import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from ventanas import PaginaAlta, PaginaListado, PaginaModificar, PaginaBaja

FICHERO = "articulos.dat"

class Articulos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Artículos")
        self.setFixedSize(750, 550)
        self.setStyleSheet("background-color: #f0f0f5; font-family: Arial; font-size: 12pt;")
        self.articulos = []
        self.cargar_datos()

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        barra = QHBoxLayout()
        self.btn_alta = QPushButton("Alta")
        self.btn_listado = QPushButton("Listado")
        self.btn_mod = QPushButton("Modificar")
        self.btn_baja = QPushButton("Baja")

        for btn in [self.btn_alta, self.btn_listado, self.btn_mod, self.btn_baja]:
            btn.setFixedHeight(40)
            barra.addWidget(btn)

        layout.addLayout(barra)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        self.pag_alta = PaginaAlta(self)
        self.pag_listado = PaginaListado(self)
        self.pag_mod = PaginaModificar(self)
        self.pag_baja = PaginaBaja(self)

        self.stack.addWidget(self.pag_alta)
        self.stack.addWidget(self.pag_listado)
        self.stack.addWidget(self.pag_mod)
        self.stack.addWidget(self.pag_baja)

        # Conectar botones a métodos (sin lambda)
        self.btn_alta.clicked.connect(self.mostrar_alta)
        self.btn_listado.clicked.connect(self.mostrar_listado)
        self.btn_mod.clicked.connect(self.mostrar_mod)
        self.btn_baja.clicked.connect(self.mostrar_baja)

    # Métodos para mostrar páginas
    def mostrar_alta(self):
        self.stack.setCurrentWidget(self.pag_alta)

    def mostrar_listado(self):
        self.stack.setCurrentWidget(self.pag_listado)

    def mostrar_mod(self):
        self.stack.setCurrentWidget(self.pag_mod)

    def mostrar_baja(self):
        self.stack.setCurrentWidget(self.pag_baja)

    def cargar_datos(self):
        if not os.path.exists(FICHERO):
            return
        with open(FICHERO, "r", encoding="utf-8") as f:
            for linea in f:
                ref, desc, precio, stock, obs = linea.strip().split("|")
                self.articulos.append({
                    "ref": ref,
                    "desc": desc,
                    "precio": precio,
                    "stock": stock,
                    "obs": obs
                })


    def guardar_datos(self):
        with open(FICHERO, "w", encoding="utf-8") as f:
            for a in self.articulos:
                f.write(f"{a['ref']}|{a['desc']}|{a['precio']}|{a['stock']}|{a['obs']}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Articulos()
    ventana.show()
    sys.exit(app.exec())
