from PyQt5 import QtCore, QtGui, QtWidgets
import library.Neko_lib_sqlite
from library.layout.dialog_window import ErrorDialog
from library.layout.generation_classes import FlowLayout, GenerateBook
import sys, os

basedir = os.path.abspath(os.curdir)
print(basedir)
class MainPage(QtWidgets.QWidget):
    def __init__(self, main_obj):
        super(MainPage, self).__init__()
        self.setGeometry(QtCore.QRect(0, 0, 802, 621))
        self.main_obj = main_obj
        self.setStyleSheet("\n"
                           "background-color: qlineargradient(spread:pad, x1:1, y1:0.574, x2:1, y2:0, stop:0 rgba(18, 18, 18, 255), stop:1 rgba(32, 32, 32, 255));")
        self.stack_main = QtWidgets.QStackedWidget(self)
        self.stack_main.setGeometry(QtCore.QRect(0, 0, 801, 621))
        self.page_main_book = QtWidgets.QWidget()
        self.page_main_book.setObjectName("page_main_book")
        self.area_for_main_book = QtWidgets.QScrollArea(self.page_main_book)
        self.area_for_main_book.setGeometry(QtCore.QRect(0, 0, 801, 621))
        self.area_for_main_book.setStyleSheet(
            "border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
            "background: rgba(199, 199, 199, 0.0);\n"
        )
        self.area_for_main_book.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_main_book.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_main_book.setWidgetResizable(True)
        self.area_for_main_book.setObjectName("area_for_main_book")
        self.area_for_main_book_container_2 = QtWidgets.QWidget()
        self.area_for_main_book_container_2.setGeometry(QtCore.QRect(0, 0, 769, 509))
        self.area_for_main_book_container_2.setObjectName("area_for_main_book_container_2")
        self.sub_book_layout = QtWidgets.QVBoxLayout(self.area_for_main_book_container_2)
        self.sub_book_layout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.sub_book_layout.setObjectName("sub_book_layout")
        self.area_for_main_book.setWidget(self.area_for_main_book_container_2)

        "widget"
        self.resent_book_area = AreaBookPos3("Recent", self.stack_main, 1)
        self.resent_book_area_more = AreaBookPos_more("Recent", self.stack_main)
        self.like_book_area = AreaBookPos3("Like", self.stack_main, 2)
        self.like_book_area_more = AreaBookPos_more("Like", self.stack_main)
        self.sub_book_layout.addWidget(self.resent_book_area)
        self.sub_book_layout.addWidget(self.like_book_area)
        self.stack_main.addWidget(self.page_main_book)
        self.stack_main.addWidget(self.resent_book_area_more)  # more recent
        self.stack_main.addWidget(self.like_book_area_more)  # more favorite
        self.stack_main.setCurrentIndex(0)
        self.load_page()

    def load_page(self):
        config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        # self.clearLayout(self.sub_book_layout)
        if config_name["recent_book"]:
            for id_book in config_name["recent_book"][:15]:
                self.add_book(self.resent_book_area.gridLayout, id_book)
                self.add_book(self.resent_book_area_more.gridLayout, id_book)
        else:
            self.resent_book_area.gridLayout.addWidget(NoBook())
        if config_name["favorites_book"]:
            for id_book in config_name["favorites_book"]:
                self.add_book(self.like_book_area.gridLayout, id_book)
                self.add_book(self.like_book_area_more.gridLayout, id_book)
        else:
            # self.like_book_area.gridLayout.setAlignment(QtCore.Qt.AlignCenter)
            self.like_book_area.gridLayout.addWidget(NoBook())

    def reload_like_book(self):
        config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        self.clearLayout(self.like_book_area.gridLayout)
        self.clearLayout(self.like_book_area_more.gridLayout)
        if config_name["favorites_book"]:
            for id_book in config_name["favorites_book"]:
                self.add_book(self.like_book_area.gridLayout, id_book)
                self.add_book(self.like_book_area_more.gridLayout, id_book)
        else:
            # self.like_book_area.gridLayout.setAlignment(QtCore.Qt.AlignCenter)
            self.like_book_area.gridLayout.addWidget(NoBook())

    def reload_recent_book(self):
        config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        self.clearLayout(self.resent_book_area.gridLayout)
        self.clearLayout(self.resent_book_area_more.gridLayout)
        if config_name["recent_book"]:
            for id_book in config_name["recent_book"][:15]:
                self.add_book(self.resent_book_area.gridLayout, id_book)
                self.add_book(self.resent_book_area_more.gridLayout, id_book)
        else:
            self.resent_book_area.gridLayout.addWidget(NoBook())

    def add_book(self, obj_layout, id_book):
        try:
            conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
            self.obj_layout = obj_layout
            with conn:
                self.obj_layout.addWidget(
                    GenerateBook(library.Neko_lib_sqlite.get_book(conn, id_book), self.main_obj))
        except:
            config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
            if id_book in config_name["recent_book"]:
                config_name["recent_book"].remove(id_book)
            elif id_book in config_name["favorites_book"]:
                config_name["favorites_book"].remove(id_book)
            else:
                conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
                library.Neko_lib_sqlite.del_books(conn, [id_book])
                self.error_dialog = ErrorDialog(self.main_obj)
                self.error_dialog.exec_()

            #  если в конфиге нет то удалить из бд, впролне правдоподобно

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()


