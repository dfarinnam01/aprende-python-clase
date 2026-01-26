import sys
import cv2
from PyQt6.QtWidgets import (
    QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
)
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer


class WebcamWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Webcam - PyQt6")

        # Label para la imagen
        self.image_label = QLabel()
        self.image_label.setScaledContents(True)

        # Botón cerrar
        self.close_button = QPushButton("Cerrar")
        self.close_button.clicked.connect(self.close_app)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        # Inicializar webcam
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Timer para actualizar frames
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qt_image = QImage(
            frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888
        )

        self.image_label.setPixmap(QPixmap.fromImage(qt_image))

    def close_app(self):
        self.timer.stop()
        self.cap.release()
        self.close()

    def closeEvent(self, event):
        self.timer.stop()
        self.cap.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebcamWidget()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
