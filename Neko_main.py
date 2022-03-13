import sys
import sqlite_Neko
from PyQt5.QtGui import QKeySequence, QWheelEvent
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
        self.main_note_frame.hide()
        self.setting_frame.hide()
        self.Note_frame_2.hide()
        # self.frame_main.hide()
        self.main_min_frame.hide()
        self.setting_page_2.hide()
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
        self.button_note.clicked.connect(self.show_note_frame)
        self.back_from_note_button.clicked.connect(self.return_to_main)
        self.note_close_button.clicked.connect(self.close_edit_note)
        self.note_save_button.clicked.connect(self.save_note)
        self.button_add_note.clicked.connect(self.create_new_note)
        self.note_del_button.clicked.connect(self.del_note)
        self.wrap_button.clicked.connect(self.hide_main_window)
        self.like_command_button_min.clicked.connect(self.show_hide_like_command)
        self.teg_button_min.clicked.connect(self.show_teg_frame)
        self.button_note_min.clicked.connect(self.show_note_frame)
        self.setting_button_on_page_2.clicked.connect(self.set_on_page_2)
        self.button_on_1_page.clicked.connect(self.set_on_page_1)
        self.button_window_r_2.clicked.connect(self.Next_main_window_size)
        self.button_window_l_2.clicked.connect(self.Next_main_window_size)
        """set variables"""
        self.scroll_px = 0
        self.button_bar = [0,1,2,3]
        self.main_window_size = False
        self.next_main_frame = False
        self.like_button_check = False
        self.teg_button_check = False
        self.setting_button_check = False
        self.directory_list = []  # список получает пути, выбранные через проводник
        self.link_site = ""  # получает название сайта
        self.del_list = []  # выбранные команды для удаления попадают сюда
        self.language_list = ["russian", "english"]
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.names_character_list = sqlite_Neko.get_names_character(
                conn)  # получить имена всех доступных персонажей
            self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.work_table,self.main_window_size = sqlite_Neko.get_global_name(
                conn)
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
            self.set_name_in_widget()
        """note variable"""
        self.current_note_button = None
        """check main window"""
        if self.main_window_size == "min":
            self.flag_main_min_frame = True
            self.frame_main.hide()
            self.main_min_frame.show()
        self.label_normal_window_page_2.setText(self.main_window_size)
    """fun min frame"""
    @staticmethod
    def shift(lst, steps):
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                lst.append(lst.pop(0))
        else:
            for i in range(steps):
                lst.insert(0, lst.pop())

    def wheelEvent(self, event: QWheelEvent):
        adj = int(event.angleDelta().y()) // 120

        self.scroll_px = self.scroll_px + adj
        if self.scroll_px != 0:
            self.clear_note(self.gridLayout_min)
            self.button_note_min = QtWidgets.QPushButton()
            self.button_note_min.setEnabled(True)
            self.button_note_min.setMinimumSize(QtCore.QSize(50, 50))
            self.button_note_min.setMaximumSize(QtCore.QSize(50, 50))
            self.button_note_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;")
            self.button_note_min.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("material/image 50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.button_note_min.setIcon(icon)
            self.button_note_min.setIconSize(QtCore.QSize(50, 50))
            self.button_note_min.setAutoDefault(False)
            self.button_note_min.setDefault(False)
            self.button_note_min.setObjectName("button_note_min")
            self.like_command_button_min = QtWidgets.QPushButton()
            self.like_command_button_min.setEnabled(True)
            self.like_command_button_min.setMaximumSize(QtCore.QSize(50, 50))
            self.like_command_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                       "border-radius: 13px;")
            self.like_command_button_min.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("material/image 41.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.like_command_button_min.setIcon(icon1)
            self.like_command_button_min.setMinimumSize(QtCore.QSize(50, 50))
            self.like_command_button_min.setIconSize(QtCore.QSize(50, 50))
            self.like_command_button_min.setAutoDefault(False)
            self.like_command_button_min.setDefault(False)
            self.like_command_button_min.setObjectName("like_command_button_min")
            self.teg_button_min = QtWidgets.QPushButton()
            self.teg_button_min.setEnabled(True)
            self.teg_button_min.setMinimumSize(QtCore.QSize(50, 50))
            self.teg_button_min.setMaximumSize(QtCore.QSize(50, 50))
            self.teg_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "border-radius: 13px;")
            self.teg_button_min.setText("")
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap("material/image 42.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.teg_button_min.setIcon(icon2)
            self.teg_button_min.setIconSize(QtCore.QSize(50, 50))
            self.teg_button_min.setAutoDefault(False)
            self.teg_button_min.setDefault(False)
            self.teg_button_min.setObjectName("teg_button_min")
            self.code_button = QtWidgets.QPushButton()
            self.code_button.setEnabled(True)
            self.code_button.setGeometry(QtCore.QRect(90, 110, 61, 61))
            self.code_button.setMinimumSize(QtCore.QSize(50, 50))
            self.code_button.setMaximumSize(QtCore.QSize(50, 50))
            self.code_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;")
            self.code_button.setText("")
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("material/image 62.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.code_button.setIcon(icon1)
            self.code_button.setIconSize(QtCore.QSize(50, 50))
            self.code_button.setAutoDefault(False)
            self.code_button.setDefault(False)
            self.code_button.setObjectName("code_button")
            self.like_command_button_min.clicked.connect(self.show_hide_like_command)
            self.teg_button_min.clicked.connect(self.show_teg_frame)
            self.button_note_min.clicked.connect(self.show_note_frame)
            self.shift(self.button_bar,1)
            self.gridLayout_min.addWidget(self.like_command_button_min, 0, self.button_bar[0], 1, 1)
            self.gridLayout_min.addWidget(self.button_note_min, 0, self.button_bar[1], 1, 1)
            self.gridLayout_min.addWidget(self.teg_button_min, 0, self.button_bar[2], 1, 1)
            self.gridLayout_min.addWidget(self.code_button, 0, self.button_bar[3], 1, 1)

        self.scroll_px = 0
    """fun Note frame"""

    def del_note(self, ):
        """
           removes the entry from the database that matches work_table, current_note_button
           param conn: database connection
           """
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sqlite_Neko.delete_note(conn, self.work_table, self.current_note_button)
            sqlite_Neko.reset_button_note(conn, self.work_table, self.current_note_button)
            self.Note_frame_2.hide()
            self.generate_note()

    def generate_note(self):
        """
          adds 2 column entries to gridLayout_note
           param conn: database connection
           param list_all_note: list of all signatures received from Neko.db
           param pushButton_note: a button that displays the text of the note, when clicked, it switches to editing, the function edit_note()
           param gridLayout_note: grid widget in main_note_frame
           """
        self.clear_note(self.gridLayout_note)
        conn = sqlite_Neko.create_connection("Neko.db")
        list_coordinate = []
        with conn:
            list_all_note = sqlite_Neko.get_note_list(conn, self.work_table)[0]
        for i in range(len(list_all_note)):
            list_coordinate.append((i, 0))
            list_coordinate.append((i, 1))
        print(list_all_note)
        count = 0
        for i in list_coordinate[:len(list_all_note)]:
            x, y = i
            self.pushButton_note = QtWidgets.QPushButton()
            self.pushButton_note.setMinimumSize(QtCore.QSize(148, 161))
            self.pushButton_note.setMaximumSize(QtCore.QSize(148, 161))
            self.pushButton_note.setStyleSheet("background: rgba(23, 23, 23, 0.76);\n"
                                               "border: 1px solid #ABABAB;\n"
                                               "box-sizing: border-box;\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 24px;\n"
                                               "font-family: Roboto Mono;\n"
                                               "font-style: normal;\n"
                                               "font-weight: normal;\n"
                                               "font-size: 14px;\n"
                                               "line-height: 24px;\n"
                                               "vertical-align: top; \n"
                                               "text-align: Top left;\n"
                                               "padding: 10px 10px 20px 10px;\n"
                                               "color: #FFFFFF;")
            self.pushButton_note.setText(f"{list_all_note[count]}")
            self.pushButton_note.setObjectName(f"{count}")
            self.pushButton_note.clicked.connect(lambda checked, button=self.pushButton_note: self.edit_note(button))
            self.gridLayout_note.addWidget(self.pushButton_note, x, y)
            count += 1

    def edit_note(self, button):
        """
           shows Note_frame_2 which allows text editing
           param conn:
           param current_note_button: marks the ordinal index of the button
           param note_edit: QTextEdit widget

           """
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.Note_frame_2.show()
            print(self.work_table, button.objectName())
            note_from_bd = sqlite_Neko.note_button_up(conn, self.work_table, button.objectName())
            print(note_from_bd)
            self.current_note_button = button.objectName()
            self.note_edit.setText(note_from_bd[0])

    def save_note(self):
        """saves the updated note_edit entry from Note_frame_2"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            text = self.note_edit.toPlainText()
            sqlite_Neko.save_note_sq(conn, (
                self.work_table, self.current_note_button, text, self.work_table, self.current_note_button))

    def close_edit_note(self):
        """close Note_frame_2"""
        self.Note_frame_2.hide()
        self.generate_note()

    def create_new_note(self):
        """generates a new entry at the end of the database"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            (list_all_note, list_object_name) = sqlite_Neko.get_note_list(conn, self.work_table)
            print((self.work_table, f"{len(list_object_name) + 1}", ""))
            sqlite_Neko.create_note(conn, (self.work_table, str(len(list_object_name)), "Firo"))
            self.generate_note()

    def clear_note(self, gridLayout):
        """
           Clears the resulting layout from elements
           param gridLayout_note: layout для очистки от элементов
           """
        while gridLayout.count():
            item = gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

    def show_note_frame(self):
        self.frame_main.hide()
        self.main_note_frame.show()
        self.generate_note()
        self.button_add_note.setText(f"{self.name_character} want add")

    def return_to_main(self):
        if self.main_window_size == "min":
            self.main_note_frame.hide()
        else:
            self.main_note_frame.hide()
            self.frame_main.show()

    """fun setting frame"""
    def set_on_page_2(self):
        self.setting_frame.hide()
        self.setting_page_2.show()

    def set_on_page_1(self):
        self.setting_frame.show()
        self.setting_page_2.hide()

    def set_back_on_main(self):
        if self.main_window_size == "min":
            self.setting_frame.hide()
            self.main_min_frame.show()

        else:
            self.setting_frame.hide()
            self.frame_main.show()

    def save_global_setting(self):
        """ stores global settings in database  """
        conn = sqlite_Neko.create_connection("Neko.db")
        get_user_name = self.Nickname_2.text()
        if get_user_name not in ["нике", "nickname"]:
            self.name_user = get_user_name
        get_character_name = self.Nickname_1.text()
        if get_character_name not in ["нике", "nickname"]:
            self.name_character = get_character_name
        if self.main_window_size == "min":
            self.frame_main.hide()
            self.flag_main_min_frame = True
            self.main_min_frame.show()
        else :
            self.flag_main_min_frame = False
            self.frame_main.show()
            self.main_min_frame.hide()
        print(get_user_name, self.name_user)
        with conn:
            sqlite_Neko.update_global_name(conn, (
                self.view_character, self.name_character, self.name_user, self.language, self.behavior,
                self.work_table,self.main_window_size))
        self.set_name_in_widget()
    def Next_main_window_size(self):
        self.next_main_frame = not self.next_main_frame
        if self.next_main_frame:
            self.main_window_size = "min"
        else:
            self.main_window_size = "normal"
        self.label_normal_window_page_2.setText(self.main_window_size)
    def Next_language(self):
        """allows you to change the language in the settings
           param language_index: needed to determine the current language
           """
        language_index = self.language_list.index(self.language)
        language_index += 1
        if language_index == len(self.language_list):
            language_index = 0
        self.language = self.language_list[language_index]
        if self.language == "russian":
            self.set_ru()
        elif self.language == "english":
            self.set_en()

    def Next_character(self):
        """allows you to change the character in the settings
          param language_index: needed to determine the current character
          """
        character_index = self.names_character_list.index(self.view_character)
        print(character_index)
        character_index += 1
        if character_index > len(self.names_character_list) - 1:
            character_index = 0
        self.view_character = self.names_character_list[character_index]
        print(self.view_character)
        self.update_paths()

    def update_paths(self):
        """associated with Next_character, according to the selected character, changes the paths to the pictures of the corresponding
         character, all frames use 4 different images of one character, stored in database """
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.current_paths_character = sqlite_Neko.get_paths_character(conn, self.view_character)
            self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
            self.character_on_add_del_frame.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
            self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))

    def set_name_in_widget(self):
        """ follows after save_global_setting(), applies resulting changes to unique variables
        self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.work_table"""
        self.dialog_character.setText(f"          {self.name_user},надеюсь, ты меня не просто так позвал?")
        self.character_name_label.setText(self.name_character)
        self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
        self.character_on_add_del_frame.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
        self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))
        self.character_s.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))

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
        print(self.rule_command_button.objectName())
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
        self.directory_list = []
        self.clear_note(self.grid)
        self.del_list = []
        self.clear_note(self.delite_bar)



    def get_directory(self):
        """select files for action"""
        folder = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку", ".")
        print(folder)
        self.directory_list.append(folder)
        print(self.directory_list)
        for i in range(4):
            column = [[0, 0], [0, 1], [1, 0], [1, 1], ]
            x, y = column[i]
            if i < len(self.directory_list):
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
                if len(self.directory_list[i]) > 20:
                    ne = self.directory_list[i][:20] + "\n" + self.directory_list[i][20:40:] + "\n" + self.directory_list[i][40:60:] + "\n" + \
                         self.directory_list[i][60::]
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
        """add command to database"""
        self.link_site = self.lineEdit_4.text()
        if (self.directory_list != []) and (self.link_site in ["set site", "укажи сайт"]):
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.input_name_command.text()
            file = []
            with conn:
                for i in range(4):
                    if i < len(self.directory_list):
                        file.append(self.directory_list[i])
                    else:
                        file.append("")

                task = ("f", file[0], file[1], file[2], file[3], "", command)
                sqlite_Neko.create_task(conn, task)
                self.directory_list = []
                self.clear_note(self.grid)
                self.input_name_command.setText("access")
        elif (self.directory_list == []) and (self.link_site not in ["set site", "укажи сайт"]):
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.input_name_command.text()
            with conn:
                task = ("s", "", "", "", "", self.link_site, command)
                sqlite_Neko.create_task(conn, task)
                self.input_name_command.setText("access")

        else:
            self.input_name_command.setText("fail")
        self.clear_note(self.delite_bar)
        self.show_update_item_in_area_delite_choice()

    def show_update_item_in_area_delite_choice(self):
        """updates buttons containing commands"""
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
            self.delite_bar.addWidget(self.pushButton, 0, i)

    def active_button(self, pushButton):
        """makes the button active when pressed, adds a command to del_list"""
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

    def del_command(self):
        """delite command from database with name from del_list"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            for i in self.del_list:
                sqlite_Neko.delete_task(conn, i)
        self.clear_note(self.delite_bar)
        self.show_update_item_in_area_delite_choice()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()
