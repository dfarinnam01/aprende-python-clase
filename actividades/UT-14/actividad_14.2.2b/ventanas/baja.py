from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QFormLayout, QHBoxLayout
)


class PaginaBaja(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo cargado: Ninguno")

        self.ref = QLineEdit()
        btn_buscar = QPushButton("Buscar")
        btn_buscar.clicked.connect(self.buscar)

        fila = QHBoxLayout()
        fila.addWidget(self.ref)
        fila.addWidget(btn_buscar)

        self.desc = QLabel("-")
        self.precio = QLabel("-")
        self.stock = QLabel("-")
        self.obs = QLabel("-")

        btn_borrar = QPushButton("Borrar artículo")
        btn_borrar.clicked.connect(self.borrar)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self.limpiar)

        layout.addRow(self.lbl_estado)
        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_borrar)
        layout.addRow(btn_limpiar)

    def buscar(self):
        self.actual = None
        ref = self.ref.text().strip()

        for a in self.main.articulos:
            if a["ref"] == ref:
                self.actual = a
                self.lbl_estado.setText(f"Artículo cargado: {ref}")

                self.desc.setText(a["desc"])
                self.precio.setText(str(a["precio"]))
                self.stock.setText(str(a["stock"]))
                self.obs.setText(a["obs"])
                return

        QMessageBox.warning(self, "Error", "Referencia no encontrada")

    def borrar(self):
        if not self.actual:
            QMessageBox.warning(self, "Error", "Busca primero un artículo")
            return

        confirm = QMessageBox.question(
            self,
            "Confirmar",
            f"¿Borrar artículo {self.actual['ref']}?"
        )

        if confirm == QMessageBox.StandardButton.Yes:
            self.main.articulos.remove(self.actual)
            self.main.guardar_datos()
            QMessageBox.information(self, "OK", "Artículo borrado")
            self.limpiar()
            self.main.stack.setCurrentWidget(self.main.pag_listado)

    def limpiar(self):
        self.actual = None
        self.lbl_estado.setText("Artículo cargado: Ninguno")
        self.ref.clear()
        self.desc.setText("-")
        self.precio.setText("-")
        self.stock.setText("-")
        self.obs.setText("-")