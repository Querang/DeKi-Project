import subprocess
import sys
import os.path
import sys
import webbrowser
import sqlite_Neko
from PyQt5.QtGui import QKeySequence, QWheelEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from layout_file.layout_rebuild import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
