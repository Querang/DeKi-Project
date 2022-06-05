import speech_recognition
from PyQt5 import QtCore, QtGui, QtWidgets
import desktop_helper.sqlite_Neko as sqlite_Neko


class Ui_VoiceFrame(object):
    def setup_Voice_frame(self):
        self.page_voice_frame = QtWidgets.QWidget()
        """ voice settings frame """
        self.voice_set_1 = QtWidgets.QFrame(self.page_voice_frame)
        self.voice_set_1.setGeometry(QtCore.QRect(100, 100, 929, 445))
        self.voice_set_1.setStyleSheet("background: rgba(23, 23, 23, 0.7);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.voice_set_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.voice_set_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.voice_set_1.setObjectName("voice_set_1")
        self.button_panel_1 = QtWidgets.QFrame(self.voice_set_1)
        self.button_panel_1.setGeometry(QtCore.QRect(0, 0, 221, 445))
        self.button_panel_1.setStyleSheet("background: rgba(23, 23, 23, 1);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                          "border-radius: 13px;")
        self.button_panel_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_panel_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_panel_1.setObjectName("button_panel_1")
        self.mic_button_1 = QtWidgets.QPushButton(self.button_panel_1)
        self.mic_button_1.setGeometry(QtCore.QRect(40, 40, 151, 28))
        self.mic_button_1.setStyleSheet(" QPushButton {"
                                        "font: 12pt \"Arial\";\n"
                                        "background: rgba(149, 149, 149, 0.0);\n"
                                        "color: rgba(255, 255, 255, 0.7);}\n}"
                                        "QPushButton:hover {\n"
                                        "color: white;}")
        self.mic_button_1.setObjectName("mic_button_1")
        self.name_button_1 = QtWidgets.QPushButton(self.button_panel_1)
        self.name_button_1.setGeometry(QtCore.QRect(40, 90, 151, 28))
        self.name_button_1.setStyleSheet(" QPushButton {"
                                         "font: 12pt \"Arial\";\n"
                                         "background: rgba(149, 149, 149, 0.0);\n"
                                         "color: rgba(255, 255, 255, 0.7);}\n}"
                                         "QPushButton:hover {\n"
                                         "color: white;}")
        self.name_button_1.setObjectName("name_button_1")
        self.command_button_1 = QtWidgets.QPushButton(self.button_panel_1)
        self.command_button_1.setGeometry(QtCore.QRect(40, 140, 151, 28))
        self.command_button_1.setStyleSheet(" QPushButton {"
                                            "font: 12pt \"Arial\";\n"
                                            "background: rgba(149, 149, 149, 0.0);\n"
                                            "color: rgba(255, 255, 255, 0.7);}\n}"
                                            "QPushButton:hover {\n"
                                            "color: white;}")
        self.command_button_1.setObjectName("command_button_1")
        self.exit_button_2 = QtWidgets.QPushButton(self.button_panel_1)
        self.exit_button_2.setGeometry(QtCore.QRect(70, 410, 81, 28))
        self.exit_button_2.setStyleSheet(" QPushButton {"
                                         "font: 10pt \"Arial\";\n"
                                         "background: rgba(149, 149, 149, 0.0);\n"
                                         "color: rgba(255, 255, 255, 0.7);}\n}"
                                         "QPushButton:hover {\n"
                                         "color: white;}")
        self.exit_button_2.setObjectName("exit_button_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.voice_set_1)
        self.stackedWidget.setGeometry(QtCore.QRect(230, 10, 691, 421))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.microphone_select = QtWidgets.QComboBox(self.page_1)
        self.microphone_select.setGeometry(QtCore.QRect(20, 15, 631, 80))
        self.microphone_select.setStyleSheet("background: rgba(23, 23, 23, 0.7);;\n"
                                             "font: 18pt \"Arial\";\n"
                                             "border: 3px solid #575151;\n"
                                             "box-sizing: border-box;\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 13px;\n"
                                             "font-weight: normal;\n"
                                             "line-height: 40px;\n"
                                             "color: #FFFFFF;\n")
        self.microphone_select.setEditable(False)
        self.microphone_select.setCurrentText("")
        self.microphone_select.setObjectName("microphone_select")
        self.instr_check = QtWidgets.QLabel(self.page_1)
        self.instr_check.setGeometry(QtCore.QRect(270, 130, 191, 20))
        self.instr_check.setStyleSheet("position: absolute;\n"
                                       "width: 205px;\n"
                                       "height: 20px;\n"
                                       "left: 841px;\n"
                                       "top: 574px;\n"
                                       "background: rgba(23, 23, 23, 0);\n"
                                       "font-family: \'Roboto Mono\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 16px;\n"
                                       "line-height: 21px;\n")
        self.instr_check.setObjectName("instr_check")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.create_name_button = QtWidgets.QPushButton(self.page_2)
        self.create_name_button.setGeometry(QtCore.QRect(330, 100, 313, 51))
        self.create_name_button.setStyleSheet(" QPushButton {"
                                              "font: 12pt \"Arial\";\n"
                                              "background: rgba(149, 149, 149, 0.0);\n"
                                              "border: 3px solid #575151;\n"
                                              "box-sizing: border-box;\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "border-radius: 13px;\n"
                                              "font-weight: normal;\n"
                                              "line-height: 40px;\n"
                                              "color: rgba(255, 255, 255, 0.7);}\n}"
                                              "QPushButton:hover {\n"
                                              "color: white;}")
        self.create_name_button.setObjectName("create_name_button")
        self.instr_1 = QtWidgets.QLabel(self.page_2)
        self.instr_1.setGeometry(QtCore.QRect(110, 80, 121, 20))
        self.instr_1.setStyleSheet("position: absolute;\n"
                                   "width: 205px;\n"
                                   "height: 20px;\n"
                                   "left: 841px;\n"
                                   "top: 574px;\n"
                                   "background: rgba(23, 23, 23, 0);\n"
                                   "font-family: \'Roboto Mono\';\n"
                                   "font-style: normal;\n"
                                   "font-weight: 400;\n"
                                   "font-size: 16px;\n"
                                   "line-height: 21px;\n"
                                   "color: rgba(255, 255, 255, 1);\n")
        self.instr_1.setObjectName("instr_1")
        self.input_name_command_voice = QtWidgets.QLineEdit(self.page_2)
        self.input_name_command_voice.setGeometry(QtCore.QRect(330, 20, 313, 51))
        self.input_name_command_voice.setStyleSheet("box-sizing: border-box;\n"
                                                    "font: 12pt \"Arial\";\n"
                                                    "position: absolute;\n"
                                                    "width: 313px;\n"
                                                    "height: 51px;\n"
                                                    "left: 1108px;\n"
                                                    "top: 517px;\n"
                                                    "color: #FFFFFF;\n"
                                                    "background: rgba(233, 209, 209, 0.5);\n"
                                                    "border-radius: 11px;\n")
        self.input_name_command_voice.setObjectName("input_name_command_voice")
        self.command_bd_select = QtWidgets.QComboBox(self.page_2)
        self.command_bd_select.setGeometry(QtCore.QRect(10, 20, 309, 51))
        self.command_bd_select.setStyleSheet("background: rgba(23, 23, 23, 0.7);;\n"
                                             "font: 18pt \"Arial\";\n"
                                             "border: 3px solid #575151;\n"
                                             "box-sizing: border-box;\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 13px;\n"
                                             "font-weight: normal;\n"
                                             "line-height: 40px;\n"
                                             "color: #FFFFFF;\n")
        self.command_bd_select.setEditable(False)
        self.command_bd_select.setCurrentText("")
        self.command_bd_select.setObjectName("command_bd_select")
        self.bd_com = QtWidgets.QLabel(self.page_2)
        self.bd_com.hide()
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.scrollAreaPage3 = QtWidgets.QScrollArea(self.page_3)
        self.scrollAreaPage3.setGeometry(QtCore.QRect(0, 0, 691, 421))
        self.scrollAreaPage3.setWidgetResizable(True)
        self.scrollAreaPage3.setObjectName("scrollAreaPage3")
        self.scrollAreaWidgetContentsPage3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsPage3.setGeometry(QtCore.QRect(0, 0, 691, 421))
        self.scrollAreaWidgetContentsPage3.setObjectName("scrollAreaWidgetContentsPage3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.scrollAreaWidgetContentsPage3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_10.setAlignment(QtCore.Qt.AlignTop)
        self.scrollAreaPage3.setWidget(self.scrollAreaWidgetContentsPage3)
        self.stackedWidget.addWidget(self.page_3)
        self.mic_button_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.name_button_1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.command_button_1.clicked.connect(self.set_voice_page_3)
        self.create_name_button.clicked.connect(self.add_voice_com)
        self.microphone_search()
        self.bd_command_searcher()
        return self.page_voice_frame

    def clear_note(self, gridLayout):
        """
           Clears the resulting layout from elements
           param gridLayout_note: layout для очистки от элементов
           """
        while gridLayout.count():
            item = gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

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
            self.input_name_command_voice.setPlaceholderText("")
        elif (command_name.find("(") != -1) or (command_name.find(")") != -1):
            self.input_name_command_voice.setPlaceholderText("")
        else:
            while command_name[len(command_name) - 1] == " ":
                command_name = command_name[0: len(command_name) - 2]
            bd_name = self.command_bd_select.currentText()

        for j in sources_in_bd:
            bd_name = self.command_bd_select.currentText()
            if j == bd_name:
                count_names = count_names + 1

        name_flag = True
        for j in names_in_bd:
            if j == command_name:
                name_flag = False

        if count_names < 4 and name_flag is True:
            with conn:
                bd_name = self.command_bd_select.currentText()
                voice_com = (command_name, bd_name, 1)
                sqlite_Neko.create_voice_com(conn, voice_com)
                self.input_name_command_voice.setText("")
                self.input_name_command_voice.setPlaceholderText("access")
        else:
            if name_flag is False:
                self.input_name_command_voice.setText("")
                self.input_name_command_voice.setPlaceholderText("Такое название уже есть!")
            else:
                self.input_name_command_voice.setText("")
                self.input_name_command_voice.setPlaceholderText("Слишком много названий!")
    def set_voice_page_3(self):
        """переход на третью страницу stackwidget"""
        self.clear_note(self.gridLayout_10)
        self.load_voice_commands_list()
        self.stackedWidget.setCurrentIndex(2)

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
