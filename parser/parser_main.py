import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from layout.main_layout import Ui_MainWindow
from layout.template_layout import Dialog_get_date


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.show()
        self.serfing_button.clicked.connect(self.get_parse_date)

    def get_parse_date(self):
        self.dialog_date = Dialog_get_date([self.geometry().x(), self.geometry().y()])
        self.dialog_date.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
