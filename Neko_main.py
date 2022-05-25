import subprocess
import os.path
import sys
import sqlite_Neko
import random
import pyttsx3
import speech_recognition
import webbrowser
import wave
import json
import keyboard
import Neko_voice
from multiprocessing import Process
from vosk import Model, KaldiRecognizer
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
        self.voice_set_1.hide()
        self.frame_rule_command.hide()
        self.command_panel_frame.hide()
        self.teg_frame.hide()
        self.main_note_frame.hide()
        self.setting_frame.hide()
        self.Note_frame_2.hide()
        # self.frame_main.hide()
        self.main_min_frame.hide()
        self.setting_page_2.hide()
        self.notification_panel.hide()
        """hotkey"""
        self.shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        self.shortcut.activated.connect(self.hide_main_window)
        self.shortcut = QShortcut(QKeySequence("s"), self)
        self.shortcut.activated.connect(self.show_voice_settings)

        self.voice_process = Process(target=Neko_voice.voice_helper)
        self.voice_process.start()

        """assign an action"""
        self.mic_button_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.name_button_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.command_button_1.clicked.connect(self.set_voice_page_3)
        self.exit_button_2.clicked.connect(self.close_voice_settings)
        self.close_not_button.clicked.connect(self.close_notification)
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
        self.microphone_select.activated[str].connect(self.onActivated_1)
        self.command_bd_select.activated[str].connect(self.onActivated_2)
        self.button_window_r_2.clicked.connect(self.Next_main_window_size)
        self.button_window_l_2.clicked.connect(self.Next_main_window_size)
        self.create_name_button.clicked.connect(self.add_voice_com)
        """set variables"""
        self.scroll_px = 0
        self.button_bar = [0, 1, 2, 3]
        self.main_window_size = False
        self.next_main_frame = False
        self.like_button_check = False
        self.teg_button_check = False
        self.setting_button_check = False
        self.directory_list = []  # список получает пути, выбранные через проводник
        self.link_site = ""  # получает название сайта
        self.del_list = []  # выбранные команды для удаления попадают сюда
        self.del_list_voice = []
        self.language_list = ["russian", "english"]
        self.microphone_search()
        self.bd_command_searcher()


        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            self.names_character_list = sqlite_Neko.get_names_character(conn)  # получить имена всех доступных персонажей
            self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.work_table, self.main_window_size = sqlite_Neko.get_global_name(
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
            self.pushButton_note.setStyleSheet("background: rgba(23, 23, 23, 0.5);\n"
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
            self.character_s.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))
            self.character_s_min.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))

    def set_name_in_widget(self):
        """ follows after save_global_setting(), applies resulting changes to unique variables
        self.view_character, self.name_character, self.name_user, self.language, self.behavior, self.work_table"""
        self.dialog_character.setText(f"          {self.name_user},надеюсь, ты меня не просто так позвал?")
        self.character_name_label.setText(self.name_character)
        self.character_label.setPixmap(QtGui.QPixmap(self.current_paths_character[1]))
        self.character_on_add_del_frame.setPixmap(QtGui.QPixmap(self.current_paths_character[2]))
        self.character_set.setPixmap(QtGui.QPixmap(self.current_paths_character[3]))
        self.character_s.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))
        self.character_s_min.setPixmap(QtGui.QPixmap(self.current_paths_character[4]))

    """fun in main frame"""

    def show_setting_frame(self):
        if self.main_window_size == "min":
            self.teg_frame.hide()
            self.frame_rule_command.hide()
            self.main_min_frame.hide()
        else:
            self.teg_frame.hide()
            self.frame_rule_command.hide()
            self.frame_main.hide()
        self.setting_frame.show()
        self.command_panel_frame.hide()


    def hide_main_window(self):
        self.showMinimized()

    def show_rule_command_frame(self):
        if self.main_window_size == "min":
            self.frame_rule_command.hide()
            self.main_min_frame.hide()
        else:
            self.frame_rule_command.hide()
            self.frame_main.show()
        self.frame_rule_command.show()
        self.teg_frame.hide()
        self.show_update_item_in_area_delite_choice()

    def show_hide_like_command(self):
        print(self.rule_command_button.objectName())
        if self.like_button_check:
            self.command_panel_frame.hide()
        else:
            self.command_panel_frame.show()
            self.command_panel_frame_button_update()
        self.like_button_check = not self.like_button_check

    def show_teg_frame(self):
        if self.teg_button_check:
            self.teg_frame.hide()
        else:
            self.teg_frame.show()
        self.teg_button_check = not self.teg_button_check

    def close_notification(self):
        self.notification_panel.hide()

    """fun in  frame add/del"""

    def back_on_main_frame(self):
        if self.main_window_size == "min":
            self.main_min_frame.show()
        else:
            self.frame_main.show()
        self.frame_rule_command.hide()
        self.directory_list = []
        self.clear_note(self.grid)
        self.del_list = []
        self.clear_note(self.delite_bar)

    def get_directory(self):
        """select files for action"""
        folder = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "/")[0]
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

    def add_voice_com(self):
        """add voice com"""
        conn = sqlite_Neko.create_connection("Neko.db")
        command_name = self.input_name_command_voice.text()
        sources_in_bd = sqlite_Neko.voice_commands_source(conn)
        names_in_bd = sqlite_Neko.voice_commands_names(conn)
        count_names = 0
        count = 0
        for i in command_name:
            if i == " ":
                count = count + 1
        if count == len(command_name):
            self.input_name_command_voice.setText("")
        elif (command_name.find("(") != -1) or (command_name.find(")") != -1):
            self.input_name_command_voice.setText("")
        else:
            while command_name[len(command_name)-1] == " ":
                command_name = command_name[0: len(command_name)-2]
            bd_name = self.bd_com.text()

        for j in sources_in_bd:
            bd_name = self.bd_com.text()
            if j == bd_name:
                count_names = count_names + 1

        name_flag = True
        for j in names_in_bd:
            if j == command_name:
                name_flag = False

        if count_names < 4 and name_flag is True:
            with conn:
                bd_name = self.bd_com.text()
                voice_com = (command_name, bd_name, 1)
                sqlite_Neko.create_voice_com(conn, voice_com)
                self.input_name_command_voice.setText("")
        else:
            if name_flag is False:
                self.input_name_command_voice.setText("Такое название уже есть!")
            else:
                self.input_name_command_voice.setText("Слишком много названий!")

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

    def command_panel_frame_button_update(self):
        """обновляет кнопки, содержащие команды для выполнения"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i, j in enumerate(name):
            self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.pushButton = QtWidgets.QPushButton()
            self.pushButton.setMinimumSize(140, 52)
            self.pushButton.setMaximumSize(140, 52)
            self.pushButton.setStyleSheet("border-radius: 2px;\n"
                                          "font: 12pt \"MS Shell Dlg 2\";\n"
                                          "color: rgba(255, 255, 255, 0.67);\n"
                                          "\n"
                                          "background: rgba(23, 23, 23, 0.31);\n"
                                          "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                          "box-sizing: border-box;\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
            self.pushButton.setText(f"{j}")
            self.pushButton.clicked.connect(lambda checked, button=self.pushButton: self.active_command_button(button))
            self.gridLayout_9.addWidget(self.pushButton, i, 0)

    def active_command_button(self, pushButton):
        """считывает название кнопки, выполняет команду"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            button_name = pushButton.text()
            sql_command_name = sqlite_Neko.select_all_command(conn)
            sql_command_type = sqlite_Neko.select_type_of_commands(conn)
            sql_command_files = sqlite_Neko.select_files_of_commands(conn)
            sql_command_site = sqlite_Neko.select_sites_of_command(conn)
            index = sql_command_name.index(button_name)
            command_type = sql_command_type[index]
            if command_type == 's':
                if sql_command_site[index].find("https://"):
                    webbrowser.open_new_tab(str(sql_command_site[index]))
                else:
                    webbrowser.open_new_tab("https://" + str(sql_command_site[index]))
            elif command_type == 'f':
                for i in sql_command_files[index]:
                    print(sql_command_files[index])
                    if os.path.exists(i) is True:
                        subprocess.call(('cmd', '/c', 'start', '', i))
                    elif os.path.exists(i) is False:
                        if i == "":
                            pass
                        else:
                            self.del_list.append(button_name)
                            self.del_command()
                            self.clear_note(self.gridLayout_9)
                            self.command_panel_frame_button_update()

    "голосовые из бд"
    def active_command_voice(self, button_name):
        """считывает название кнопки, выполняет команду"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sql_command_name = sqlite_Neko.voice_commands_names(conn)
            sql_command_name_source = sqlite_Neko.voice_commands_source(conn)
            main_button_name = str()
            for i in range(len(button_name)):
                if i < len(button_name) - 1:
                    main_button_name = main_button_name + str(button_name[i]) + ' '
                elif i == len(button_name) - 1:
                    main_button_name = main_button_name + str(button_name[i])
            if str(main_button_name) in sql_command_name:
                index = sql_command_name.index(str(main_button_name))
                real_name = sql_command_name_source[index]
                sql_command_type = sqlite_Neko.select_type_of_commands(conn)
                sql_command_files = sqlite_Neko.select_files_of_commands(conn)
                sql_command_site = sqlite_Neko.select_sites_of_command(conn)
                index = sql_command_name.index(str(real_name))
                command_type = sql_command_type[index]
                if command_type == 's':
                    if sql_command_site[index].find("https://"):
                        webbrowser.open_new_tab(str(sql_command_site[index]))
                    else:
                        webbrowser.open_new_tab("https://" + str(sql_command_site[index]))
                elif command_type == 'f':
                    for i in sql_command_files[index]:
                        print(sql_command_files[index])
                        if os.path.exists(i) is True:
                            subprocess.call(('cmd', '/c', 'start', '', i))
                        elif os.path.exists(i) is False:
                            if i == "":
                                pass
                            else:
                                self.del_list.append(button_name)
                                self.del_command()
                                self.clear_note(self.gridLayout_9)
                                self.command_panel_frame_button_update()
            else:
                self.play_voice_assistant_speech("Нет такой команды")

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

    def show_voice_settings(self):
        """показать головые команды"""
        self.voice_set_1.show()

    def close_voice_settings(self):
        """закрыть голосовые настройки"""
        self.voice_set_1.hide()

    def load_voice_commands_list(self):
        """загрузка команд из базы данных на фрейм с их отображением"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sql_command_name = sqlite_Neko.select_all_command(conn)
            sql_voice_names = sqlite_Neko.voice_commands_names(conn)
            sql_voice_source = sqlite_Neko.voice_commands_source(conn)
            sql_active_list = sqlite_Neko.voice_commands_status(conn)
            for i in sql_command_name:
                """Создание фрейма"""
                self.command_bd_box = QtWidgets.QGroupBox()
                self.command_bd_box.setGeometry(QtCore.QRect(50, 40, 640, 182))
                self.command_bd_box.setMinimumSize(QtCore.QSize(640, 51))
                self.command_bd_box.setMaximumSize(QtCore.QSize(640, 51))
                self.command_bd_box.setStyleSheet("background: rgba(200, 40, 40, 0.0);")
                self.command_bd_box.setTitle("")
                self.command_bd_box.setObjectName("command_bd_box")
                self.name_table = QtWidgets.QFrame(self.command_bd_box)
                self.name_table.setGeometry(QtCore.QRect(0, 0, 640, 51))
                self.name_table.setStyleSheet("background: #181818;\n"
                                              "border: 1px solid #646464;")
                self.name_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.name_table.setFrameShadow(QtWidgets.QFrame.Raised)
                self.name_table.setObjectName("name_table")
                self.source_command = QtWidgets.QLabel(self.name_table)
                self.source_command.setGeometry(QtCore.QRect(20, 13, 61, 21))
                self.source_command.setText(f"Команда {i}")
                self.source_command.setStyleSheet("background: rgba(149, 149, 149, 0.0);\n"
                                                  "color: rgba(255, 255, 255, 0.7);\n"
                                                  "border: 0px solid #646464;")
                self.button_added_2 = QtWidgets.QPushButton(self.name_table)
                self.button_added_2.setGeometry(QtCore.QRect(470, 13, 61, 21))
                self.button_added_2.setStyleSheet(" QPushButton {"
                                                  "border: 0px solid #646464;"
                                                  "background: rgba(149, 149, 149, 0.0);\n"
                                                  "color: rgba(255, 255, 255, 0.7);}\n}"
                                                  "QPushButton:hover {\n"
                                                  "color: white;}")
                self.button_added_2.setText("Раскрыть")
                self.button_added_2.clicked.connect(lambda checked,
                                                           panel=self.command_bd_box, button=self.button_added_2:
                                                    self.setSizeContainer(panel, button))
                self.button_added_2.setObjectName("button_added_2")
                self.button_added_3 = QtWidgets.QPushButton(self.name_table)
                self.button_added_3.setGeometry(QtCore.QRect(560, 13, 61, 21))
                self.button_added_3.setStyleSheet(" QPushButton {"
                                                  "border: 0px solid #646464;"
                                                  "background: rgba(149, 149, 149, 0.0);\n"
                                                  "color: rgba(255, 255, 255, 0.7);}\n}"
                                                  "QPushButton:hover {\n"
                                                  "color: white;}")
                active_counter = 0
                inactive_counter = 0
                coincidence_counter = 0
                for k in range(len(sql_voice_source)):
                    """проверка активности команды"""
                    if i == sql_voice_source[k]:
                        print(k)
                        coincidence_counter = coincidence_counter + 1
                        if sql_active_list[k] == 1:
                            active_counter = active_counter + 1
                        if sql_active_list[k] == 0:
                            inactive_counter = inactive_counter + 1
                if coincidence_counter == active_counter:
                    self.button_added_3.setText("Активно")
                elif coincidence_counter == inactive_counter:
                    self.button_added_3.setText("Неактивно")
                self.button_added_3.setObjectName("button_added_3")
                self.button_added_3.clicked.connect(lambda checked, text=i, status=self.button_added_3.text(),
                                                    button=self.button_added_3:
                                                    self.active_status(text, status, button))
                self.contain_table = QtWidgets.QFrame(self.command_bd_box)
                self.contain_table.setGeometry(QtCore.QRect(0, 53, 640, 131))
                self.contain_table.setStyleSheet("background: #181818;\n"
                                                 "border: 1px solid #646464;")
                self.contain_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.contain_table.setFrameShadow(QtWidgets.QFrame.Raised)
                self.contain_table.setObjectName("contain_table")
                placement = 10
                for j in range(len(sql_voice_names)):
                    """Добавление всех названий для команды"""
                    if sql_voice_source[j] == i:
                        self.named_command = QtWidgets.QLabel(self.contain_table)
                        self.named_command.setGeometry(QtCore.QRect(20, placement, 111, 21))
                        self.named_command.setText(f"{sql_voice_names[j]}")
                        self.named_command.setStyleSheet("background: rgba(149, 149, 149, 0.0);\n"
                                                          "color: rgba(255, 255, 255, 0.7);\n"
                                                          "border: 0px solid #646464;")
                        self.deleter = QtWidgets.QPushButton(self.contain_table)
                        self.deleter.setGeometry(QtCore.QRect(140, placement, 111, 21))
                        self.deleter.setStyleSheet(" QPushButton {"
                                                   "border: 0px solid #646464;"
                                                   "background: rgba(149, 149, 149, 0.0);\n"
                                                   "color: rgba(255, 255, 255, 0.7);}\n}"
                                                   "QPushButton:hover {\n"
                                                   "color: white;}")
                        self.deleter.setText(f"Удалить")
                        self.deleter.clicked.connect(lambda checked, text=self.named_command.text(),
                                                     button=self.deleter,
                                                     label=self.named_command:
                                                            self.del_voice_command(text, button, label))
                        self.deleter.setObjectName("deleter")
                        placement = placement + 30
                self.gridLayout_10.addWidget(self.command_bd_box)

    def setSizeContainer(self, panel, button):
        """изменяет размер контейнера"""
        panel_text = button.text()
        if panel_text == "Раскрыть":
            panel.setMinimumSize(QtCore.QSize(640, 191))
            panel.setMaximumSize(QtCore.QSize(640, 191))
            button.setText("Cкрыть")
        else:
            panel.setMinimumSize(QtCore.QSize(640, 51))
            panel.setMaximumSize(QtCore.QSize(640, 51))
            button.setText("Раскрыть")

    def del_voice_command(self, text, button, label):
        """удаляет команды"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sqlite_Neko.delete_voice_commands(conn, text)
        button.hide()
        label.hide()

    def active_status(self, name, status, button):
        """изменяет статус команды"""
        if status == "Активно":
            status = 1
        else:
            status = 0
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            sqlite_Neko.update_active_voice(conn, name, status)
        if button.text() == "Активно":
            button.setText("Неактивно")
        else:
            button.setText("Активно")
        self.clear_note(self.gridLayout_10)
        self.load_voice_commands_list()

    def set_voice_page_3(self):
        """переход на третью страницу stackwidget"""
        self.clear_note(self.gridLayout_10)
        self.load_voice_commands_list()
        self.stackedWidget.setCurrentIndex(2)

    def del_command(self):
        """delite command from database with name from del_list"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            for i in self.del_list:
                sqlite_Neko.delete_task(conn, i)
                sqlite_Neko.delete_voice_source(conn, i)
        self.clear_note(self.delite_bar)
        self.clear_note(self.gridLayout_9)
        self.show_update_item_in_area_delite_choice()


    def onActivated_1(self):
        """для выбора микрофона"""
        return self.microphone_select.currentIndex()

    def onActivated_2(self, text):
        """для выбора голосовой команды"""
        self.bd_com.setText(text)

    def microphone_search(self):
        """создает список микрофонов"""
        name_list = []
        index_list = []
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            name_list.append(name)
            index_list.append(index)
            self.microphone_select.addItem(name)
        print(name_list)

    def bd_command_searcher(self):
        """для добавления команд в combobox"""
        conn = sqlite_Neko.create_connection("Neko.db")
        names = sqlite_Neko.select_all_command(conn)
        self.command_bd_select.addItems(names)


if __name__ == "__main__":
    ttsEngine = pyttsx3.init()
    recognizer = speech_recognition.Recognizer()
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
