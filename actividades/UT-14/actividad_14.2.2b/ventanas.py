from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QMessageBox, QFormLayout, QHBoxLayout, QVBoxLayout, QScrollArea
)
from PyQt6.QtCore import Qt

class PaginaAlta(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        layout = QFormLayout(self)
        layout.setVerticalSpacing(15)
        self.setStyleSheet("background-color: #ffffff; border-radius: 10px; padding: 15px;")

        self.ref = QLineEdit()
        self.desc = QLineEdit()
        self.precio = QLineEdit()
        self.stock = QLineEdit()
        self.obs = QLineEdit()

        for campo in [self.ref, self.desc, self.precio, self.stock, self.obs]:
            campo.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")

        btn = QPushButton("Dar de alta")
        btn.setStyleSheet(
            "background-color: #2196F3; color: white; font-weight: bold; padding: 8px; border-radius: 5px;"
            "QPushButton:hover { background-color: #0b7dda; }"
        )
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

        self.main.articulos.append({
            "ref": ref,
            "desc": self.desc.text(),
            "precio": self.precio.text(),
            "stock": self.stock.text(),
            "obs": self.obs.text()
        })
        self.main.guardar_datos()
        QMessageBox.information(self, "OK", "Artículo dado de alta")
        self.ref.clear(); self.desc.clear(); self.precio.clear(); self.stock.clear(); self.obs.clear()


class PaginaListado(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        layout = QVBoxLayout(self)
        btn = QPushButton("Actualizar listado")
        btn.setStyleSheet(
            "background-color: #FF9800; color:white; font-weight:bold; padding:6px; border-radius:5px;"
            "QPushButton:hover { background-color: #e68a00; }"
        )
        btn.clicked.connect(self.mostrar)
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.lbl.setStyleSheet("background:#eaeaea; padding:10px; border-radius:5px;")
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.lbl)
        layout.addWidget(btn)
        layout.addWidget(scroll)

    def mostrar(self):
        texto = "<b>Listado de artículos</b><br><br>"
        for a in self.main.articulos:
            texto += f"Ref: {a['ref']}<br>"
            texto += f"Descripción: {a['desc']}<br>"
            texto += f"Precio: {a['precio']}<br>"
            texto += f"Stock: {a['stock']}<br>"
            texto += f"Observaciones: {a['obs']}<br><hr>"
        self.lbl.setText(texto)


class PaginaModificar(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None
        layout = QFormLayout(self)
        layout.setVerticalSpacing(15)
        self.setStyleSheet("background-color: #ffffff; border-radius: 10px; padding: 15px;")

        self.ref = QLineEdit()
        btn_buscar = QPushButton("Buscar")
        btn_buscar.setStyleSheet(
            "background-color:#FF5722;color:white;font-weight:bold;padding:5px;border-radius:5px;"
            "QPushButton:hover {background-color:#e64a19;}"
        )
        btn_buscar.clicked.connect(self.buscar)
        fila = QHBoxLayout()
        fila.addWidget(self.ref)
        fila.addWidget(btn_buscar)

        self.desc = QLineEdit(); self.precio = QLineEdit()
        self.stock = QLineEdit(); self.obs = QLineEdit()
        for campo in [self.desc, self.precio, self.stock, self.obs]:
            campo.setStyleSheet("padding:5px; border:1px solid #ccc; border-radius:5px;")
            campo.setEnabled(False)

        btn_guardar = QPushButton("Guardar cambios")
        btn_guardar.setStyleSheet(
            "background-color:#4CAF50;color:white;font-weight:bold;padding:8px;border-radius:5px;"
            "QPushButton:hover{background-color:#45a049;}"
        )
        btn_guardar.clicked.connect(self.guardar)

        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_guardar)
        self.setLayout(layout)

    def buscar(self):
        self.actual = None
        ref = self.ref.text().strip()
        for a in self.main.articulos:
            if a["ref"] == ref:
                self.actual = a
                self.desc.setText(a["desc"]); self.precio.setText(a["precio"])
                self.stock.setText(a["stock"]); self.obs.setText(a["obs"])
                for campo in [self.desc, self.precio, self.stock, self.obs]:
                    campo.setEnabled(True)
                return
        QMessageBox.warning(self, "Error", "Referencia no encontrada")
        for campo in [self.desc, self.precio, self.stock, self.obs]:
            campo.setText(""); campo.setEnabled(False)

    def guardar(self):
        if not self.actual:
            QMessageBox.warning(self, "Error", "Busca primero un artículo")
            return
        self.actual["desc"] = self.desc.text(); self.actual["precio"] = self.precio.text()
        self.actual["stock"] = self.stock.text(); self.actual["obs"] = self.obs.text()
        self.main.guardar_datos()
        QMessageBox.information(self, "OK", "Artículo modificado")


class PaginaBaja(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.actual = None
        layout = QFormLayout(self)
        layout.setVerticalSpacing(15)
        self.setStyleSheet("background-color:#ffffff;border-radius:10px;padding:15px;")

        self.ref = QLineEdit()
        btn_buscar = QPushButton("Buscar")
        btn_buscar.setStyleSheet(
            "background-color:#FF5722;color:white;font-weight:bold;padding:5px;border-radius:5px;"
            "QPushButton:hover {background-color:#e64a19;}"
        )
        btn_buscar.clicked.connect(self.buscar)
        fila = QHBoxLayout(); fila.addWidget(self.ref); fila.addWidget(btn_buscar)

        self.desc = QLabel("-"); self.precio = QLabel("-"); self.stock = QLabel("-"); self.obs = QLabel("-")
        for lbl in [self.desc, self.precio, self.stock, self.obs]:
            lbl.setStyleSheet("padding:5px; border:1px solid #ccc; border-radius:5px; background:#f0f0f0;")

        btn_borrar = QPushButton("Borrar artículo")
        btn_borrar.setStyleSheet(
            "background-color:#F44336;color:white;font-weight:bold;padding:8px;border-radius:5px;"
            "QPushButton:hover{background-color:#d32f2f;}"
        )
        btn_borrar.clicked.connect(self.borrar)

        layout.addRow("Referencia", fila)
        layout.addRow("Descripción", self.desc)
        layout.addRow("Precio", self.precio)
        layout.addRow("Stock", self.stock)
        layout.addRow("Observaciones", self.obs)
        layout.addRow(btn_borrar)
        self.setLayout(layout)

    def buscar(self):
        self.actual = None
        ref = self.ref.text().strip()
        for a in self.main.articulos:
            if a["ref"] == ref:
                self.actual = a
                self.desc.setText(a["desc"]); self.precio.setText(a["precio"])
                self.stock.setText(a["stock"]); self.obs.setText(a["obs"])
                return
        QMessageBox.warning(self, "Error", "Referencia no encontrada")
        self.desc.setText("-"); self.precio.setText("-")
        self.stock.setText("-"); self.obs.setText("-")
        self.actual = None

    def borrar(self):
        if not self.actual:
            QMessageBox.warning(self, "Error", "Busca primero un artículo")
            return
        confirm = QMessageBox.question(self, "Confirmar", f"¿Borrar artículo {self.actual['ref']}?")
        if confirm == QMessageBox.StandardButton.Yes:
            self.main.articulos.remove(self.actual)
            self.main.guardar_datos()
            QMessageBox.information(self, "OK", "Artículo borrado")
            self.ref.clear(); self.desc.setText("-"); self.precio.setText("-")
            self.stock.setText("-"); self.obs.setText("-"); self.actual=None
