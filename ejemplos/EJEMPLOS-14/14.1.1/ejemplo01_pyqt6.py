import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit,QPushButton, QMessageBox

class VentanaSuma(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Suma")
        self.setFixedSize(300, 200) # tamaño fijo para absoluto
        self.init_ui()

    def init_ui(self):
        # Labels
        lbl1 = QLabel("Número 1:", self)
        lbl1.move(20, 20)

        lbl2 = QLabel("Número 2:", self)
        lbl2.move(20, 60)

        # Entradas
        self.entry1 = QLineEdit(self)
        self.entry1.setGeometry(100, 20, 150, 25)

        self.entry2 = QLineEdit(self)
        self.entry2.setGeometry(100, 60, 150, 25)

        # Botón azul claro
        self.btn_sumar = QPushButton("Sumar", self)
        self.btn_sumar.setGeometry(100, 100, 100, 30)
        self.btn_sumar.setStyleSheet("background-color: #85C1E9;")
        self.btn_sumar.clicked.connect(self.sumar)

        # Resultado
        self.lbl_resultado = QLabel("", self)
        self.lbl_resultado.setStyleSheet("background-color: #85C1E9")
        self.lbl_resultado.resize(120,25)
        self.lbl_resultado.move(100, 150)

    def sumar(self):
        try:
            n1 = float(self.entry1.text())
            n2 = float(self.entry2.text())
            self.lbl_resultado.setText(f"Suma: {n1 + n2}")
            self.lbl_resultado.adjustSize()
        except ValueError:
            QMessageBox.warning(self, "Error", "Introduce números válidos")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSuma()
    ventana.show()
    sys.exit(app.exec())