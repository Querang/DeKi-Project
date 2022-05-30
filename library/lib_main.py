import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from library.layout.generation_classes import FolderButton, GenerateFolderPage
from library import Neko_lib_sqlite
from library.layout.lib_layout_main import Ui_MainWindow
from library.layout.main_page import MainPage
from multiprocessing import Process
from multiprocessing import freeze_support
import http.server
import socketserver
from library.layout.dialog_window import SettingDialog, TutorialDialog, ErrorDialog
import traceback
from sqlite3 import Error
basedir = os.path.abspath(os.curdir)
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        """show/hide"""
        self.show()
        self.frame_folder_add.hide()
        """ button in lib_sub_left_fram_top"""
        self.button_find.clicked.connect(lambda: self.lib_right.setCurrentIndex(1))
        self.button_main_folder.clicked.connect(lambda: self.lib_right.setCurrentIndex(0))
        self.button_create_folder_flag = False
        self.button_create_folder.clicked.connect(
            lambda: self.frame_folder_add.show() if self.frame_folder_add.isHidden() else self.frame_folder_add.hide())
        self.button_save_folder.clicked.connect(self.save_folder)
        """button connect in top_bar"""
        # self.button_X.clicked.connect(lambda: sys.exit())
        self.button_X.clicked.connect(self.close_app)
        self.button_swap.clicked.connect(lambda: self.showMinimized())
        self.button_setting.clicked.connect(self.setting_frame)
        self.tutorial_button.clicked.connect(self.tutorial_dialog)
        """fun load"""
        self.load_folder()
        self.server_process = Process(target=server)
        self.server_process.start()
        "main page"
        self.main_page = MainPage(self)
        self.lib_right.insertWidget(0, self.main_page)
        self.lib_right.setCurrentIndex(0)
        # self.setting_frame()

    def save_folder(self):
        try:
            name_folder = self.folder_name_input.text()
            conn = Neko_lib_sqlite.create_connection("lib.db")
            with conn:
                """get resource"""
                id_folder = Neko_lib_sqlite.create_folder(conn, name_folder)
                print(id_folder)
            """add button folder"""
            self.verticalLayout_4.addWidget(
                FolderButton(name_folder, id_folder, self.lib_sub_right, self.lib_sub_left_frame_down, self))
            """add new page"""
            self.lib_sub_right.insertWidget(id_folder, GenerateFolderPage(name_folder, id_folder, [], self))
            self.lib_sub_right.setCurrentIndex(id_folder)
        except Error:
            tb = traceback.format_exc()
            QtWidgets.QMessageBox.information(self,"",tb)
            # self.error_dialog = ErrorDialog(self)
            # self.error_dialog.exec_()



    def close_app(self):
        config_name = Neko_lib_sqlite.read_config("lib_config.yaml")
        (config_name["window_position_x"], config_name["window_position_y"]) = self.geometry().x(), self.geometry().y()
        Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_name)
        self.server_process.kill()
        sys.exit()

    def load_folder(self):
        conn = Neko_lib_sqlite.create_connection("lib.db")
        with conn:
            """get resource"""
            all_folder = Neko_lib_sqlite.get_all_folder_and_id(conn)
            if all_folder:
                need_amount_pages = all_folder[-1][0]
            else:
                need_amount_pages = 0
            for i in range(need_amount_pages):
                self.lib_sub_right.addWidget(QtWidgets.QWidget())
        for (id, folder_name) in all_folder:
            list_book = Neko_lib_sqlite.get_list_book_id(conn, id)
            """add button folder"""
            self.verticalLayout_4.addWidget(
                FolderButton(folder_name, id, self.lib_sub_right, self.lib_sub_left_frame_down, self))
            """add new page"""
            self.lib_sub_right.insertWidget(id, GenerateFolderPage(folder_name, id, list_book, self))
            self.lib_sub_right.setCurrentIndex(id)

    def clearLayout(self):
        while self.verticalLayout_4.count():
            child = self.verticalLayout_4.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def setting_frame(self):
        self.set_dialog = SettingDialog(self)
        self.set_dialog.exec_()

    def tutorial_dialog(self):
        self.tu_dialog = TutorialDialog(self)
        self.tu_dialog.exec_()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MiddleButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


def server():
    PORT = 7000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == '__main__':
    freeze_support()
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.setWindowIcon(QtGui.QIcon(os.path.join(basedir,'lib_material/icon_window.png')))
    # app.setQuitOnLastWindowClosed(True)
    w = MainWindow()
    sys.exit(app.exec_())
