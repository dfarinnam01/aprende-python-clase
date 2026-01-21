from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys

def calcular_lineas():
    with open("ejemplo.txt", "r",encoding="UTF-8") as f:
        c=0
        for _ in f:
            c=c+1
        return c

def analiza_fichero():
    num_lineas = calcular_lineas()
    label_resultado.setText(f'El fichero tiene {num_lineas} lineas')

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
# ventana.resize(400, 300)
ventana.move(400,300)
# ventana.setGeometry(400, 300)
# ventana.setFixedSize(400, 300) fijas la ventana y no puedes cambiar el tamaño

label_titulo=QLabel("Fichero: ",ventana)
label_titulo.move(20,20)
edit_filename=QLineEdit(ventana)
edit_filename.move(100,20)
edit_filename.resize(100,25)

btn_cargar=QPushButton("Analizar",ventana)
btn_cargar.move(200,20)
btn_cargar.clicked.connect(analiza_fichero)

label_lineas=QLabel(f"Numero de lineas del fichero",ventana)
label_lineas.setStyleSheet("font-weight: bold")
label_lineas.move(20, 60)

label_resultado=QLabel("",ventana)
label_resultado.move(20, 80)
label_resultado.resize(350,25)
label_resultado.setStyleSheet("background-color: rgb(255, 255, 255);")
ventana.show()
sys.exit(app.exec())