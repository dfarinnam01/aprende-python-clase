from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

def calcular_lineas():
    with open("ejemplo.txt", "r",encoding="UTF-8") as f:
        c=0
        for _ in f:
            c=c+1
        return c

app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
ventana.resize(400, 300)

label_lineas=QLabel(f"Numero de lineas del fichero",ventana)
label_lineas.setStyleSheet("font-weight: bold")
label_lineas.move(20, 20)
label_resultado=QLabel("",ventana)
label_resultado.move(20, 60)
num_lineas=calcular_lineas()
label_resultado.setText(f"El fichero tiene {num_lineas} lineas")
label_resultado.setStyleSheet("background-color: rgb(255, 255, 255);")
ventana.show()
sys.exit(app.exec())