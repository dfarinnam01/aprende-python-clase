from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QFormLayout, QHBoxLayout
)


class PaginaModificar(QWidget):
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

        self.desc = QLineEdit()
        self.precio = QLineEdit()
        self.stock = QLineEdit()
        self.obs = QLineEdit()

        for campo in [self.desc, self.precio, self.stock, self.obs]:
            campo.setEnabled(False)

        btn_guardar = QPushButton("Guardar cambios")
        btn_guardar.clicked.connect(self.guardar)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self.limpiar)

        layout.addRow(self.lbl_estado)
        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_guardar)
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

                for campo in [self.desc, self.precio, self.stock, self.obs]:
                    campo.setEnabled(True)
                return

        QMessageBox.warning(self, "Error", "Referencia no encontrada")

    def guardar(self):
        if not self.actual:
            QMessageBox.warning(self, "Error", "Busca primero un artículo")
            return

        try:
            precio = float(self.precio.text())
            stock = int(self.stock.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio decimal y stock entero")
            return

        confirm = QMessageBox.question(self, "Confirmar", "¿Guardar cambios?")
        if confirm != QMessageBox.StandardButton.Yes:
            return

        self.actual["desc"] = self.desc.text()
        self.actual["precio"] = precio
        self.actual["stock"] = stock
        self.actual["obs"] = self.obs.text()

        self.main.guardar_datos()
        QMessageBox.information(self, "OK", "Artículo modificado")

    def limpiar(self):
        self.actual = None
        self.lbl_estado.setText("Artículo cargado: Ninguno")
        self.ref.clear()
        self.desc.clear()
        self.precio.clear()
        self.stock.clear()
        self.obs.clear()

        for campo in [self.desc, self.precio, self.stock, self.obs]:
            campo.setEnabled(False)