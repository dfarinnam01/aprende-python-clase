from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QFormLayout, QHBoxLayout,
    QVBoxLayout, QScrollArea
)
from PyQt6.QtCore import Qt


# ============================
#        PAGINA ALTA
# ============================
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

        btn = QPushButton("Dar de alta")
        btn.clicked.connect(self.alta)

        layout.addRow("Referencia", self.ref)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn)

    def alta(self):
        ref = self.ref.text().strip()

        if not ref:
            QMessageBox.warning(self, "Error", "Referencia obligatoria")
            return

        for a in self.main.articulos:
            if a["ref"] == ref:
                QMessageBox.warning(self, "Error", "La referencia ya existe")
                return

        # Validación numérica
        try:
            float(self.precio.text())
            int(self.stock.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Precio decimal y stock entero")
            return

        self.main.articulos.append({
            "ref": ref,
            "desc": self.desc.text(),
            "precio": self.precio.text(),
            "stock": self.stock.text(),
            "obs": self.obs.text()
        })

        self.main.guardar_datos()

        QMessageBox.information(self, "OK", "Artículo dado de alta")

        self.ref.clear()
        self.desc.clear()
        self.precio.clear()
        self.stock.clear()
        self.obs.clear()


# ============================
#        PAGINA LISTADO
# ============================
class PaginaListado(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QVBoxLayout(self)

        btn = QPushButton("Actualizar listado")
        btn.clicked.connect(self.mostrar)

        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.lbl)

        layout.addWidget(btn)
        layout.addWidget(scroll)

    def mostrar(self):
        texto = "<b>Listado de artículos</b><br><br>"

        for a in self.main.articulos:
            texto += (
                f"Ref: {a['ref']}<br>"
                f"Descripción: {a['desc']}<br>"
                f"Precio: {a['precio']}<br>"
                f"Stock: {a['stock']}<br>"
                f"Observaciones: {a['obs']}<br><hr>"
            )

        self.lbl.setText(texto)


# ============================
#        PAGINA MODIFICAR
# ============================
class PaginaModificar(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

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

        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_guardar)

    def buscar(self):
        self.actual = None
        ref = self.ref.text().strip()

        for a in self.main.articulos:
            if a["ref"] == ref:
                self.actual = a
                self.desc.setText(a["desc"])
                self.precio.setText(a["precio"])
                self.stock.setText(a["stock"])
                self.obs.setText(a["obs"])

                for campo in [self.desc, self.precio, self.stock, self.obs]:
                    campo.setEnabled(True)
                return

        QMessageBox.warning(self, "Error", "Referencia no encontrada")

    def guardar(self):
        if not self.actual:
            QMessageBox.warning(self, "Error", "Busca primero un artículo")
            return

        confirm = QMessageBox.question(self, "Confirmar", "¿Guardar cambios?")
        if confirm != QMessageBox.StandardButton.Yes:
            return

        self.actual["desc"] = self.desc.text()
        self.actual["precio"] = self.precio.text()
        self.actual["stock"] = self.stock.text()
        self.actual["obs"] = self.obs.text()

        self.main.guardar_datos()

        QMessageBox.information(self, "OK", "Artículo modificado")


# ============================
#        PAGINA BAJA
# ============================
class PaginaBaja(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

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

        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_borrar)

    def buscar(self):
        self.actual = None
        ref = self.ref.text().strip()

        for a in self.main.articulos:
            if a["ref"] == ref:
                self.actual = a
                self.desc.setText(a["desc"])
                self.precio.setText(a["precio"])
                self.stock.setText(a["stock"])
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

            self.ref.clear()
            self.desc.setText("-")
            self.precio.setText("-")
            self.stock.setText("-")
            self.obs.setText("-")
            self.actual = None


# ============================
#        PAGINA CONSULTA
# ============================
class PaginaConsulta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QFormLayout(self)

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

        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)

    def buscar(self):
        ref = self.ref.text().strip()

        if not ref:
            QMessageBox.warning(self, "Error", "Introduce una referencia")
            return

        for a in self.main.articulos:
            if a["ref"] == ref:
                self.desc.setText(a["desc"])
                self.precio.setText(a["precio"])
                self.stock.setText(a["stock"])
                self.obs.setText(a["obs"])
                return

        QMessageBox.information(self, "Aviso", "Artículo no encontrado")

        self.desc.setText("-")
        self.precio.setText("-")
        self.stock.setText("-")
        self.obs.setText("-")