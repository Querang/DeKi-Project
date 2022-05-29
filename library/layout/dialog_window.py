import os
import shutil
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QShortcut, QFileDialog

import library.Neko_lib_sqlite
import sys, os

basedir = os.path.dirname(os.curdir)

class Ui_Dialog_folder(QtWidgets.QDialog):
    def __init__(self, parent, button_continue_flag):
        super(Ui_Dialog_folder, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(QtCore.QRect(170, 300, 161, 116))
        self.button_continue_flag = button_continue_flag
        print(id(self.button_continue_flag))
        self.dialog_frame_folder_del = QtWidgets.QFrame(self)
        self.dialog_frame_folder_del.setGeometry(QtCore.QRect(0, 0, 161, 116))
        self.dialog_frame_folder_del.setStyleSheet("background: rgba(23, 23, 23, 0.95);\n"
                                                   "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                   "border-radius: 13px;")

        self.label_q = QtWidgets.QLabel(self.dialog_frame_folder_del)
        self.label_q.setGeometry(QtCore.QRect(20, 10, 121, 61))
        print("hi")
        self.label_q.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                   "font-family: \'Roboto Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 14px;\n"
                                   "line-height: 18px;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.label_q.setObjectName("label_q")
        self.button_continue = QtWidgets.QPushButton(self.dialog_frame_folder_del)
        self.button_continue.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.button_continue.setStyleSheet("QPushButton {\n"
                                           "font-family: \'Roboto Mono\';\n"
                                           "font-style: normal;\n"
                                           "font-weight: 400;\n"
                                           "font-size: 16px;\n"
                                           "line-height: 18px;\n"
                                           "color: rgba(255, 255, 255, 0.8);background: rgba(23, 23, 23, 0.0);}\n"
                                           "QPushButton:hover{\n"
                                           "color: rgba(255, 255, 255, 1.0)\n"
                                           "}")
        self.button_back = QtWidgets.QPushButton(self.dialog_frame_folder_del)
        self.button_back.setGeometry(QtCore.QRect(90, 80, 51, 23))
        self.button_back.setStyleSheet("QPushButton {\n"
                                       "font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 16px;\n"
                                       "line-height: 18px;\n"
                                       "color: rgba(255, 255, 255, 0.8);background: rgba(23, 23, 23, 0.0);}\n"
                                       "QPushButton:hover{\n"
                                       "color: rgba(255, 255, 255, 1.0)\n"
                                       "}")
        self.button_back.setObjectName("button_back")
        self.label_q.setText("Are you \n"
                             "  sure?   (=｀ω´=)")
        self.button_continue.setText("continue")
        self.button_back.setText("back")
        self.button_back.clicked.connect(lambda: self.close())
        self.button_continue.clicked.connect(self.del_folder)

    def del_folder(self):
        self.button_continue_flag = True
        print(id(self.button_continue_flag))
        self.close()

    @staticmethod
    def get_data(parent, button_continue_flag):
        dialog = Ui_Dialog_folder(parent, button_continue_flag)
        dialog.exec_()
        return dialog.button_continue_flag


class SettingDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(SettingDialog, self).__init__(parent=parent)
        self.parent = parent
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(QtCore.QRect(457, 93, 277, 357))
        config_names = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        self.setStyleSheet("background: #1F1F1F;border: 1px solid #727272;")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 181, 51))
        self.textBrowser.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 16px;\n"
                                       "line-height: 75.4%;\n"
                                       "/* or 12px */\n"
                                       "\n"
                                       "color: #969C9D;\n"
                                       "background: rgba(199, 199, 199, 0.0);\n"
                                       "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.textBrowser.setObjectName("textBrowser")
        self.set1 = CheckMyBox(self)
        self.set1.setGeometry(QtCore.QRect(230, 26, 21, 31))

        self.set1.setIconSize(QtCore.QSize(22, 21))
        self.set1.setObjectName("set1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 97, 201, 51))
        self.textBrowser_2.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                         "font-style: normal;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 16px;\n"
                                         "line-height: 75.4%;\n"
                                         "/* or 12px */\n"
                                         "\n"
                                         "color: #969C9D;\n"
                                         "background: rgba(199, 199, 199, 0.0);\n"
                                         "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 65, 181, 31))
        self.textBrowser_3.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                         "font-style: normal;\n"
                                         "font-weight: 400;\n"
                                         "font-size: 16px;\n"
                                         "line-height: 75.4%;\n"
                                         "/* or 12px */\n"
                                         "\n"
                                         "color: #969C9D;\n"
                                         "background: rgba(199, 199, 199, 0.0);\n"
                                         "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.set2 = CheckMyBox(self)
        self.set2.setEnabled(True)
        self.set2.setGeometry(QtCore.QRect(230, 66, 21, 31))
        self.set2.setCheckable(True)
        self.set2.setObjectName("set2")
        self.set3 = CheckMyBox(self)
        self.set3.setEnabled(True)
        self.set3.setGeometry(QtCore.QRect(230, 96, 21, 31))
        self.set3.setIconSize(QtCore.QSize(22, 21))
        self.set3.setCheckable(True)
        if config_names["flag_pos"]:
            self.set1.setChecked(True)
        if config_names["flag_sort"]:
            self.set2.setChecked(True)
        if config_names["flag_f11"]:
            self.set3.setChecked(True)
        self.button_export = MenuButton(self)
        self.button_export.setGeometry(QtCore.QRect(80, 310, 121, 23))

        self.button_swap = QtWidgets.QPushButton(self)
        self.button_swap.setGeometry(QtCore.QRect(250, 0, 31, 23))
        self.button_swap.setStyleSheet("color: #FFFFFF;\n"
                                       "background: rgba(199, 199, 199, 0.0);border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.button_swap.setObjectName("button_swap")
        self.button_swap.clicked.connect(lambda: self.close())

        QtCore.QMetaObject.connectSlotsByName(self)
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Remember the position of the window?</span></p></body></html>")
        self.textBrowser_2.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Use F11, when book load?</span></p></body></html>")
        self.textBrowser_3.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Sort by recent</span></p></body></html>")
        self.button_export.setText("export book")
        self.button_swap.setText("X")
        self.set1.stateChanged.connect(
            lambda: self.change_setting("flag_pos", True) if self.set1.isChecked() else self.change_setting("flag_pos",
                                                                                                            False))
        self.set2.stateChanged.connect(
            lambda: self.change_setting("flag_sort", True) if self.set2.isChecked() else self.change_setting(
                "flag_sort",
                False))
        self.set3.stateChanged.connect(
            lambda: self.change_setting("flag_f11", True) if self.set3.isChecked() else self.change_setting("flag_f11",
                                                                                                            False))
        self.button_export.clicked.connect(self.copy_books)

    def change_setting(self, config_name, flag):
        config_names = library.Neko_lib_sqlite.read_config(os.path.join(basedir,"lib_config.yaml"))
        if flag:
            config_names[config_name] = True
        else:
            config_names[config_name] = False
        library.Neko_lib_sqlite.write_config(os.path.join(basedir,"lib_config.yaml"), config_names)

    def copy_books(self):
        try:
            folder = self.get_directory()
            new_dist = folder + "/neko_lib"
            os.mkdir(new_dist)
            print("qq")
            for root, dirs, files in os.walk(os.path.abspath(os.path.join(basedir,"bookshelf"))):
                print(root, dirs, files)
                for file in files:
                    print(os.path.join(root, file))
                    if (file.endswith(".pdf")):
                        print(os.path.join(root, file))
                        shutil.copy(os.path.join(root, file), new_dist, follow_symlinks=True)
        except:
            self.error_dialog = ErrorDialog(self.parent)
            self.error_dialog.exec_()
            pass

    def get_directory(self):  # <-----
        return QFileDialog.getExistingDirectory(self, "Выбрать папку", ".")


class TutorialDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(TutorialDialog, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(QtCore.QRect(457, 93, 277, 357))
        self.setStyleSheet("background: #202020;")
        self.textBrowser = QtWidgets.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 241, 311))
        self.textBrowser.setStyleSheet("font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 16px;\n"
                                       "line-height: 75.4%;\n"
                                       "/* or 12px */\n"
                                       "\n"
                                       "color: #969C9D;\n"
                                       "background: rgba(199, 199, 199, 0.0);\n"
                                       "border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.textBrowser.setObjectName("textBrowser")
        QtCore.QMetaObject.connectSlotsByName(self)
        self.button_swap = QtWidgets.QPushButton(self)
        self.button_swap.setGeometry(QtCore.QRect(250, 0, 31, 23))
        self.button_swap.setStyleSheet("color: #FFFFFF;\n"
                                       "background: rgba(199, 199, 199, 0.0);border: 0.5px solid rgba(167, 167, 167, 0.0);")
        self.button_swap.setObjectName("button_swap")
        self.button_swap.clicked.connect(lambda: self.close())
        self.button_swap.setText("X")
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Roboto Mono\'; font-size:16px; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline;\">Hotkey</span></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Ctrl+w - wrap application</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Ctrl+f - show add folder </span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px;\">Ctrl+x - close application</span></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; text-decoration: underline;\">Neko hints </span><span style=\" font-size:16px;\">: if the book does not load, then click F5</span></p>\n"
            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16px; text-decoration: underline;\">Neko hints </span><span style=\" font-size:16px;\">: right click on the folder name on the page</span></p></body></html>")


class CheckMyBox(QtWidgets.QCheckBox):
    def __init__(self, parent):
        super(CheckMyBox, self).__init__(parent=parent)
        self.setStyleSheet("\n"
                           "QCheckBox  \n"
                           "{\n"
                           # "color: rgba(255, 255, 255, 0.8);\n"
                           # "background: rgba(199, 199, 199, 0.0);\n"
                           "border: 0.5px solid rgba(167, 167, 167, 0.0);\n"
                           "}\n"
                           "QCheckBox::indicator\n"
                           "{\n"
                           # "background-color:  rgba(199, 199, 199, 0.0);\n"
                           # "border: 1px solid rgba(255, 255, 255, 0.2);\n"
                           "width: 16px; height: 16px;"
                           "}\n"
                           # " QCheckBox::indicator:unchecked {"
                           #   " image: url(:.../lib_material/arrow.png);}"
                           )
        self.setText("")


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
                           "border: 0.5px solid rgba(167, 167, 167, 0.0);"
                           "color: rgba(255, 255, 255, 0.7);}\n"
                           "QPushButton:hover {\n"
                           "color: white;}")


class ErrorDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(ErrorDialog, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(QtCore.QRect(470, 300, 161, 116))
        self.setStyleSheet("background: rgba(23, 23, 23, 0.95);\n"
                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                           "border-radius: 13px;")
        self.label_q = QtWidgets.QLabel(self)
        self.label_q.setGeometry(QtCore.QRect(10, 10, 151, 61))
        self.label_q.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                   "font-family: \'Roboto Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 14px;\n"
                                   "line-height: 18px;\n"
                                   "\n"
                                   "color: #FFFFFF;")
        self.label_q.setObjectName("label_q")
        self.button_back = QtWidgets.QPushButton(self)
        self.button_back.setGeometry(QtCore.QRect(40, 70, 81, 23))
        self.button_back.setStyleSheet("QPushButton {\n"
                                       "font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 18px;\n"
                                       "line-height: 18px;\n"
                                       "color: rgba(255, 255, 255, 0.8);background: rgba(23, 23, 23, 0.0);}\n"
                                       "QPushButton:hover{\n"
                                       "color: rgba(255, 255, 255, 1.0)\n"
                                       "}")
        self.button_back.setObjectName("button_back")
        self.label_q.setText("Sorry something,\n"
                             " went wrong   (=｀ω´=)")
        self.button_back.setText("-- sigh --")
        self.button_back.clicked.connect(lambda: sys.exit())
