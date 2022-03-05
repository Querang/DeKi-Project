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
        self.setGeometry(0, size.height() // 8, size.width(), size.height())

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # add widget
        self.grid = QtWidgets.QGridLayout(self.frame_11)

        # self.frame_rule_command.hide()
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
        self.bread_button.clicked.connect(self.get_directory)
        # set variables
        self.like_button_check = False
        self.teg_button_check = False
        self.dirlist = []

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
        self.dirlist = []
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            # if widget has some id attributes you need to
            # save in a list to maintain order, you can do that here
            # i.e.:   aList.append(widget.someId)
            widget.deleteLater()
    # выбор файлов для действия
    def get_directory(self):

        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку", ".")
        print(folder)
        self.dirlist.append(folder)
        print(self.dirlist)
        for i in range(3):
            column = [[0, 0], [0, 1], [1, 0], [1, 1], ]
            x, y = column[i]
            if i < len(self.dirlist):
                label = QtWidgets.QLabel()
                label.setGeometry(QtCore.QRect(0, 0, 121, 151))
                label.setMaximumSize(121, 151)

                label.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                    "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 13px;\n"
                                    "font-size: 12px;\n"
                                    "line-height: 27px;\n"
                                    "\n"
                                    "color: #FFFFFF;")
                if len(self.dirlist[i]) > 20:
                    ne = self.dirlist[i][:20] + "\n" + self.dirlist[i][20:40:] + "\n" + self.dirlist[i][40:60:] + "\n" + \
                         self.dirlist[i][60::]
                label.setText(ne)
                self.grid.addWidget(label, x, y)


            else:
                label = QtWidgets.QLabel()
                label.setGeometry(QtCore.QRect(0, 0, 121, 151))
                label.setStyleSheet("background: rgba(23, 23, 23, 0);\n"
                                    "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 13px;\n"
                                    "font-size: 12px;\n"
                                    "line-height: 27px;\n"
                                    "\n"
                                    "color: #FFFFFF;")
                self.grid.addWidget(label, x, y)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
