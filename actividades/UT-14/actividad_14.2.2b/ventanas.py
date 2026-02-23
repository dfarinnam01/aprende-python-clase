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


# ============================
#        PAGINA LISTADO
# ============================
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


# ============================
#        PAGINA MODIFICAR
# ============================
class PaginaModificar(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo cargado: Ninguno")
        self.lbl_estado.setStyleSheet("color: blue; font-weight: bold;")

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
        self.lbl_estado.setText("Artículo cargado: Ninguno")

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


# ============================
#        PAGINA BAJA
# ============================
class PaginaBaja(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo cargado: Ninguno")
        self.lbl_estado.setStyleSheet("color: red; font-weight: bold;")

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
        self.lbl_estado.setText("Artículo cargado: Ninguno")

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


# ============================
#        PAGINA CONSULTA
# ============================
class PaginaConsulta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo consultado: Ninguno")
        self.lbl_estado.setStyleSheet("color: green; font-weight: bold;")

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


# ============================
#        PAGINA LISTADO
# ============================
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


# ============================
#        PAGINA MODIFICAR
# ============================
class PaginaModificar(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo cargado: Ninguno")
        self.lbl_estado.setStyleSheet("color: blue; font-weight: bold;")

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
        self.lbl_estado.setText("Artículo cargado: Ninguno")

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


# ============================
#        PAGINA BAJA
# ============================
class PaginaBaja(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo cargado: Ninguno")
        self.lbl_estado.setStyleSheet("color: red; font-weight: bold;")

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
        self.lbl_estado.setText("Artículo cargado: Ninguno")

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


# ============================
#        PAGINA CONSULTA
# ============================
class PaginaConsulta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        layout = QFormLayout(self)

        self.lbl_estado = QLabel("Artículo consultado: Ninguno")
        self.lbl_estado.setStyleSheet("color: green; font-weight: bold;")

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