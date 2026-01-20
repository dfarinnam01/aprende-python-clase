from PyQt6.QtWidgets import QApplication, QWidget, QLabel,QPushButton
import sys

def crear_ventana():

    ventana = QWidget()
    ventana.setWindowTitle("Contador")
    # ventana.resize(400, 300)
    #ventana.move(400, 300)
    ventana.setGeometry(50,50,400, 300)
    # ventana.setFixedSize(400, 300) fijas la ventana y no puedes cambiar el tamaño
    return ventana

def crear_widgets(ventana):
    def incrementar():
        global contador
        contador += 1
        label_contador.setText(str(contador))
    def decrementar():
        global contador
        contador -= 1
        label_contador.setText(str(contador))


    btn_sumar = QPushButton("+", ventana)
    btn_sumar.move(100, 20)
    btn_sumar.clicked.connect(incrementar)

    btn_restar = QPushButton("-", ventana)
    btn_restar.move(200, 20)
    btn_restar.clicked.connect(decrementar)

    label_contador = QLabel(str(contador), ventana)
    label_contador.setStyleSheet("font-weight: bold")
    label_contador.move(20, 60)
    label_contador.resize(30,80)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    contador = 0
    ventana = crear_ventana()
    crear_widgets(ventana)
    ventana.show()
    sys.exit(app.exec())