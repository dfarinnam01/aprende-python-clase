from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QScrollArea
)
from PyQt6.QtCore import Qt


class PaginaListado(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QVBoxLayout(self)

        self.lbl_total = QLabel()
        self.lbl_total.setStyleSheet("font-weight: bold;")

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.lbl)

        layout.addWidget(self.lbl_total)
        layout.addWidget(scroll)

    def mostrar(self):
        total = len(self.main.articulos)
        self.lbl_total.setText(f"Total artículos: {total}")

        if total == 0:
            self.lbl.setText("No hay artículos registrados.")
            return

        texto = ""

        for a in sorted(self.main.articulos, key=lambda x: x["ref"]):
            texto += (
                f"<b>Ref:</b> {a['ref']}<br>"
                f"Descripción: {a['desc']}<br>"
                f"Precio: {a['precio']}<br>"
                f"Stock: {a['stock']}<br>"
                f"Observaciones: {a['obs']}<br><hr>"
            )

        self.lbl.setText(texto)