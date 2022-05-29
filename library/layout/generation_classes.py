import os
import pathlib
import shutil
import time
import webbrowser

import fitz
import keyboard
import qpageview
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import QMouseEvent, QKeySequence
from PyQt5.QtWidgets import QShortcut

from library.layout.dialog_window import Ui_Dialog_folder, ErrorDialog
import library.Neko_lib_sqlite
import sys, os

basedir = os.path.dirname(os.curdir)

class GenerateFolderPage(QtWidgets.QWidget):
    def __init__(self, name_folder, id_folder, list_book, main_obj):
        super(GenerateFolderPage, self).__init__()
        self.config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        print(self.config_name)
        self.flag_sort = self.config_name["flag_sort"]
        self.action_flag = False  # delete folder

        self.name_folder_text = name_folder
        self.id_folder = id_folder
        self.list_book = list_book
        self.main_obj = main_obj
        self.list_del_book = []
        self.setGeometry(QtCore.QRect(0, 0, 802, 621))
        self.lib_sub_right_page_folder = QtWidgets.QWidget(self)
        self.lib_sub_right_page_folder.setStyleSheet("\n"
                                                     "background-color: qlineargradient(spread:pad, x1:1, y1:0.574, x2:1, y2:0, stop:0 rgba(18, 18, 18, 255), stop:1 rgba(32, 32, 32, 255));")
        self.lib_sub_right_page_folder.setObjectName("lib_sub_right_page_folder")
        self.lib_sub_right_page_folder.setMinimumSize(QtCore.QSize(802, 621))
        self.test_container_in_page = QtWidgets.QGroupBox(self.lib_sub_right_page_folder)

        self.test_container_in_page.setGeometry(QtCore.QRect(0, 0, 802, 621))
        self.test_container_in_page.setStyleSheet("border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                                                  "background: linear-gradient(180deg, #202020 0%, #0F0F0F 100%);")
        self.test_container_in_page.setTitle("")
        self.test_container_in_page.setObjectName("test_container_in_page")
        self.area_for_book = QtWidgets.QScrollArea(self.test_container_in_page)
        self.area_for_book.setGeometry(QtCore.QRect(9, 50, 801, 581))
        self.area_for_book.setStyleSheet("padding: 15px 7px  5px 7px;\n"
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
        # self.gridLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.area_for_book.setWidget(self.area_for_book_container)
        self.name_folder = MenuLabel(self.test_container_in_page, self.del_folder, self.type_sort_book)
        self.name_folder.setGeometry(QtCore.QRect(20, 10, 421, 41))
        self.name_folder.setStyleSheet("font-family: \'RobotoFlex\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 200;\n"
                                       "font-size: 26px;\n"
                                       "line-height: 75.4%;\n"
                                       "/* or 14px */\n"
                                       "background: rgba(199, 199, 199, 0.0);\n"
                                       "border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                                       "color: rgba(255, 255, 255, 0.85);\n"
                                       "")

        self.name_folder.setText(self.name_folder_text)
        self.button_add_book = QtWidgets.QPushButton(self.test_container_in_page)
        self.button_add_book.setGeometry(QtCore.QRect(610, 1, 94, 27))
        self.button_add_book.setMinimumSize(QtCore.QSize(91, 22))
        self.button_add_book.setStyleSheet("background: rgba(0, 0, 0, 0.7);\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "font-family: \'RobotoFlex\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 700;\n"
                                           "font-size: 11px;\n"
                                           "line-height: 75.4%;\n"
                                           "padding: 0 0 0 5px;\n"
                                           "/* or 14px */\n"
                                           "text-align: Left;\n"
                                           "border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                                           "color: rgba(255, 255, 255, 0.85);")
        self.button_add_book.setObjectName("button_add_book")
        self.button_add_book.setText("Neko want add")
        """frame del book"""
        self.frame_del_book = QtWidgets.QFrame(self.test_container_in_page)
        self.frame_del_book.setGeometry(QtCore.QRect(0, 555, 801, 66))
        self.frame_del_book.setStyleSheet("background: #111111;\n"
                                          "\n"
                                          "\n"
                                          "border-top: 2px solid rgb(46, 46, 46);")
        self.frame_del_book.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_del_book.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_del_book.setObjectName("frame_del_book")
        self.button_trash = QtWidgets.QPushButton(self.frame_del_book)
        self.button_trash.setGeometry(QtCore.QRect(720, 6, 61, 51))
        self.button_trash.setStyleSheet("background: rgba(149, 149, 149, 0.0);\n"
                                        "border-top:0px solid rgb(46, 46, 46);")
        self.button_trash.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(os.path.join(basedir,"lib_material/trash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_trash.setIcon(icon4)
        self.button_trash.setIconSize(QtCore.QSize(46, 43))
        self.button_trash.setObjectName("button_trash")
        self.frame_del_book.hide()
        "button connect"
        self.button_add_book.clicked.connect(self.chose_book_file)
        self.button_trash.clicked.connect(self.del_book)
        "fun"
        self.load_book(self.list_book)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        try:
            for file in files:
                if pathlib.Path(file).suffix == ".pdf":
                    print("ok")
                    new_dist = os.path.abspath(os.path.join(basedir,"bookshelf"))
                    new_path = shutil.copy(file, new_dist, follow_symlinks=True)
                    conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
                    with conn:
                        id_book = library.Neko_lib_sqlite.create_book(conn, self.get_date_about_book(new_path))
                        self.list_book = library.Neko_lib_sqlite.get_list_book_id(conn, self.id_folder)
                    self.load_book(self.list_book)
                else:
                    print("good try, but app receive only pdf")
        except:
            print("mistake")

    def type_sort_book(self, flag):
        config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        config_name["flag_sort"] = flag
        library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_name)
        self.flag_sort = flag
        self.load_book(self.list_book)

    def del_folder(self):
        try:
            print(id(self.action_flag))
            self.action = Ui_Dialog_folder.get_data(self.main_obj, self.action_flag)
            print(self.action)
            if self.action:
                conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
                library.Neko_lib_sqlite.del_folder(conn, self.id_folder)
                self.main_obj.clearLayout()
                self.main_obj.load_folder()
            else:
                pass
        except:
            self.error_dialog = ErrorDialog(self.main_obj)
            self.error_dialog.exec_()
            pass  # here will be append dialog window with mistake

    def del_book(self):
        conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
        with conn:
            try:
                config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
                for id_book in self.list_del_book:
                    if id_book in config_name["recent_book"]:
                        config_name["recent_book"].remove(id_book)
                    if id_book in config_name["favorites_book"]:
                        config_name["favorites_book"].remove(id_book)
                library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_name)
                self.main_obj.main_page.reload_like_book()
                self.main_obj.main_page.reload_recent_book()
                library.Neko_lib_sqlite.del_books(conn, self.list_del_book)
                "очистить лейаут"
                self.clearLayout(self.gridLayout)
                new_list = library.Neko_lib_sqlite.get_list_book_id(conn, self.id_folder)
                self.list_del_book = []
                self.frame_del_book.hide()
                self.load_book(new_list)
                # for i in new_list:
                #     self.add_book(i)
            except:
                self.error_dialog = ErrorDialog(self.main_obj)
                self.error_dialog.exec_()
                pass  # here will be append dialog window with mistake

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def chose_book_file(self):
        "выбирает файл - копирует - должен возвращать новое расположение"
        try:
            files = QtWidgets.QFileDialog.getOpenFileNames(self, 'Open file', None, "Book (*.pdf )")[0]
            for file in files:
                # print(file)
                new_dist = os.path.join(basedir,"bookshelf")
                new_path = shutil.copy(file, new_dist, follow_symlinks=True)
                print("this", new_path)
                conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
                with conn:
                    id_book = library.Neko_lib_sqlite.create_book(conn, self.get_date_about_book(new_path))
                    self.list_book = library.Neko_lib_sqlite.get_list_book_id(conn, self.id_folder)
                self.load_book(self.list_book)
        except:
            pass
        # return new_path

    def get_date_about_book(self, path):
        book_name = os.path.basename(path)[:-4]
        "get image"
        doc = fitz.open(path)
        page = doc.load_page(0)
        pix = page.get_pixmap()
        pix.save(os.path.join(basedir,f"lib_material/image_for_book/{book_name}.png"))
        "set value"
        book_image_path = os.path.join(basedir,f"lib_material/image_for_book/{book_name}.png")
        book_path = path
        current_page = 0
        return (self.id_folder, book_name, book_path, book_image_path, current_page)

    def load_book(self, list_book):
        self.clearLayout(self.gridLayout)
        if self.flag_sort:
            if list_book:
                for i in list_book[::-1]:
                    self.add_book(i)
        else:
            if list_book:
                for i in list_book:
                    self.add_book(i)

    def add_book(self, id_book):
        try:
            conn = library.Neko_lib_sqlite.create_connection(os.path.join(basedir,"lib.db"))
            with conn:
                self.gridLayout.addWidget(
                    GenerateBook(library.Neko_lib_sqlite.get_book(conn, id_book), self.main_obj, self.frame_del_book,
                                 self.list_del_book))
        except:
            pass


class ShowcaseButton(QtWidgets.QPushButton):
    leftClicked = QtCore.pyqtSignal()
    rightClicked = QtCore.pyqtSignal()
    likeClicked = QtCore.pyqtSignal()

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if (e.button() == QtCore.Qt.MouseButton.LeftButton) and (modifiers == QtCore.Qt.ShiftModifier):
            self.likeClicked.emit()
        elif e.button() == QtCore.Qt.MouseButton.LeftButton:
            self.leftClicked.emit()
        elif e.button() == QtCore.Qt.MouseButton.RightButton:
            self.rightClicked.emit()
        else:
            e.ignore()


class MenuLabel(QtWidgets.QLabel):

    def __init__(self, parent, del_folder_fun, sort_fun):
        super(MenuLabel, self).__init__(parent)
        self.del_folder_fun = del_folder_fun
        self.sort_fun = sort_fun

    def contextMenuEvent(self, event):

        menu = QtWidgets.QMenu(self)
        menu.setStyleSheet("font-family: \'RobotoFlex\';\n"
                           "font-style: normal;\n"
                           "font-weight: 200;\n"
                           "font-size: 16px;\n"
                           "line-height: 75.4%;\n"
                           "/* or 14px */\n"
                           "background: rgba(199, 199, 199, 0.0);\n"
                           "border: 0.5px solid rgba(167, 167, 167, 0.01);\n"
                           "color: rgba(255, 255, 255, 0.85);\n"
                           "")
        Rename = menu.addAction("Rename")
        Delete = menu.addAction("Delete")
        menu_sort = menu.addMenu('Sort')
        Sort_recent = menu_sort.addAction("Sort_recent")
        Sort_late = menu_sort.addAction("Sort_late")
        result = menu.exec_(self.mapToGlobal(event.pos()))
        if Rename == result:
            print("Action")
        elif Delete == result:
            self.del_folder_fun()
        elif Sort_recent == result:
            self.sort_fun(True)
        elif result == result:
            self.sort_fun(False)


class GenerateBook(QtWidgets.QWidget):
    def __init__(self, book_data, window_main_obj, frame_del_book_obj=None, list_del_book=None, ):
        super(GenerateBook, self).__init__()
        # print(book_data)
        self.main_obj = window_main_obj
        self.book_data = book_data
        self.frame_del_book_obj = frame_del_book_obj
        self.id_book, self.book_name, self.book_path, self.book_image_path, self.current_page = book_data
        self.setMinimumSize(QtCore.QSize(221, 311))
        self.test_group_book = QtWidgets.QGroupBox(self)
        self.test_group_book.setMinimumSize(QtCore.QSize(221, 311))
        self.test_group_book.setMaximumSize(QtCore.QSize(221, 311))
        self.test_group_book.setStyleSheet("\n"
                                           "background-color: qlineargradient(spread:pad, x1:1, y1:0.556818, x2:1, y2:0, stop:0 rgba(27, 27, 27, 255), stop:1 rgba(22, 22, 22, 255));\n"
                                           "box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.85);\n"
                                           "border-radius: 8px;\n"
                                           "padding: 0px 20px  20px 20px;")
        self.test_group_book_style_flag = False
        self.test_group_book.setTitle("")
        self.test_group_book.setObjectName("test_group_book")
        self.image_book = QtWidgets.QLabel(self.test_group_book)
        self.image_book.setGeometry(QtCore.QRect(7, 10, 207, 241))
        self.image_book.setStyleSheet("border-radius: 20px;\n"
                                      "padding: 0px;")
        self.image_book.setText("")
        self.image_book.setPixmap(QtGui.QPixmap(self.book_image_path))
        self.image_book.setScaledContents(True)
        self.image_book.setAlignment(QtCore.Qt.AlignCenter)
        self.image_book.setWordWrap(False)
        self.image_book.setObjectName("image_book")
        self.name_book = QtWidgets.QTextBrowser(self.test_group_book)
        self.name_book.setGeometry(QtCore.QRect(20, 249, 171, 46))
        self.name_book.setStyleSheet("font-family: \'Montserrat\';\n"
                                     "font-style: normal;\n"
                                     "font-weight: 400;\n"
                                     "font-size: 12px;\n"
                                     "line-height: 15px;\n"
                                     "padding: 0px;\n"
                                     "color: rgba(255, 255, 255, 0.8); ")
        self.name_book.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_book.setObjectName("name_book")
        self.name_book.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Montserrat\'; font-size:12px; font-weight:400; font-style:normal;\">\n"
            f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt;\">{self.book_name}</span></p></body></html>")
        self.like_mark_label = QtWidgets.QPushButton(self.test_group_book)
        self.like_mark_label.setEnabled(True)
        self.like_mark_label.setGeometry(QtCore.QRect(160, 10, 41, 41))
        self.like_mark_label.setAutoFillBackground(False)
        self.like_mark_label.setStyleSheet("color: #FFFFFF;\n"
                                           "background: rgba(199, 199, 199, 0.0);\n"
                                           "padding: 0;")
        self.like_mark_label.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(os.path.join(basedir,"lib_material/like_mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off))
        self.like_mark_label.setIcon(icon3)
        self.like_mark_label.setIconSize(QtCore.QSize(32, 32))
        self.like_mark_label.setAutoRepeat(False)
        self.like_mark_label.setObjectName("like_mark_label")
        self.showcase_button = ShowcaseButton(self.test_group_book)
        self.showcase_button.setGeometry(QtCore.QRect(0, 0, 221, 311))
        self.showcase_button.setStyleSheet("QPushButton {"
                                           "background: rgba(149, 149, 149, 0.0);}\n"
                                           "QPushButton:hover {\n"
                                           "background: rgba(210, 210, 210, 0.05);}")
        self.showcase_button.setObjectName("showcase_button")
        self.showcase_button.rightClicked.connect(lambda: self.click_on_book(self.frame_del_book_obj, list_del_book))
        self.showcase_button.leftClicked.connect(self.left_click_on_book)
        self.showcase_button.likeClicked.connect(self.add_favorite_book)
        self.like_mark_label.hide()
        self.check_on_like_mark()

    def check_on_like_mark(self):
        config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        if self.id_book in config_name["favorites_book"]:
            self.like_mark_label.show()

        else:
            self.like_mark_label.hide()

    def add_favorite_book(self):
        self.check_on_like_mark()
        if self.main_obj:
            config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
            print(config_name["favorites_book"], self.id_book)
            if self.id_book in config_name["favorites_book"]:
                config_name["favorites_book"].remove(self.id_book)
            else:
                config_name["favorites_book"].append(self.id_book)
            print(config_name["favorites_book"], self.id_book)
            library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_name)
            self.check_on_like_mark()
            self.main_obj.main_page.reload_like_book()
            self.main_obj.main_page.reload_recent_book()

    def left_click_on_book(self):
        try:
            dst = os.path.join(basedir,"bookshelf/pdfjs-2.14.305-dist/web/compressed.tracemonkey-pldi-09.pdf")
            conn = library.Neko_lib_sqlite.create_connection("lib.db")
            with conn:

                data_book = library.Neko_lib_sqlite.get_book(conn, self.id_book)
                print(data_book[1])
            src = os.path.join(basedir,f"{data_book[1]}.pdf")
            print("1")
            print(src,dst)
            shutil.copyfile(src, dst, follow_symlinks=True)
            print("2")
            webbrowser.open("http://localhost:8000/bookshelf/pdfjs-2.14.305-dist/web/viewer.html")
        except:
            print("noo")
        config_names = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        if config_names["flag_f11"]:
            time.sleep(4)
            keyboard.press_and_release('f11')
        if self.main_obj:
            config_name = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))

            if self.id_book in config_name["recent_book"]:
                config_name["recent_book"].remove(self.id_book)
                config_name["recent_book"].insert(0, self.id_book)
            else:
                config_name["recent_book"].insert(0, self.id_book)
            library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_name)
            self.main_obj.main_page.reload_recent_book()

    def click_on_book(self, frame_del_obj, list_del_book):
        if frame_del_obj:
            self.test_group_book_style_flag = not self.test_group_book_style_flag
            if self.test_group_book_style_flag:
                list_del_book.append(self.id_book)
                self.test_group_book.setStyleSheet("\n"
                                                   "background: rgba(255, 255, 255, 0.2);;\n"
                                                   "box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.85);\n"
                                                   "border-radius: 8px;\n"
                                                   "padding: 0px 20px  20px 20px;")
            else:
                self.test_group_book.setStyleSheet("\n"
                                                   "background-color: qlineargradient(spread:pad, x1:1, y1:0.556818, x2:1, y2:0, stop:0 rgba(27, 27, 27, 255), stop:1 rgba(22, 22, 22, 255));\n"
                                                   "box-shadow: 4px 4px 4px rgba(0, 0, 0, 0.85);\n"
                                                   "border-radius: 8px;\n"
                                                   "padding: 0px 20px  20px 20px;")
                list_del_book.remove(self.id_book)
            print(list_del_book)
            if list_del_book:
                frame_del_obj.show()
            else:
                frame_del_obj.hide()


class FolderButton(QtWidgets.QWidget):
    """generation folder button"""

    def __init__(self, name_folder, index_folder, obj_page, obj_frame, obj_main_window):
        super(FolderButton, self).__init__()
        self.index_folder = index_folder
        # print(self.index_folder)
        self.name_folder = name_folder
        self.obj_page = obj_page
        self.obj_main_window = obj_main_window
        self.obj_frame = obj_frame
        self.button_folder = ShowcaseButton(self)
        self.setMinimumSize(QtCore.QSize(156, 28))
        self.button_folder.setMinimumSize(QtCore.QSize(156, 28))
        self.button_folder.setStyleSheet(" QPushButton {"
                                         "background: rgba(149, 149, 149, 0.0);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "font-family: \'Montserrat\';\n"
                                         "font-style: normal;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 14px;\n"
                                         "line-height: 15px;\n"
                                         "text-align: Left;\n"
                                         "padding: 0 0 0 10px;\n"
                                         "color: rgba(255, 255, 255, 0.7);}\n"
                                         "QPushButton:hover {\n"
                                         "color: white;}")
        self.button_folder.setText(self.name_folder)
        self.button_folder.setObjectName(self.name_folder)
        self.button_folder.leftClicked.connect(self.switch_on_page)

    def change_color_btn(self):
        current_folder = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        for w in self.obj_frame.findChildren(FolderButton):
            print(w)
            if current_folder["current_folder"] == w.index_folder:
                w.button_folder.setStyleSheet(" QPushButton {"
                                              "background: rgba(149, 149, 149, 0.0);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "font-family: \'Montserrat\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 15px;\n"
                                              "text-align: Left;\n"
                                              "padding: 0 0 0 10px;\n"
                                              "color: white;}\n"
                                              )
            else:
                w.button_folder.setStyleSheet(" QPushButton {"
                                              "background: rgba(149, 149, 149, 0.0);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "font-family: \'Montserrat\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 14px;\n"
                                              "line-height: 15px;\n"
                                              "text-align: Left;\n"
                                              "padding: 0 0 0 10px;\n"
                                              "color: rgba(255, 255, 255, 0.7);}\n"
                                              "QPushButton:hover {\n"
                                              "color: white;}")

    def switch_on_page(self):
        self.obj_main_window.lib_right.setCurrentIndex(2)
        current_folder = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        current_folder["current_folder"] = self.index_folder
        library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), current_folder)
        self.change_color_btn()
        self.obj_page.setCurrentIndex(self.index_folder)


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=20, hspacing=15, vspacing=20):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, 0, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()


class MenuButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super(MenuButton, self).__init__(parent=parent)
        self.setStyleSheet(" QPushButton {"
                           "background: rgba(149, 149, 149, 0.0);\n"
                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                           "font-family: \'RobotoFlex\';\n"
                           "font-style: normal;\n"
                           "font-weight: 700;\n"
                           "font-size: 12px;\n"
                           "line-height: 15px;\n"
                           "text-align: Left;\n"
                           "padding:  0 0 0 15px;\n"
                           "color: rgba(255, 255, 255, 0.7);}\n"
                           "QPushButton:hover {\n"
                           "color: white;}")
