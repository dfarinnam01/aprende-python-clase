from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QPushButton,
    QMessageBox, QFormLayout
)


class PaginaAlta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QFormLayout(self)
        layout.setVerticalSpacing(15)

        self.ref = QLineEdit()
        self.desc = QLineEdit()
        self.precio = QLineEdit()
        self.stock = QLineEdit()
        self.obs = QLineEdit()

        btn_alta = QPushButton("Dar de alta")
        btn_alta.clicked.connect(self.alta)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self.limpiar)

        layout.addRow("Referencia", self.ref)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_alta)
        layout.addRow(btn_limpiar)

    def alta(self):
        ref = self.ref.text().strip()

        if not ref:
            QMessageBox.warning(self, "Error", "Referencia obligatoria")
            return

        for a in self.main.articulos:
            if a["ref"] == ref:
                QMessageBox.warning(self, "Error", "La referencia ya existe")
                return

        try:
            precio = float(self.precio.text())
            stock = int(self.stock.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio decimal y stock entero")
            return

        self.main.articulos.append({
            "ref": ref,
            "desc": self.desc.text(),
            "precio": precio,
            "stock": stock,
            "obs": self.obs.text()
        })

        self.main.guardar_datos()
        QMessageBox.information(self, "OK", "Artículo dado de alta")
        self.limpiar()

    def limpiar(self):
        self.ref.clear()
        self.desc.clear()
        self.precio.clear()
        self.stock.clear()
        self.obs.clear()