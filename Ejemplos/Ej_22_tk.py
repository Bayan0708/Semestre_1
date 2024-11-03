#Ejemplos tk

#Ejemplo 1
import sys
from PySide6.QtWidgets import QApplication, QLabel
app = QApplication(sys.argv)
label = QLabel ("Hello Word")
label.show()
app.exec()


#Ejemplo 2
# import sys
# from PySide6.QtWidgets import QApplication, QLabel, QPushButton
# from PySide6.QtCore import Slot

# @Slot()
# def say_hello():
#     print("Botton presionado, hola")

# app = QApplication(sys.argv)
# button = QPushButton("Click aquí")
# button.clicked.connect(say_hello)
# button.show()
# app.exec()


