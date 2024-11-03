import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Menú Matemático")

        self.creaAcciones()
        self.creaMenu()
        self.tabs = self.createTabs()
        self.setCentralWidget(self.tabs)


    def creaAcciones(self):
        self.open_action = QAction("Abrir", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.open_file)

        self.exit_action = QAction("Salir", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.exit_app)

        self.acercade_action = QAction("Acerca de", self)
        self.acercade_action.triggered.connect(self.acercaDe)

        self.ecuacion_action = QAction(QIcon(), "Ec. 2° grado", self)
        self.ecuacion_action.triggered.connect(self.ecuacion)

        self.newtonRaphson_action = QAction(QIcon(), "Newton - Raphson", self)
        self.newtonRaphson_action.triggered.connect(self.newtonRaphson)

        self.newtonRaphson_action = QAction(QIcon(), "Newton - Raphson", self)
        self.newtonRaphson_action.triggered.connect(self.newtonRaphson)

        self.biseccion_action = QAction(QIcon(), "Bisección", self)
        self.biseccion_action.triggered.connect(self.biseccion)

        self.trapezoidalCompuesto_action = QAction(QIcon(), "Trapezoidal compuesto", self)
        self.trapezoidalCompuesto_action.triggered.connect(self.trapezoidalCompuesto)

        self.simpsonTercio_action = QAction(QIcon(), "Simpson 1/3", self)
        self.simpsonTercio_action.triggered.connect(self.simpsonTercio)
        
        self.simpsonOctavo_action = QAction(QIcon(), "Simpson 3/8", self)
        self.simpsonOctavo_action.triggered.connect(self.simpsonOctavo)

        self.vectores_action = QAction(QIcon(), "Vectores", self)
        self.vectores_action.triggered.connect(self.vectores)

        self.matrices_action = QAction(QIcon(), "Matrices", self)
        self.matrices_action.triggered.connect(self.matrices)

        self.sisemaEc_action = QAction(QIcon(), "Sistema Ecuaciones", self)
        self.sisemaEc_action.triggered.connect(self.sistemaEc)

        self.media_action = QAction(QIcon(), "Media", self)
        self.media_action.triggered.connect(self.media)

        self.desviacion_action = QAction(QIcon(), "Desviacion", self)
        self.desviacion_action.triggered.connect(self.desviacion)

        self.percil_action = QAction(QIcon(), "Percil", self)
        self.percil_action.triggered.connect(self.percil)

    def creaMenu(self):
        self.file_menu = self.menuBar().addMenu("&Archivo")
        self.file_menu.addAction(self.open_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)

        self.opciones_menu = self.menuBar().addMenu("&Opciones")
        
        self.menuBar().addSeparator()

        self.acercade_menu = self.menuBar().addMenu("Acerca &de")
        self.acercade_menu.addAction(self.acercade_action)

        self.algebra_menu = self.menuBar().addMenu("Álgebra")
        self.algebra_menu.addAction(self.ecuacion_action)
        self.algebra_menu.addAction(self.newtonRaphson_action)
        self.algebra_menu.addAction(self.biseccion_action)

        self.calculoInt_menu = self.menuBar().addMenu("Cálculo Integral")
        self.calculoInt_menu.addAction(self.trapezoidalCompuesto_action)
        self.calculoInt_menu.addAction(self.simpsonTercio_action)
        self.calculoInt_menu.addAction(self.simpsonOctavo_action)

        self.algebraLineal_menu = self.menuBar().addMenu("Álgebra Lineal")
        self.algebraLineal_menu.addAction(self.vectores_action)
        self.algebraLineal_menu.addAction(self.matrices_action)
        self.algebraLineal_menu.addAction(self.sisemaEc_action)

        self.estadistica_menu = self.menuBar().addMenu("Estadísitca")
        self.estadistica_menu.addAction(self.media_action)
        self.estadistica_menu.addAction(self.desviacion_action)
        self.estadistica_menu.addAction(self.percil_action)
        
    def embed_into_hbox_layout(self, w, margin=5):
        """Embed a widget into a layout to give it a frame"""
        result = QWidget()
        layout = QHBoxLayout(result)
        layout.setContentsMargins(margin, margin, margin, margin)
        layout.addWidget(w)
        return result

    def createTabs(self):
        result = QTabWidget()
        #result.setTabPosition(QTabWidget.North)
        result.setTabPosition(QTabWidget.North)
        #result.setTabPosition(QTabWidget.East)
        #result.setTabPosition(QTabWidget.South)
        self.edit = QLineEdit("5")
        self.button = QPushButton("Genera datos")
        self.icoAlgebra = QtGui.QIcon("./iconos/algebra-icon.png")
        self.icoCalculo = QtGui.QIcon("./iconos/calculo_icon.png")
        self.icoEstadistica = QtGui.QIcon("./iconos/estadistica_icon.png")
        result.addTab(self.embed_into_hbox_layout(self.edit), self.icoAlgebra, "Algebra")
        result.addTab(self.embed_into_hbox_layout(self.button), self.icoCalculo, "Cálculo integral")
        result.addTab(self.embed_into_hbox_layout(self.edit), "Estadística")
        result.addTab(self.embed_into_hbox_layout(QWidget()), self.icoEstadistica, "Álgebra lineal")
        return result

    @Slot()
    def open_file(self, checked):
        print("Se debera abrir un archivo")
    
    @Slot()
    def acercaDe(self):
        QMessageBox.about(self, "Acerca de","Este ejemplo muestra como crear una <b>aplicación</b>"" <b>moderna</b> usando <b>Qt</b>, con una barra de menú, ""y tabs.")

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def ecuacion(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def newtonRaphson(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def biseccion(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def trapezoidalCompuesto(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def simpsonTercio(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def simpsonOctavo(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def vectores(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def matrices(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def sistemaEc(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def sumaVec(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def restaVec(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def multiplicacionVec(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def sumaMatrices(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def restaMatrices(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def multiplicacionMatrices(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def gauss(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    
    @Slot()
    def gaussSeidel(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def doolitle(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def media(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def desviacion(self):
        QMessageBox.about(self, "Menu", "Accion Menu")

    @Slot()
    def percil(self):
        QMessageBox.about(self, "Menu", "Accion Menu")
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())