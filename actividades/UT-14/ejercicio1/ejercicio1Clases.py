from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
import sys
class Contador(QWidget):
    def __init__(self):
        super().__init__()
        self.contador = 0
        self.config_ui()
        self.show()
    def config_ui(self):
        self.setWindowTitle("Contador")
        self.setFixedSize(400, 300)
        self.move(100, 100)
        self.crear_widgets()

    def incrementar(self):
        self.contador += 1
        self.label_contador.setText(str(self.contador))

    def decrementar(self):
        self.contador -= 1
        self.label_contador.setText(str(self.contador))
    def crear_widgets(self):
        btn_sumar = QPushButton("+", self)
        btn_sumar.move(100, 20)
        btn_sumar.clicked.connect(self.incrementar)

        btn_restar = QPushButton("-", self)
        btn_restar.move(200, 20)
        btn_restar.clicked.connect(self.decrementar)

        self.label_contador = QLabel(str(self.contador), self)
        self.label_contador.setStyleSheet("font-weight: bold")
        self.label_contador.move(20, 60)
        self.label_contador.resize(30, 80)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ventana = crear_ventana()
    # crear_widgets(ventana)
    # sys.exit(app.exec())
    app = QApplication(sys.argv)
    ventana = Contador()
    sys.exit(app.exec())
