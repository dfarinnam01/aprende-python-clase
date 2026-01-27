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
                                  margin:5 0 0 0;
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
                            border:2px solid #20b2aa;
                            }
                        QLineEdit:focus {
                            border:2px solid #1e90ff;
                        """
        )
        self.setPlaceholderText(placeholder)
class BotonAction(QPushButton):
    def __init__(self, text="",parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
                              QPushButton {
                                  background-color: #ba55d3;
                                  border:1px solid black;
                                  padding:5px;
                                  border-radius:5px;
                                  }
                              QPushButton:hover{
                                  background-color: #c71585;
                                  border-bottom:2px solid #c71585;
                                  font-weight:bold;
                                  }
                              QPushButton:pressed{
                                    background-color: #ff0000;
                                    font-weight:bold;
                                    border-bottom:2px solid #ff0000;
                                    }""")

