from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys
class ContadorLineas(QWidget):
    def __init__(self):
        super().__init__()
        self.config_ui()
        self.show()
    def config_ui(self):
        self.setWindowTitle("Contador de lineas")
        self.setFixedSize(400, 300)
        self.move(100, 100)
        self.crear_widgets()

    def crear_widgets(self):
        label_titulo = QLabel("Fichero: ", self)
        label_titulo.move(20, 20)

        self.edit_filename = QLineEdit(self)
        self.edit_filename.move(100, 20)
        self.edit_filename.resize(100, 25)

        btn_cargar = QPushButton("Analizar", self)
        btn_cargar.move(200, 20)
        btn_cargar.clicked.connect(self.analiza_fichero)

        label_lineas = QLabel(f"Numero de lineas del fichero", self)
        label_lineas.setStyleSheet("font-weight: bold")
        label_lineas.move(20, 60)

        self.label_resultado = QLabel("", self)
        self.label_resultado.move(20, 80)
        self.label_resultado.resize(350, 25)
        self.label_resultado.setStyleSheet("background-color: rgb(255, 255, 255);")

    def calcular_lineas(self):
        with open(self.edit_filename.text(), "r",encoding="UTF-8") as f:
            c=0
            for _ in f:
                c=c+1
            return c

    def analiza_fichero(self):
            num_lineas = self.calcular_lineas()
            self.label_resultado.setText(f'El fichero tiene {num_lineas} lineas')

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ventana = crear_ventana()
    # crear_widgets(ventana)
    # sys.exit(app.exec())
    app = QApplication(sys.argv)
    ventana = ContadorLineas()
    ventana.show()
    sys.exit(app.exec())
