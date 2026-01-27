import sys

from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QStackedWidget, QLabel, QLineEdit, QVBoxLayout, \
    QHBoxLayout, QFormLayout, QGridLayout, QSizePolicy, QMainWindow, QStatusBar, QScrollArea, QGraphicsOpacityEffect

from ui import BotonMenu, LabelItem, EditItem, BotonAction

'''
Tiene áreas predefinidas:
Barra de menú (menuBar())
Barra de herramientas (addToolBar())
Panel central (setCentralWidget())
Barra de estado (statusBar())
Dock widgets (paneles acoplables) (addDockWidget())
+--------------------------------------------------+
| MenuBar (Archivo, Edición, Ayuda...)           |
+--------------------------------------------------+
| ToolBar (iconos, botones)                      |
+--------------------------------------------------+
| DockWidget  | CentralWidget                     |
|            |                                   |
|            |                                   |
+------------+----------------------------------+
| StatusBar (mensajes, estado)                   |
+--------------------------------------------------+

'''
class Entradas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entradas = []
        self.config_ui()

    def config_ui(self):
        self.setWindowTitle("Menu botones - Entradas")
        self.resize(600, 500)
        self.crear_widgets()
        # self.statusBar().showMessage(f"Abriendo la aplicación",5000)
        self.statusBar().showMessage(f"Número de entradas: {len(self.entradas)}")

    def crear_widgets(self):

        # Panel Menu
        self.crear_menu()

        self.panel_central = QStackedWidget()
        self.panel_central.setStyleSheet("background-color: #8B0000;")
        self.crear_widgets_entrada(self.panel_central)
        self.crear_widgets_listado(self.panel_central)
        self.setCentralWidget(self.panel_central)

        panel_estado = QStatusBar()
        panel_estado.setStyleSheet("background-color: #c71585;")
        panel_estado.setFixedHeight(50)

        self.setStatusBar(panel_estado)


    def crear_menu(self):
        panel_menu = QWidget()
        panel_menu.setFixedHeight(50)
        panel_menu.setStyleSheet("background-color: #c71585;")
        self.setMenuWidget(panel_menu)

        layout_menu = QHBoxLayout(panel_menu)
        # panel_menu.setLayout(layout_menu)

        self.boton_nueva = BotonMenu("Nueva", panel_menu)
        self.boton_nueva.setCheckable(True)
        self.boton_nueva.setChecked(True)
        self.boton_nueva.clicked.connect(self.nueva_entrada)

        self.boton_listado = BotonMenu("Listado", panel_menu)
        self.boton_listado.setCheckable(True)
        self.boton_listado.setChecked(False)
        self.boton_listado.clicked.connect(self.listado_entradas)

        self.boton_salir = BotonMenu("Salir", panel_menu)
        self.boton_salir.setCheckable(True)
        self.boton_salir.clicked.connect(self.cerrar_app)

        layout_menu.addWidget(self.boton_nueva)
        layout_menu.addWidget(self.boton_listado)
        layout_menu.addWidget(self.boton_salir)

    def crear_widgets_entrada(self, panel_central):
        panel_nueva = QWidget()
        # panel_nueva.setStyleSheet("background-color: #8B8888;")

        layout_panel_nueva = QVBoxLayout(panel_nueva)
        layout_panel_nueva.setContentsMargins(20, 20, 20, 20)
        layout_panel_nueva.setSpacing(15)
        # panel_nueva.setLayout(layout_panel_nueva)

        #  Stretch superior para centrar verticalmente
        layout_panel_nueva.addStretch(1)

        # --- Fila centrada (Label + Edit) ---
        layout_fila_entrada = QHBoxLayout()
        layout_fila_entrada.setSpacing(10)

        label = LabelItem("Entrada")
        self.edit_entrada = EditItem()
        self.edit_entrada.setFixedWidth(200)

        # Fila item entrada
        layout_fila_entrada.addStretch(1)
        layout_fila_entrada.addWidget(label)
        layout_fila_entrada.addWidget(self.edit_entrada)
        layout_fila_entrada.addStretch(1)

        layout_panel_nueva.addLayout(layout_fila_entrada)

        #  Stretch inferior para centrar verticalmente
        layout_panel_nueva.addStretch(1)

        # --- Botón abajo a la derecha ---
        button_layout = QHBoxLayout()

        boton_guardar = BotonAction("Guardar")
        boton_guardar.setFixedWidth(100)
        boton_guardar.clicked.connect(self.guardar)

        button_layout.addStretch(1)
        button_layout.addWidget(boton_guardar)

        layout_panel_nueva.addLayout(button_layout)

        panel_central.addWidget(panel_nueva)


    def crear_widgets_listado(self, panel_central):
        # Creamos un panel contenedor
        panel_listado = QWidget()

        # Creamos layout
        layout_panel_listado = QVBoxLayout(panel_listado)
        layout_panel_listado.setContentsMargins(20, 20, 20, 20)
        layout_panel_listado.setSpacing(10)
        # panel_listado.setLayout(layout_panel_listado)

        # Label + Edit
        label = LabelItem("Listado")
        label.setFixedHeight(25)
        label.setStyleSheet("color:#ffffff;font-size: 20px;")
        layout_panel_listado.addWidget(label)

        # Sin scroll
        '''self.lbl_salida= QLabel(panel_listado)
        self.lbl_salida.setStyleSheet("background-color:#F5F5DC; padding:5 10 5 10;;font-size: 16px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_panel_listado.addWidget( self.lbl_salida)'''
        # Con scroll
        self.lbl_salida = QLabel(panel_listado)
        self.lbl_salida.setStyleSheet("background-color:#F5F5DC; padding:5 10 5 10;;font-size: 16px;")
        self.lbl_salida.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll_salida = QScrollArea()
        scroll_salida.setWidgetResizable(True)
        scroll_salida.setWidget(self.lbl_salida)
        # Cambiar colores del scroll vertical
        '''scroll_salida.setStyleSheet("""
        QScrollBar:vertical {
            background: #f0f0f0;          /* color del track */
            width: 15px;                   /* ancho del scroll */
            margin: 0px 0px 0px 0px;
            border-radius: 5px;
        }

        QScrollBar::handle:vertical {
            background: #c71585;           /* color de la “manija” */
            min-height: 20px;
            border-radius: 5px;
        }

        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            background: none;
            height: 0px;
        }

        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            background: none;
        }
        """)'''
        layout_panel_listado.addWidget(scroll_salida)

        # Añadimos el panel al QStackedWidget
        panel_central.addWidget(panel_listado)

    def fade_to_index(self, panel_central,index):
        next_w = panel_central.widget(index)

        effect = QGraphicsOpacityEffect(next_w)
        next_w.setGraphicsEffect(effect)
        effect.setOpacity(0.0)

        panel_central.setCurrentIndex(index)

        anim = QPropertyAnimation(effect, b"opacity", panel_central)
        anim.setDuration(1000)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        anim.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def nueva_entrada(self):
        # self.panel_central.setCurrentIndex(0)
        self.fade_to_index(self.panel_central, 0)
        self.boton_nueva.setChecked(True)
        self.boton_listado.setChecked(False)

    def listado_entradas(self):
        # self.panel_central.setCurrentIndex(1)
        self.fade_to_index(self.panel_central, 1)
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(True)
        self.listar()

    def cerrar_app(self):
        self.boton_nueva.setChecked(False)
        self.boton_listado.setChecked(False)
        self.boton_salir.setChecked(True)
        # sys.exit()
        QApplication.quit()

    def guardar(self):
        entrada = self.edit_entrada.text()
        self.entradas.append(entrada)
        self.edit_entrada.clear()
        self.statusBar().showMessage(f"Número de entradas: {len(self.entradas)}")

    def listar(self):
        salida = '<span style="color:#ff0000;">Listado de entradas</span><br>'
        for entrada in self.entradas:
           salida += entrada + "<br>"
        self.lbl_salida.setText(salida)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Entradas()
    ventana.show()
    sys.exit(app.exec())