class NoBook(QtWidgets.QWidget):
    def __init__(self):
        super(NoBook, self).__init__()
        self.setMinimumSize(QtCore.QSize(791, 371))
        self.setStyleSheet("background: #0E0E0E;")
        self.frame_no_result = QtWidgets.QFrame(self)
        self.frame_no_result.setGeometry(QtCore.QRect(250, 100, 200, 70))

        self.frame_no_result.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_no_result.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_no_result.setObjectName("frame_no_result")
        self.find_label = QtWidgets.QLabel(self.frame_no_result)
        self.find_label.setGeometry(QtCore.QRect(0, 0, 200, 60))
        self.find_label.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 24px;\n"
                                      "line-height: 75.4%;\n"
                                      "/* or 12px */\n"
                                      "\n"
                                      "\n"
                                      "color: rgba(255, 255, 255, 0.5);")
        self.find_label.setAlignment(QtCore.Qt.AlignCenter)
        self.find_label.setObjectName("find_label")
        self.find_label.setText("No book")


class AreaBookPos3(QtWidgets.QWidget):
    def __init__(self, name_page, obj_stackwidget=None, id_switch=None):
        super(AreaBookPos3, self).__init__()
        self.setMinimumSize(QtCore.QSize(791, 371))
        self.name_page = name_page
        self.container = QtWidgets.QWidget(self)
        self.obj_stackwidget = obj_stackwidget
        self.id_switch = id_switch
        self.container.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.container.setStyleSheet("background: rgba(167, 167, 167, 0.0);\n"
                                     )
        self.book_container = QtWidgets.QGroupBox(self.container)
        self.book_container.setGeometry(QtCore.QRect(0, 0, 801, 371))
        self.book_container.setStyleSheet("border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                                          )
        self.book_container.setTitle("")
        self.book_container.setObjectName("book_container")
        self.name_container = QtWidgets.QTextBrowser(self.book_container)
        self.name_container.setGeometry(QtCore.QRect(20, 10, 421, 51))
        self.name_container.setStyleSheet("font-family: \'RobotoFlex\';\n"
                                          "font-style: normal;\n"
                                          "font-weight: 200;\n"
                                          "font-size: 13px;\n"
                                          "line-height: 75.4%;\n"
                                          "/* or 14px */\n"
                                          "background: rgba(199, 199, 199, 0.0);\n"
                                          "border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                                          "color: rgba(255, 255, 255, 0.85);\n"
                                          "")
        self.name_container.setObjectName("qq")
        self.area_for_book = QtWidgets.QScrollArea(self.book_container)
        self.area_for_book.setGeometry(QtCore.QRect(0, 38, 750, 361))

        self.area_for_book.setStyleSheet("border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                                         "padding: 15px 7px  5px 7px;\n"
                                         "background: rgba(199, 199, 199, 0.0);\n"
                                         )
        self.area_for_book.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_book.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_for_book.setWidgetResizable(True)
        self.area_for_book.setObjectName("area_for_book")
        self.area_for_book_container = QtWidgets.QWidget()
        self.area_for_book_container.setGeometry(QtCore.QRect(0, 0, 801, 549))
        self.area_for_book_container.setObjectName("area_for_book_container")
        self.gridLayout = FlowLayout(self.area_for_book_container)
        self.gridLayout.setObjectName("gridLayout")
        self.area_for_book.setWidget(self.area_for_book_container)
        self.name_container.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'RobotoFlex\'; font-size:13px; font-weight:200; font-style:normal;\">\n"
            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">{self.name_page}</span></p></body></html>")
        self.button_all = QtWidgets.QPushButton(self.book_container)
        self.button_all.setGeometry(QtCore.QRect(710, 20, 41, 23))
        self.button_all.setStyleSheet(" QPushButton {"
                                      "color: rgba(255, 255, 255, 0.7);\n"
                                      "text-decoration: underline;\n"
                                      "font: 75 8pt \"Arial\";\n"
                                      "text-decoration: underline;\n"
                                      "font: 8pt \"MS Shell Dlg 2\";\n"
                                      "background: rgba(199, 199, 199, 0.0);\n"
                                      "font-family: \'RobotoFlex\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 400;\n"
                                      "font-size: 18px;\n"
                                      "letter-spacing: 0.115em;}"
                                      "QPushButton:hover {\n"
                                      "color: white;}"
                                      )
        self.button_all.setObjectName("button_all")
        self.button_all.setText("All")
        self.button_all.clicked.connect(lambda: self.obj_stackwidget.setCurrentIndex(self.id_switch))


class AreaBookPos_more(AreaBookPos3):
    def __init__(self, name_page, obj_stackwidget):
        super(AreaBookPos_more, self).__init__(name_page, obj_stackwidget)
        # super(AreaBookPos_more, self).__init__(name_page, obj_stackwidget)
        self.obj_stackwidget = obj_stackwidget
        self.id_switch = 0
        self.container.setGeometry(QtCore.QRect(10, 10, 801, 612))
        self.book_container.setGeometry(QtCore.QRect(0, 0, 801, 612))
        self.area_for_book.setGeometry(QtCore.QRect(0, 38, 801, 590))
        self.button_all.setText("Back")
        self.button_all.clicked.connect(lambda: self.obj_stackwidget.setCurrentIndex(self.id_switch))
