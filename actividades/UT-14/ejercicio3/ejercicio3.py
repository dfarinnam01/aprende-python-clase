from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QMessageBox
import sys
class Suma_ADV_label(QWidget):
    def __init__(self):
        super().__init__()
        self.suma = 0
        self.config_ui()
        self.show()
    def config_ui(self):
        self.setWindowTitle("Suma")
        self.setFixedSize(400, 300)
        self.move(100, 100)
        self.crear_widgets()

    def sumar(self):
        try:
            n1 = int(self.label_input_n1.text())
            n2 = int(self.label_input_n2.text())
            self.label_suma.setText("Resultado: "+str(n1+n2))
            self.msgBox.clear()
        except Exception:
            self.msgBox = QLabel("Introduce numeros correctamente",self)
            self.msgBox.move(100, 120)
            self.msgBox.setStyleSheet("color: red")
            self.msgBox.show()


    def crear_widgets(self):
        self.label_input_n1=QLineEdit(self)
        self.label_input_n1.move(30, 10)
        self.label_input_n1.resize(100, 30)

        self.label_input_n2 = QLineEdit(self)
        self.label_input_n2.move(200, 10)
        self.label_input_n2.resize(100, 30)

        btn_sumar = QPushButton("Suma", self)
        btn_sumar.move(130, 60)
        btn_sumar.clicked.connect(self.sumar)


        self.label_suma = QLabel("Resultado: "+str(self.suma), self)
        self.label_suma.setStyleSheet("font-weight: bold")
        self.label_suma.move(20, 60)
        self.label_suma.resize(110, 80)

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # ventana = crear_ventana()
    # crear_widgets(ventana)
    # sys.exit(app.exec())
    app = QApplication(sys.argv)
    ventana = Suma_ADV_label()
    sys.exit(app.exec())