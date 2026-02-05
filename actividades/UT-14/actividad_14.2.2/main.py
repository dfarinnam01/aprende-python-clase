import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QMessageBox, QScrollArea
)
from PyQt6.QtCore import Qt


FICHERO = "articulos.dat"


class Articulos(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CRUD Artículos")
        self.setFixedSize(700, 500)

        self.articulos = []
        self.init_ui()
        self.cargar_datos()

    # ---------------- UI ----------------
    def init_ui(self):
        central = QWidget(self)
        self.setCentralWidget(central)

        label = QLabel("Referencia", central)
        label.move(30, 30)

        label = QLabel("Descripción", central)
        label.move(30, 70)

        label = QLabel("Precio", central)
        label.move(30, 110)

        label = QLabel("Stock", central)
        label.move(30, 150)

        label = QLabel("Observaciones", central)
        label.move(30, 190)

        self.ref = QLineEdit(central)
        self.ref.setGeometry(140, 30, 200, 25)

        self.desc = QLineEdit(central)
        self.desc.setGeometry(140, 70, 200, 25)

        self.precio = QLineEdit(central)
        self.precio.setGeometry(140, 110, 200, 25)

        self.stock = QLineEdit(central)
        self.stock.setGeometry(140, 150, 200, 25)

        self.obs = QLineEdit(central)
        self.obs.setGeometry(140, 190, 200, 25)

        btn_alta = QPushButton("Alta", central)
        btn_alta.setGeometry(400, 30, 120, 30)
        btn_alta.clicked.connect(self.alta)

        btn_baja = QPushButton("Baja", central)
        btn_baja.setGeometry(400, 70, 120, 30)
        btn_baja.clicked.connect(self.baja)

        btn_mod = QPushButton("Modificar", central)
        btn_mod.setGeometry(400, 110, 120, 30)
        btn_mod.clicked.connect(self.modificar)

        btn_listar = QPushButton("Listado", central)
        btn_listar.setGeometry(400, 150, 120, 30)
        btn_listar.clicked.connect(self.listar)

        self.lbl_salida = QLabel()
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.lbl_salida.setStyleSheet(
            "background-color:#f5f5dc; padding:10px;"
        )
        scroll = QScrollArea(central)
        scroll.setGeometry(30, 240, 640, 220)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.lbl_salida)

    def alta(self):
        ref = self.ref.text().strip()
        desc = self.desc.text().strip()
        precio = self.precio.text().strip()
        stock = self.stock.text().strip()
        obs = self.obs.text().strip()
        if not ref:
            self.mensaje("La referencia es obligatoria")
            return
        for articulo in self.articulos:
            if articulo["ref"] == ref:
                self.mensaje("La referencia ya existe")
                return
        articulo = {
            "ref": ref,
            "desc": desc,
            "precio": precio,
            "stock": stock,
            "obs": obs
        }
        self.articulos.append(articulo)
        self.guardar_datos()
        self.limpiar()
        self.mensaje("Artículo dado de alta")

    def baja(self):
        ref = self.ref.text().strip()
        encontrado = False
        for articulo in self.articulos:
            if articulo["ref"] == ref:
                self.articulos.remove(articulo)
                encontrado = True
        if not encontrado:
            self.mensaje(f'Articulo con Referencia "{ref}" no existe')
        else:
            self.guardar_datos()
            self.limpiar()
            self.mensaje(f'Articulo con Referencia "{ref}" borrado')

    def modificar(self):
        ref = self.ref.text().strip()

        for a in self.articulos:
            if a["ref"] == ref:
                a["desc"] = self.desc.text().strip()
                a["precio"] = self.precio.text().strip()
                a["stock"] = self.stock.text().strip()
                a["obs"] = self.obs.text().strip()

                self.guardar_datos()
                self.limpiar()
                self.mensaje("Artículo modificado")
                return

        self.mensaje("No existe la referencia")

    def listar(self):
        texto = "<b>Listado de artículos</b><br><br>"
        for articulo in self.articulos:
            texto += f"Ref: {articulo['ref']}<br>"
            texto += f"Descripción: {articulo['desc']}<br>"
            texto += f"Precio: {articulo['precio']}<br>"
            texto += f"Stock: {articulo['stock']}<br>"
            texto += f"Observaciones: {articulo['obs']}<br>"
            texto += "<hr>"
        self.lbl_salida.setText(texto)

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
            for articulo in self.articulos:
                linea = f"{articulo['ref']}|{articulo['desc']}|{articulo['precio']}|{articulo['stock']}|{articulo['obs']}\n"
                f.write(linea)

    def limpiar(self):
        self.ref.clear()
        self.desc.clear()
        self.precio.clear()
        self.stock.clear()
        self.obs.clear()

    def mensaje(self, texto):
        QMessageBox.information(self, "Info", texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Articulos()
    ventana.show()
    sys.exit(app.exec())
