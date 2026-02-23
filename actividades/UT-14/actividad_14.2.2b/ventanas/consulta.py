from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QFormLayout, QHBoxLayout
)


class PaginaConsulta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo consultado: Ninguno")

        self.ref = QLineEdit()
        btn_buscar = QPushButton("Consultar")
        btn_buscar.clicked.connect(self.buscar)

        fila = QHBoxLayout()
        fila.addWidget(self.ref)
        fila.addWidget(btn_buscar)

        self.desc = QLabel("-")
        self.precio = QLabel("-")
        self.stock = QLabel("-")
        self.obs = QLabel("-")

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self.limpiar)

        layout.addRow(self.lbl_estado)
        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_limpiar)

    def buscar(self):
        ref = self.ref.text().strip()

        if not ref:
            QMessageBox.warning(self, "Error", "Introduce una referencia")
            return

        for a in self.main.articulos:
            if a["ref"] == ref:
                self.lbl_estado.setText(f"Artículo consultado: {ref}")
                self.desc.setText(a["desc"])
                self.precio.setText(str(a["precio"]))
                self.stock.setText(str(a["stock"]))
                self.obs.setText(a["obs"])
                return

        QMessageBox.information(self, "Aviso", "Artículo no encontrado")
        self.limpiar()

    def limpiar(self):
        self.lbl_estado.setText("Artículo consultado: Ninguno")
        self.ref.clear()
        self.desc.setText("-")
        self.precio.setText("-")
        self.stock.setText("-")
        self.obs.setText("-")