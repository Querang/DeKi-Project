import sys
import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import schedule
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QSystemTrayIcon, QStyle, QAction, QMenu, qApp
from PyQt5 import QtCore
from PyQt5.uic.properties import QtGui

from layout.main_layout import Ui_MainWindow
from layout.template_layout import Dialog_get_date, FlowLayout
import Firo_parse_sqlite
import layout.template_layout
import threading


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, window_notify):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setupUi(self)
        self.show()
        self.serfing_button.clicked.connect(self.get_parse_date)
        self.window_notify = window_notify
        # self.get_parse_date()
        self.conn = Firo_parse_sqlite.create_connection("parse_.db")
        """function"""
        # ww = threading.Thread(target= create_main2)
        # ww.start()
        self.load_label()
        # self.ProgressBar()
        self.button_X.clicked.connect(self.hide)
        self.tray_icon = QSystemTrayIcon(self)
        icon = QIcon()
        icon.addPixmap(QPixmap("../parser/material/Firo_parser.png"), QIcon.Normal,
                       QIcon.Off)
        self.tray_icon.setIcon(icon)
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(self.close_app)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()


    def close_app(self):
        self.connect_sub()
        sys.exit()

    def load_label(self):
        with self.conn:
            data = Firo_parse_sqlite.get_data(self.conn)
            for item in data:
                self.verticalLayout_2.addWidget(
                    layout.template_layout.GenerateParseLabel(self, item, self.window_notify))

    # def connect(self):
    #     schedule.every(10).seconds.do(self.connect_sub)
    #     while True:
    #         schedule.run_pending()
    #         time.sleep(1)
    #
    def connect_sub(self):
        while self.verticalLayout_2.count():
            child = self.verticalLayout_2.takeAt(0)
            if child.widget():
                if child.widget().hand:
                    child.widget().hand.kill()

    def get_parse_date(self):
        self.dialog_date = Dialog_get_date(self, [self.geometry().x(), self.geometry().y()], self.window_notify)
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

        # self.descr_2.setHtml(
        #                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        #                                 "p, li { white-space: pre-wrap; }\n"
        #                                 "</style></head><body style=\" font-family:\'NSimSun\'; font-size:13px; font-weight:200; font-style:normal;\">\n"
        #                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">Loading...</span></p>\n"
        #                                 "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
        #                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Firo: I\'m in a hurry, but you have to wait!</span></p></body></html>")
        thread = DummyThread(self)
        thread.start()
        thread.finished.connect(lambda: self.loading())
        self.point = "Loading."
        threading.Thread(target=self.close_this).start()

    def close_this(self):
        time.sleep(15)
        self.close()

    def loading(self):
        self.descr_2.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            f"</style></head><body style=\" font-family:\'NSimSun\'; font-size:13px; font-weight:200; font-style:normal;\">\n"
            f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13px;\">{self.point}</span></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Firo: I\'m in a hurry, but you have to wait!</span></p></body></html>")
        self.point = self.point + "."
        if self.point == "Loading....":
            self.point = "Loading."


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool | QtCore.Qt.WindowStaysOnTopHint)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        desktop = QtWidgets.QApplication.desktop()
        self.setGeometry(QtCore.QRect(desktop.width() - 230, 40, 180, 60))
        self.show()
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_container_area = QtWidgets.QFrame(self.centralwidget)
        self.frame_container_area.setGeometry(QtCore.QRect(0, 0, 451, 321))
        self.frame_container_area.setMinimumSize(QtCore.QSize(451, 321))
        self.frame_container_area.setMaximumSize(QtCore.QSize(451, 521))
        self.frame_container_area.setStyleSheet("background: rgba(44, 40, 40, 0.0);")
        self.frame_container_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_container_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_container_area.setObjectName("frame_container_area")
        self.area_for_item = QtWidgets.QScrollArea(self.frame_container_area)
        self.area_for_item.setGeometry(QtCore.QRect(0, 0, 416, 501))
        self.area_for_item.setMinimumSize(QtCore.QSize(416, 300))
        self.area_for_item.setMaximumSize(QtCore.QSize(416, 501))
        self.area_for_item.setStyleSheet("background: rgba(44, 40, 40, 0.0);\n"
                                         "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.area_for_item.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_item.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_item.setWidgetResizable(True)
        self.area_for_item.setObjectName("area_for_item")
        self.area_for_item_container = QtWidgets.QWidget()
        self.area_for_item_container.setGeometry(QtCore.QRect(0, 0, 414, 499))
        self.area_for_item_container.setObjectName("area_for_item_container")
        self.verticalLayout_2 = FlowLayout(self.area_for_item_container)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.area_for_item.setWidget(self.area_for_item_container)
        self.scroll_label = QtWidgets.QLabel(self.frame_container_area)
        self.scroll_label.setGeometry(QtCore.QRect(435, 20, 4, 450))
        self.scroll_label.setStyleSheet("background: #0C0C0C;")
        self.scroll_label.setObjectName("scroll_label")
        self.verticalLayout_2.addWidget(QtWidgets.QPushButton())
        self.setCentralWidget(self.centralwidget)


class DummyThread(QThread):
    finished = pyqtSignal()

    def run(self):
        while True:
            self.finished.emit()
            time.sleep(1)


# class DummyThread(QThread):
#     a = Ui_MainWindow()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    a = Ui_MainWindow()
    w = MainWindow(a)
    app.setWindowIcon(QIcon('../parser/lib_material/Firo_parser.png'))

    sys.exit(app.exec_())
