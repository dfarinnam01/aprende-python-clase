from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import sys
app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Hola PyQt6")
ventana.resize(400, 300)
label_nombre = QLabel(ventana)
label_nombre.setText("Nombre")
label_nombre.move(10,50)

nombre = QLineEdit(ventana)
nombre.setPlaceholderText("Nombre")
nombre.move(10,80)
btn_ver=QPushButton("Ver",ventana)
btn_ver.move(10,100)
ventana.show()
sys.exit(app.exec())