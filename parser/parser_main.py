import sys
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import schedule
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QLabel
from PyQt5 import QtCore
from PyQt5.uic.properties import QtGui

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
        self.ProgressBar()

    def load_label(self):
        with self.conn:
            data = Firo_parse_sqlite.get_data(self.conn)
            for item in data:
                self.verticalLayout_2.addWidget(layout.template_layout.GenerateParseLabel(self, item))

    # def connect(self):
    #     schedule.every(10).seconds.do(self.connect_sub)
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
    #
    # def connect_sub(self):
    #     while self.verticalLayout_2.count():
    #         child = self.verticalLayout_2.takeAt(0)
    #         if child.widget():
    #             child.widget().handler_content()

    def get_parse_date(self):
        self.dialog_date = Dialog_get_date(self, [self.geometry().x(), self.geometry().y()])
        self.dialog_date.exec_()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MiddleButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def ProgressBar(self):
        self.a = ProgressLoading([self.geometry().x(), self.geometry().y()])
        self.a.exec_()


class ProgressLoading(QDialog):
    def __init__(self, position):
        super(ProgressLoading, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.position_x, self.position_y = position
        self.setGeometry(QtCore.QRect(self.position_x, self.position_y, 452, 682))
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 452, 682))
        self.frame.setStyleSheet("background: rgba(24, 24, 24, 0.5);\n"
                                 )
        self.frame_lock_2 = QtWidgets.QFrame(self.frame)
        self.frame_lock_2.setGeometry(QtCore.QRect(10, 200, 421, 201))
        self.frame_lock_2.setStyleSheet("background: #181818;\n"
                                        "border: 1px solid #646464;\n"
                                        "box-sizing: border-box;\n"
                                        "border-radius: 4px;")
        self.frame_lock_2.setObjectName("frame_lock_2")
        self.descr_2 = QtWidgets.QTextBrowser(self.frame_lock_2)
        self.descr_2.setGeometry(QtCore.QRect(50, 60, 181, 71))
        self.descr_2.setStyleSheet("font: 8pt \"NSimSun\";;\n"
                                   "font-weight: 200;\n"
                                   "font-size: 13px;\n"
                                   "line-height: 10px;\n"
                                   "text-decoration-line: underline;\n"
                                   "background: rgba(44, 40, 40, 0.0);\n"
                                   "color: rgba(255, 255, 255, 0.8);\n"
                                   "\n"
                                   "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.descr_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descr_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descr_2.setObjectName("descr_2")
        self.label_2 = QtWidgets.QLabel(self.frame_lock_2)
        self.label_2.setGeometry(QtCore.QRect(250, 22, 101, 131))
        self.label_2.setStyleSheet("background: rgba(44, 40, 40, 0.0);\n"
                                   "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.label_2.setText("")
        self.label_2.setPixmap(QPixmap("../parser/material/Firo_s.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")

        self.descr_2.setHtml(
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'NSimSun\'; font-size:13px; font-weight:200; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">Loading...</span></p>\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Firo: I\'m in a hurry, but you have to wait!</span></p></body></html>")

        threading.Thread(target=self.close_this).start()


    def close_this(self):
        print("qq")
        time.sleep(10)
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
