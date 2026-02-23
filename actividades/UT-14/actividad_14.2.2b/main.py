import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
)

from ventanas import (
    PaginaAlta, PaginaListado,
    PaginaModificar, PaginaBaja,
    PaginaConsulta
)

FICHERO = "articulos.dat"


class Articulos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CRUD Artículos")
        self.setFixedSize(750, 550)

        self.setStyleSheet("""
            QWidget {
                background-color: #EBE8E8;
                color: black;
                font-family: Arial;
                font-size: 12pt;
            }
        """)

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
        self.btn_consulta = QPushButton("Consulta")

        for btn in [
            self.btn_alta,
            self.btn_listado,
            self.btn_mod,
            self.btn_baja,
            self.btn_consulta
        ]:
            btn.setFixedHeight(40)
            barra.addWidget(btn)

        layout.addLayout(barra)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        self.pag_alta = PaginaAlta(self)
        self.pag_listado = PaginaListado(self)
        self.pag_mod = PaginaModificar(self)
        self.pag_baja = PaginaBaja(self)
        self.pag_consulta = PaginaConsulta(self)

        self.stack.addWidget(self.pag_alta)
        self.stack.addWidget(self.pag_listado)
        self.stack.addWidget(self.pag_mod)
        self.stack.addWidget(self.pag_baja)
        self.stack.addWidget(self.pag_consulta)

        self.btn_alta.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_alta))
        self.btn_listado.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_listado))
        self.btn_mod.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_mod))
        self.btn_baja.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_baja))
        self.btn_consulta.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_consulta))

        self.stack.currentChanged.connect(self.actualizar_listado_auto)

    def actualizar_listado_auto(self):
        if self.stack.currentWidget() == self.pag_listado:
            self.pag_listado.mostrar()

    def cargar_datos(self):
        self.articulos.clear()

        if not os.path.exists(FICHERO):
            return

        with open(FICHERO, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) != 5:
                    continue

                ref, desc, precio, stock, obs = partes

                self.articulos.append({
                    "ref": ref,
                    "desc": desc,
                    "precio": float(precio),
                    "stock": int(stock),
                    "obs": obs
                })

    def guardar_datos(self):
        with open(FICHERO, "w", encoding="utf-8") as f:
            for a in self.articulos:
                f.write(
                    f"{a['ref']}|{a['desc']}|{a['precio']}|"
                    f"{a['stock']}|{a['obs']}\n"
                )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Articulos()
    window.show()
    sys.exit(app.exec())