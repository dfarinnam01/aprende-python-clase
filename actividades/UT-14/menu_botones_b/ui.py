from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit


class BotonMenu(QPushButton):
    def __init__(self, text="",parent=None):
        super().__init__(text, parent)
        self.setCheckable(True)
        self.setStyleSheet("""
                              QPushButton {
                                  background-color: #cccccc;
                                  border:1px solid black;
                                  padding:5px;
                                  border-radius:5px;
                                  }
                              QPushButton:checked{
                                  background-color: #ffebcd;
                                  border-bottom:2px solid black;
                                  font-weight:bold;
                                  }""")

class LabelItem(QLabel):
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("background-color: #ffffff;")

class EditItem(QLineEdit):
    def __init__(self,parent=None,placeholder=""):
        super().__init__(parent)
        self.setStyleSheet("""
                        QLineEdit {
                            background-color: #ffffff;
                            border:1px solid black;
                            border-radius:5px;
                            padding:5px;
                            }
                        QLineEdit:hover {
                            border:1px solid #20b2aa;
                            }"""
        )
        self.setPlaceholderText(placeholder)

