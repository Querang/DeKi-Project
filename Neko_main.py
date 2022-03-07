import sys
import sqlite_Neko
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from Neko_layout import Ui_MainWindow
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

        self.frame_rule_command.hide()
        self.command_panel_frame.hide()
        #self.setting_frame.hide()

        # hotkey
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.hide_main_window)

        # assign an action
        self.rule_command_button.clicked.connect(self.show_rule_command_frame)
        self.rule_command_back_button.clicked.connect(self.back_on_main_frame)
        self.like_command_button.clicked.connect(self.show_hide_like_command)
        self.teg_button.clicked.connect(self.show_setting_frame)
        self.bread_button.clicked.connect(self.get_directory)
        self.push_add_command.clicked.connect(self.add_date_in_Neko_bd)
        self.button_delite_command.clicked.connect(self.del_command)
        # set variables
        self.like_button_check = False
        self.teg_button_check = False
        self.dirlist = []
        self.link_site = ""
        self.del_list = []

    def hide_main_window(self):
        self.showMinimized()

    def show_rule_command_frame(self):
        self.frame_main.hide()
        self.frame_rule_command.show()
        self.command_panel_frame.hide()
        self.show_update_item_in_area_delite_choice()

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
        self.clear_grid()
        self.del_list = []
        self.clear_delite_bar()

    # ADD FRAME FUN
    def clear_grid(self):
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
        for i in range(4):
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

    def add_date_in_Neko_bd(self):
        self.link_site = self.lineEdit_4.text()
        if (self.dirlist != []) and (self.link_site == "set site"):
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.input_name_command.text()
            file = []
            with conn:
                for i in range(4):
                    if i < len(self.dirlist):
                        file.append(self.dirlist[i])
                    else:
                        file.append("")

                task = ("f", file[0], file[1], file[2], file[3], "", command)
                sqlite_Neko.create_task(conn, task)
                self.dirlist = []
                self.clear_grid()
                self.input_name_command.setText("access")
        elif (self.dirlist == []) and (self.link_site != "set site"):
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.input_name_command.text()
            with conn:
                task = ("s", "", "", "", "", self.link_site, command)
                sqlite_Neko.create_task(conn, task)
                self.input_name_command.setText("access")

        else:
            self.input_name_command.setText("fail")
        self.clear_delite_bar()
        self.show_update_item_in_area_delite_choice()


    def show_update_item_in_area_delite_choice(self):
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i,j in enumerate(name):
            if len(name)>3:
                self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            else:
                self.scrollArea_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.pushButton = QtWidgets.QPushButton()
            self.pushButton.setGeometry(QtCore.QRect(30, 20, 200, 32))
            self.pushButton.setMinimumSize(200, 52)
            self.pushButton.setMaximumSize(200, 52)
            self.pushButton.setStyleSheet("border-radius: 2px;\n"
                                             "font: 12pt \"MS Shell Dlg 2\";\n"
                                             "color: rgba(255, 255, 255, 0.67);\n"
                                             "\n"
                                             "background: rgba(23, 23, 23, 0.31);\n"
                                             "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                             "box-sizing: border-box;\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
            self.pushButton.setText(f"{j}")
            self.pushButton.clicked.connect(lambda checked, button=self.pushButton: self.active_button(button))
            self.Layout.addWidget(self.pushButton,0,i)


    def active_button(self,pushButton):
        pushButton.setStyleSheet("border-radius: 2px;\n"
                                 "font: 12pt \"MS Shell Dlg 2\";\n"
                                 "color: rgba(255, 255, 255, 0.67);\n"
                                 "\n"
                                 "background: rgba(74, 65, 65, 0.31);\n"
                                 "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                 "box-sizing: border-box;\n"
                                 "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        qq = pushButton.text()
        self.del_list.append(qq)
        print(self.del_list)


    def clear_delite_bar(self):
        while self.Layout.count():
            item = self.Layout.takeAt(0)
            widget = item.widget()
            # if widget has some id attributes you need to
            # save in a list to maintain order, you can do that here
            # i.e.:   aList.append(widget.someId)
            widget.deleteLater()
    def del_command(self):
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            for i in self.del_list:
                sqlite_Neko.delete_task(conn,i)
        self.clear_delite_bar()
        self.show_update_item_in_area_delite_choice()

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
