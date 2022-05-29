import os

from PyQt5 import QtCore, QtGui, QtWidgets
import library.Neko_lib_sqlite
from library.layout.generation_classes import GenerateBook, FlowLayout
basedir = os.path.dirname(os.curdir)

class FindPage(QtWidgets.QWidget):
    def __init__(self):
        super(FindPage, self).__init__()
        self.setGeometry(QtCore.QRect(0, 0, 802, 621))
        self.setStyleSheet("\n"
                           "background-color: qlineargradient(spread:pad, x1:1, y1:0.574, x2:1, y2:0, stop:0 rgba(18, 18, 18, 255), stop:1 rgba(32, 32, 32, 255));")

        self.page_find_book = QtWidgets.QWidget(self)
        self.page_find_book.setObjectName("page_find_book")
        self.area_for_find_book = QtWidgets.QScrollArea(self.page_find_book)
        self.area_for_find_book.setGeometry(QtCore.QRect(0, 80, 801, 541))
        self.area_for_find_book.setStyleSheet("padding: 15px 7px  5px 7px;\n"
                                              "border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                                              "background: rgba(199, 199, 199, 0.0);\n"
                                              "margin: 0 5px 10px 5px;")
        self.area_for_find_book.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_find_book.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_find_book.setWidgetResizable(True)
        self.area_for_find_book.setObjectName("area_for_find_book")
        self.area_for_find_book_container_2 = QtWidgets.QWidget()
        self.area_for_find_book_container_2.setGeometry(QtCore.QRect(0, 0, 769, 509))
        self.area_for_find_book_container_2.setObjectName("area_for_find_book_container_2")
        self.gridLayout_2 = FlowLayout(self.area_for_find_book_container_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.area_for_find_book.setWidget(self.area_for_find_book_container_2)
        self.find_line = QtWidgets.QLineEdit(self.page_find_book)
        self.find_line.setGeometry(QtCore.QRect(35, 22, 641, 36))
        self.find_line.setStyleSheet("background: #FBFBFB;\n"
                                     "font-family: \'Roboto Mono\';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "font-size: 16px;\n"
                                     "line-height: 75.4%;\n"
                                     "/* or 12px */\n"
                                     "border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                                     "border-radius: 6px;\n"
                                     "color: #1C1C1C;")
        self.find_line.setText("")
        self.find_line.setObjectName("find_line")
        self.button_clear_find_page = QtWidgets.QPushButton(self.page_find_book)
        self.button_clear_find_page.setGeometry(QtCore.QRect(640, 25, 31, 31))
        self.button_clear_find_page.setStyleSheet("color: #434343;\n"
                                                  "background: rgba(199, 199, 199, 0.0);\n"
                                                  "font-size: 18px;\n"
                                                  "border-top:0px solid rgb(46, 46, 46);")
        self.button_clear_find_page.setObjectName("button_clear_find_page")
        self.frame_no_result = QtWidgets.QFrame(self.page_find_book)
        self.frame_no_result.setGeometry(QtCore.QRect(126, 148, 465, 89))
        self.frame_no_result.setStyleSheet("background: #121212;")
        self.frame_no_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_no_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_no_result.setObjectName("frame_no_result")
        self.find_label = QtWidgets.QLabel(self.frame_no_result)
        self.find_label.setGeometry(QtCore.QRect(110, 20, 231, 20))
        self.find_label.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 24px;\n"
                                      "line-height: 75.4%;\n"
                                      "/* or 12px */\n"
                                      "\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.find_label.setAlignment(QtCore.Qt.AlignCenter)
        self.find_label.setObjectName("find_label")
        self.find_label_2 = QtWidgets.QLabel(self.frame_no_result)
        self.find_label_2.setGeometry(QtCore.QRect(120, 50, 231, 20))
        self.find_label_2.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "font-size: 16px;\n"
                                        "line-height: 75.4%;\n"
                                        "/* or 12px */\n"
                                        "\n"
                                        "color: #969C9D;")
        self.find_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.find_label_2.setObjectName("find_label_2")
        self.find_line.setPlaceholderText(" Find a book on the shelf...")
        self.button_clear_find_page.setText("X")
        self.find_label.setText("No result")
        self.find_label_2.setText("Alas, Neko didn\'t find anything.")
        self.find_line.textChanged.connect(self.show_book)
        self.button_reboot = QtWidgets.QPushButton(self.page_find_book)
        self.button_reboot.setGeometry(QtCore.QRect(693, 25, 41, 31))
        self.button_reboot.setStyleSheet("color: #434343;\n"
                                         "background: rgba(199, 199, 199, 0.0);\n"
                                         "font-size: 18px;\n"
                                         "border-top:0px solid rgb(46, 46, 46);")
        self.button_reboot.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(basedir,"lib_material/reboot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_reboot.setIcon(icon4)
        self.button_reboot.setIconSize(QtCore.QSize(31, 29))
        self.button_reboot.setObjectName("button_reboot")
        self.button_reboot.clicked.connect(self.reboot_book)
        conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
        with conn:
            self.list_book = library.Neko_lib_sqlite.get_all_book(conn)
        self.frame_del_book, self.list_del_book = [], []

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def reboot_book(self):
        conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
        with conn:
            self.list_book = library.Neko_lib_sqlite.get_all_book(conn)

    def add_book(self, id_book):
        conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
        with conn:
            self.gridLayout_2.addWidget(
                GenerateBook(library.Neko_lib_sqlite.get_book(conn, id_book), self.frame_del_book, self.list_del_book))

    def show_book(self):
        # print(self.find_line.text())
        self.clearLayout(self.gridLayout_2)
        amount = 0
        for i, book in enumerate(self.list_book):
            if (self.find_line.text() in book[2]) and (self.find_line.text() != ""):
                # print(book)
                self.add_book(book[1])
                self.frame_no_result.hide()
                amount += 1
        if not amount:
            self.frame_no_result.show()
