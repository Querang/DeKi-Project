import random
import sys
import sqlite_Neko
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut
from Neko_layout import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        """screen size get"""
        screen = app.primaryScreen()
        size = screen.size()

        self.setupUi(self)
        self.setGeometry(0, 0, size.width(), size.height())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        """add widget"""
        self.grid = QtWidgets.QGridLayout(self.frame_11)

        """hide/show frame"""
        self.frame_rule_command.hide()
        self.command_panel_frame.hide()
        self.teg_frame.hide()
        # self.main_note_frame.hide()
        self.setting_frame.hide()

        """hotkey"""
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.hide_main_window)

        """assign an action"""
        self.rule_command_button.clicked.connect(self.show_rule_command_frame)
        self.rule_command_back_button.clicked.connect(self.back_on_main_frame)
        self.like_command_button.clicked.connect(self.show_hide_like_command)
        self.teg_button.clicked.connect(self.show_teg_frame)
        self.bread_button.clicked.connect(self.get_directory)
        self.push_add_command.clicked.connect(self.add_date_in_Neko_bd)
        self.button_delite_command.clicked.connect(self.del_command)
        self.setting_button.clicked.connect(self.show_setting_frame)
        self.button_character_r.clicked.connect(self.Next_character)
        self.button_character_l.clicked.connect(self.Next_character)
        self.button_save.clicked.connect(self.save_global_setting)
        self.pushButton_2.clicked.connect(self.set_back_on_main)
        self.button_language_r.clicked.connect(self.Next_language)
        self.button_language_l.clicked.connect(self.Next_language)
        # self.button_note.clicked.connect(self.show_note_frame)
        # self.back_from_note_button.clicked.connect(self.return_to_main)
        # self.button_add_note.clicked.connect(self.add_note)
        """set variables"""
        self.like_button_check = False
        self.teg_button_check = False
        self.setting_button_check = False
        self.dirlist = []  # список получает пути, выбранные через проводник
        self.link_site = ""  # получает название сайта
        self.del_list = []  # выбранные команды для удаления попадают сюда
        self.language_list = ["russian", "english"]
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.names_character_list = sqlite_Neko.get_names_character(
                conn)  # получить имена всех доступных персонажей
            self.view_character, self.name_character, self.name_user, self.language, self.behavior = sqlite_Neko.get_global_name(
                conn)
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
            self.set_name_in_widget()

    """fun Note frame"""
    # def add_note(self):
    #     self.clear_gri()
    #     count = 6
    #     list_note = []
    #     """есть кнопка, она вызывает фрейм с ineedit
    #     в этом lineedit отображается текст привязанный к положению этой кнопки
    #     текст на кнопке связан с ее положением
    #     сайв на фрейме с эдитом сохраняет запись по положению"""
    #     for i in range(count):
    #         list_note.append((i,0))
    #         list_note.append((i,1))
    #     print(list_note[:count])
    #     co = 0
    #     for i in list_note[:count]:
    #         print(i)
    #         l,k = i
    #         print(l,k)
    #
    #         self.pushButton_note = QtWidgets.QPushButton()
    #         self.pushButton_note.setMinimumSize(QtCore.QSize(148, 161))
    #         self.pushButton_note.setMaximumSize(QtCore.QSize(148, 161))
    #         self.pushButton_note.setStyleSheet("background: rgba(23, 23, 23, 0.76);\n"
    #                                         "border: 1px solid #917C7C;\n"
    #                                         "box-sizing: border-box;\n"
    #                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
    #                                         "border-radius: 24px;\n"
    #                                         "font-family: Roboto Mono;\n"
    #                                         "font-style: normal;\n"
    #                                         "font-weight: normal;\n"
    #                                         "font-size: 14px;\n"
    #                                         "line-height: 24px;\n"
    #                                         "vertical-align: top; \n"
    #                                         "text-align: Top left;\n"
    #                                         "padding: 10px 10px 20px 10px;\n"
    #                                         "color: #FFFFFF;")
    #         self.pushButton_note.setText(f"{co}")
    #         self.gridLayout_note.addWidget(self.pushButton_note, l, k)
    #         co+=1

    """ далее устанавливаем каждому setObject name  отсылаемся по нему"""
    "установить глобальное значение стола заметок заметок"
    "переменная под текущую кнопку"
    # def edit_note(self,object_name):
    #     self.Note_frame_2.show()
    #     conn = sqlite_Neko.create_connection("Neko.db")
    #     with conn:
    #         note_frome_bd = sqlite_Neko.note_button_up(conn,self.work_table,object_name)
    #         self.note_edit.setText(note_frome_bd)
    #
    # def save_note(self):
    #     conn = sqlite_Neko.create_connection("Neko.db")
    #     with conn:
    #         text = self.note_edit.text()
    #         sqlite_Neko.save_note_sq(conn,self.current_note_button,text)
    #
    # def close_edit_note(self):
    #     self.Note_frame_2.hide()
    #
    #
    # def clear_gri(self):
    #     while self.gridLayout_note.count():
    #         item = self.gridLayout_note.takeAt(0)
    #         widget = item.widget()
    #         # if widget has some id attributes you need to
    #         # save in a list to maintain order, you can do that here
    #         # i.e.:   aList.append(widget.someId)
    #         widget.deleteLater()
    # def show_note_frame(self):
    #     self.frame_main.hide()
    #     self.main_note_frame.show()
    #
    # def return_to_main(self):
    #     self.main_note_frame.hide()
    #     self.frame_main.show()

    """fun setting frame"""

    def set_back_on_main(self):
        self.setting_frame.hide()
        self.frame_main.show()

    def save_global_setting(self):
        conn = sqlite_Neko.create_connection("Neko.db")
        get_user_name = self.Nickname_2.text()
        if get_user_name not in ["нике", "nickname"]:
            self.name_user = get_user_name
        get_character_name = self.Nickname_1.text()
        if get_character_name not in ["нике", "nickname"]:
            self.name_character = get_character_name
        self.name_user = get_user_name
        print(get_user_name, self.name_user)
        with conn:
            sqlite_Neko.update_global_name(conn, (
                self.view_character, self.name_character, self.name_user, self.language, self.behavior))
        self.set_name_in_widget()

    def Next_language(self):
        re_index = self.language_list.index(self.language)
        re_index += 1
        if re_index == len(self.language_list):
            re_index = 0
        self.language = self.language_list[re_index]
        if self.language == "russian":
            self.set_ru()
        elif self.language == "english":
            self.set_en()

    def Next_character(self):
        re_index = self.names_character_list.index(self.view_character)
        print(re_index)
        re_index += 1
        if re_index > len(self.names_character_list) - 1:
            re_index = 0
        self.view_character = self.names_character_list[re_index]
        print(self.view_character)
        self.update_paths()

    def update_paths(self):
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
            self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
            self.character_on_add_del_frame.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
            self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))

    def set_name_in_widget(self):
        self.dialog_character.setText(f"          {self.name_user},надеюсь, ты меня не просто так позвал?")
        self.character_name_label.setText(self.name_character)
        self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
        self.character_on_add_del_frame.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
        self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))

    """fun in main frame"""

    def show_setting_frame(self):
        self.frame_main.hide()
        self.setting_frame.show()
        self.command_panel_frame.hide()

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

    def show_teg_frame(self):
        if self.teg_button_check:
            self.teg_frame.hide()
        else:
            self.teg_frame.show()
        self.teg_button_check = not self.teg_button_check

    """fun in  frame add/del"""

    def back_on_main_frame(self):
        self.frame_main.show()
        self.frame_rule_command.hide()
        self.command_panel_frame.show()
        self.dirlist = []
        self.clear_grid()
        self.del_list = []
        self.clear_delite_bar()

    def clear_grid(self):
        """после выбора файла появляется label с его названием, функция очищает grid в котором он находится"""
        while self.grid.count():
            item = self.grid.takeAt(0)
            widget = item.widget()
            # if widget has some id attributes you need to
            # save in a list to maintain order, you can do that here
            # i.e.:   aList.append(widget.someId)
            widget.deleteLater()

    def get_directory(self):
        """выбор файлов для действия"""
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
        """добавить task в базу данных"""
        self.link_site = self.lineEdit_4.text()
        if (self.dirlist != []) and (self.link_site in ["set site", "укажи сайт"]):
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
        elif (self.dirlist == []) and (self.link_site not in ["set site", "укажи сайт"]):
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
        """обновляет кнопки, содержащие команды"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i, j in enumerate(name):
            if len(name) > 3:
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
            self.Layout.addWidget(self.pushButton, 0, i)

    def active_button(self, pushButton):
        """делает кнопку активной при нажатии,добавляет команду в del_list"""
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
                sqlite_Neko.delete_task(conn, i)
        self.clear_delite_bar()
        self.show_update_item_in_area_delite_choice()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
