import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from layout.main_layout import Ui_MainWindow
from layout.template_layout import Dialog_get_date
import Firo_parse_sqlite
import layout.template_layout


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.show()
        self.serfing_button.clicked.connect(self.get_parse_date)
        # self.get_parse_date()
        self.conn = Firo_parse_sqlite.create_connection("parse_.db")
        """function"""
        self.load_label()

    def load_label(self):
        self.clearLayout()
        with self.conn:
            data = Firo_parse_sqlite.get_data(self.conn)
            for item in data:
                self.verticalLayout_2.addWidget(layout.template_layout.GenerateParseLabel(self,item))

    def clearLayout(self):
        while self.verticalLayout_2.count():
            child = self.verticalLayout_2.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def get_parse_date(self):
        self.dialog_date = Dialog_get_date(self,[self.geometry().x(), self.geometry().y()])
        self.dialog_date.exec_()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MiddleButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
