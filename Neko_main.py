import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from Neko_without_frame_command import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # screen size get
        screen = app.primaryScreen()
        size = screen.size()

        self.setupUi(self)
        self.setGeometry(0, size.height()//8, size.width(), size.height())

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.frame_rule_command.hide()
        self.command_panel_frame.hide()
        self.setting_frame.hide()

        # hotkey
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.hide_main_window)

        # assign an action
        self.rule_command_button.clicked.connect(self.show_rule_command_frame)
        self.rule_command_back_button.clicked.connect(self.back_on_main_frame)
        self.like_command_button.clicked.connect(self.show_hide_like_command)
        self.teg_button.clicked.connect(self.show_setting_frame)

        # set variables
        self.like_button_check = False
        self.teg_button_check = False

    def hide_main_window(self):
        self.showMinimized()

    def show_rule_command_frame(self):
        self.frame_main.hide()
        self.frame_rule_command.show()
        self.command_panel_frame.hide()

    def show_hide_like_command(self):
        if self.like_button_check:
            self.command_panel_frame.hide()
        else:
            self.command_panel_frame.show()
        self.like_button_check = not self.like_button_check

    def show_setting_frame(self):
        if self.teg_button_check:
            self.setting_frame.hide()
        else:
            self.setting_frame.show()
        self.teg_button_check = not self.teg_button_check

    def back_on_main_frame(self):
        self.frame_main.show()
        self.frame_rule_command.hide()
        self.command_panel_frame.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
