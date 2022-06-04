from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingFrame(object):

    def setup_settinf_frame(self):

        self.setting_page = QtWidgets.QWidget()
        self.setting_page.setObjectName("setting_page")
        self.stackedWidget_setting_page = QtWidgets.QStackedWidget(self.setting_page)
        self.stackedWidget_setting_page.setGeometry(QtCore.QRect(100, 100, 981, 481))
        self.stackedWidget_setting_page.setObjectName("stackedWidget_setting_page")
        self.setting_page_3 = QtWidgets.QWidget()
        self.setting_page_3.setObjectName("setting_page_3")
        self.setting_page_2 = QtWidgets.QFrame(self.setting_page_3)
        self.setting_page_2.setGeometry(QtCore.QRect(10, 20, 929, 445))
        self.setting_page_2.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.35);\n"
                                          "border-radius: 13px;")
        self.setting_page_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setting_page_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setting_page_2.setObjectName("setting_page_2")
        self.label_setting_page_2 = QtWidgets.QLabel(self.setting_page_2)
        self.label_setting_page_2.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.label_setting_page_2.setStyleSheet("font: 8pt \"Arial\";\n"
                                                "font-style: normal;\n"
                                                "font-weight: normal;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 34px;\n"
                                                "/* identical to box height */\n"
                                                "background: rgba(33, 24, 24, 0.0);\n"
                                                "\n"
                                                "color: #FFFFFF;\n"
                                                "")
        self.label_setting_page_2.setObjectName("label_setting_page_2")
        self.label_window_page_2 = QtWidgets.QLabel(self.setting_page_2)
        self.label_window_page_2.setGeometry(QtCore.QRect(10, 56, 169, 55))
        self.label_window_page_2.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                               "font: 18pt \"Arial\";\n"
                                               "border: 3px solid #575151;\n"
                                               "box-sizing: border-box;\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;\n"
                                               "\n"
                                               "font-weight: normal;\n"
                                               "\n"
                                               "line-height: 40px;\n"
                                               "\n"
                                               "color: #FFFFFF;\n"
                                               "")
        self.label_window_page_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_window_page_2.setObjectName("label_window_page_2")
        self.label_normal_window_page_2 = QtWidgets.QLabel(self.setting_page_2)
        self.label_normal_window_page_2.setGeometry(QtCore.QRect(220, 56, 561, 55))
        self.label_normal_window_page_2.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                                      "font: 18pt \"Arial\";\n"
                                                      "border: 3px solid #575151;\n"
                                                      "box-sizing: border-box;\n"
                                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                      "border-radius: 13px;\n"
                                                      "\n"
                                                      "font-weight: normal;\n"
                                                      "\n"
                                                      "line-height: 40px;\n"
                                                      "\n"
                                                      "color: #FFFFFF;\n"
                                                      "")
        self.label_normal_window_page_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_normal_window_page_2.setObjectName("label_normal_window_page_2")
        self.label_page_2 = QtWidgets.QLabel(self.setting_page_2)
        self.label_page_2.setGeometry(QtCore.QRect(786, 10, 91, 31))
        self.label_page_2.setStyleSheet("background: rgba(33, 24, 24, 0.0);\n"
                                        "font: 16pt \"Arial\";\n"
                                        "box-sizing: border-box;\n"
                                        "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        "border-radius: 13px;\n"
                                        "\n"
                                        "font-weight: normal;\n"
                                        "\n"
                                        "line-height: 40px;\n"
                                        "\n"
                                        "color: #FFFFFF;\n"
                                        "")
        self.label_page_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page_2.setObjectName("label_page_2")
        self.button_window_r_2 = QtWidgets.QPushButton(self.setting_page_2)
        self.button_window_r_2.setGeometry(QtCore.QRect(740, 70, 31, 26))
        self.button_window_r_2.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_window_r_2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("material/image 38.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.button_window_r_2.setIcon(icon10)
        self.button_window_r_2.setObjectName("button_window_r_2")
        self.button_window_l_2 = QtWidgets.QPushButton(self.setting_page_2)
        self.button_window_l_2.setGeometry(QtCore.QRect(230, 70, 31, 26))
        self.button_window_l_2.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_window_l_2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("material/image 52.png"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.button_window_l_2.setIcon(icon11)
        self.button_window_l_2.setObjectName("button_window_l_2")
        self.button_on_1_page = QtWidgets.QPushButton(self.setting_page_2)
        self.button_on_1_page.setGeometry(QtCore.QRect(761, 13, 31, 26))
        self.button_on_1_page.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_on_1_page.setText("")
        self.button_on_1_page.setIcon(icon11)
        self.button_on_1_page.setObjectName("button_on_1_page")
        self.stackedWidget_setting_page.addWidget(self.setting_page_3)
        self.setting_page_1 = QtWidgets.QWidget()
        self.setting_page_1.setObjectName("setting_page_1")
        self.page_setting_1 = QtWidgets.QFrame(self.setting_page_1)
        self.page_setting_1.setGeometry(QtCore.QRect(10, 20, 929, 445))
        self.page_setting_1.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.35);\n"
                                          "border-radius: 13px;")
        self.page_setting_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.page_setting_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.page_setting_1.setObjectName("page_setting_1")
        self.label_setting = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting.setGeometry(QtCore.QRect(20, 0, 71, 31))
        self.label_setting.setStyleSheet("font: 8pt \"Arial\";\n"
                                         "font-style: normal;\n"
                                         "font-weight: normal;\n"
                                         "font-size: 14px;\n"
                                         "line-height: 34px;\n"
                                         "/* identical to box height */\n"
                                         "background: rgba(33, 24, 24, 0.0);\n"
                                         "\n"
                                         "color: #FFFFFF;\n"
                                         "")
        self.label_setting.setObjectName("label_setting")
        self.label_setting_1 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_1.setGeometry(QtCore.QRect(10, 80, 403, 75))
        self.label_setting_1.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                           "font: 18pt \"Arial\";\n"
                                           "border: 3px solid #575151;\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 11px;\n"
                                           "\n"
                                           "font-weight: normal;\n"
                                           "\n"
                                           "line-height: 40px;\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setting_1.setObjectName("label_setting_1")
        self.label_setting_4 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_4.setGeometry(QtCore.QRect(10, 310, 169, 55))
        self.label_setting_4.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                           "font: 18pt \"Arial\";\n"
                                           "border: 3px solid #575151;\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;\n"
                                           "\n"
                                           "font-weight: normal;\n"
                                           "\n"
                                           "line-height: 40px;\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setting_4.setObjectName("label_setting_4")
        self.label_setting_5 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_5.setGeometry(QtCore.QRect(10, 375, 169, 55))
        self.label_setting_5.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                           "font: 18pt \"Arial\";\n"
                                           "border: 3px solid #575151;\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;\n"
                                           "\n"
                                           "font-weight: normal;\n"
                                           "\n"
                                           "line-height: 40px;\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setting_5.setObjectName("label_setting_5")
        self.label_setting_2 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_2.setGeometry(QtCore.QRect(140, 160, 141, 31))
        self.label_setting_2.setStyleSheet("font-family: Roboto Mono;\n"
                                           "font-style: normal;\n"
                                           "font-weight: normal;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 34px;\n"
                                           "/* identical to box height */\n"
                                           "background: rgba(33, 24, 24, 0.0);\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_2.setObjectName("label_setting_2")
        self.Nickname_2 = QtWidgets.QLineEdit(self.page_setting_1)
        self.Nickname_2.setGeometry(QtCore.QRect(100, 210, 226, 58))
        self.Nickname_2.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                      "border: 3px solid #575151;\n"
                                      "box-sizing: border-box;\n"
                                      "font: 18pt \"Arial\";\n"
                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                      "border-radius: 8px;\n"
                                      "font-weight: normal;\n"
                                      "\n"
                                      "line-height: 40px;\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.Nickname_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Nickname_2.setObjectName("Nickname_2")
        self.Nickname_2.setPlaceholderText("Nickname")
        self.label_setting_6 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_6.setGeometry(QtCore.QRect(220, 310, 561, 55))
        self.label_setting_6.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                           "font: 18pt \"Arial\";\n"
                                           "border: 3px solid #575151;\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;\n"
                                           "\n"
                                           "font-weight: normal;\n"
                                           "\n"
                                           "line-height: 40px;\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setting_6.setObjectName("label_setting_6")
        self.label_setting_7 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_7.setGeometry(QtCore.QRect(220, 376, 561, 55))
        self.label_setting_7.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                           "font: 18pt \"Arial\";\n"
                                           "border: 3px solid #575151;\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;\n"
                                           "\n"
                                           "font-weight: normal;\n"
                                           "\n"
                                           "line-height: 40px;\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setting_7.setObjectName("label_setting_7")
        self.character_set = QtWidgets.QLabel(self.page_setting_1)
        self.character_set.setGeometry(QtCore.QRect(470, 0, 167, 234))
        self.character_set.setStyleSheet("background: rgba(33, 24, 24, 0.0);\n"
                                         "font: 18pt \"Arial\";\n"
                                         "\n"
                                         "box-sizing: border-box;\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 13px;\n"
                                         "\n"
                                         "font-weight: normal;\n"
                                         "\n"
                                         "line-height: 40px;\n"
                                         "\n"
                                         "color: #FFFFFF;\n"
                                         "")
        self.character_set.setText("")
        self.character_set.setPixmap(QtGui.QPixmap("material/Firo/Firo_setting.png"))
        self.character_set.setAlignment(QtCore.Qt.AlignCenter)
        self.character_set.setObjectName("character_set")
        self.button_save = QtWidgets.QPushButton(self.page_setting_1)
        self.button_save.setGeometry(QtCore.QRect(800, 310, 106, 55))
        self.button_save.setStyleSheet(" QPushButton {"
                                         "background: rgba(23, 23, 23, 0.8);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        
                                         "border: 1px solid #B19696;\n"
                                          "font-size: 26px;\n"
                                         "line-height: 15px;\n"
                            
                                         "border-radius: 13px;\n"
                                         "color: rgba(255, 255, 255, 0.7);}\n"
                                         "QPushButton:hover {\n"
                                         "color: white;}")
        self.button_save.setObjectName("button_save")
        self.back_fome_setting_button = QtWidgets.QPushButton(self.page_setting_1)
        self.back_fome_setting_button.setGeometry(QtCore.QRect(800, 370, 106, 55))
        self.back_fome_setting_button.setStyleSheet(" QPushButton {"
                                       "background: rgba(23, 23, 23, 0.8);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"

                                       "border: 1px solid #B19696;\n"
                                         "font-size: 26px;\n"
                                       "line-height: 15px;\n"

                                       "border-radius: 13px;\n"
                                       "color: rgba(255, 255, 255, 0.7);}\n"
                                       "QPushButton:hover {\n"
                                       "color: white;}")
        self.back_fome_setting_button.setObjectName("back_fome_setting_button")
        self.label_setting_8 = QtWidgets.QLabel(self.page_setting_1)
        self.label_setting_8.setGeometry(QtCore.QRect(720, 56, 171, 31))
        self.label_setting_8.setStyleSheet("font: 8pt \"Arial\";\n"
                                           "font-style: normal;\n"
                                           "font-weight: normal;\n"
                                           "font-size: 14px;\n"
                                           "line-height: 34px;\n"
                                           "/* identical to box height */\n"
                                           "background: rgba(33, 24, 24, 0.0);\n"
                                           "\n"
                                           "color: #FFFFFF;\n"
                                           "")
        self.label_setting_8.setObjectName("label_setting_8")
        self.Nickname_1 = QtWidgets.QLineEdit(self.page_setting_1)
        self.Nickname_1.setGeometry(QtCore.QRect(690, 90, 226, 58))
        self.Nickname_1.setStyleSheet("background: rgba(23, 23, 23, 0.8);\n"
                                      "border: 3px solid #575151;\n"
                                      "box-sizing: border-box;\n"
                                      "font: 18pt \"Arial\";\n"
                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                      "border-radius: 8px;\n"
                                      "font-weight: normal;\n"
                                      "\n"
                                      "line-height: 40px;\n"
                                      "\n"
                                      "color: #FFFFFF;")
        self.Nickname_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Nickname_1.setObjectName("Nickname_1")
        self.Nickname_1.setPlaceholderText("Nickname")
        self.label_10 = QtWidgets.QLabel(self.page_setting_1)
        self.label_10.setGeometry(QtCore.QRect(770, 10, 121, 31))
        self.label_10.setStyleSheet("background: rgba(33, 24, 24, 0.0);\n"
                                    "font: 16pt \"Arial\";\n"
                                    "box-sizing: border-box;\n"
                                    "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 13px;\n"
                                    "\n"
                                    "font-weight: normal;\n"
                                    "\n"
                                    "line-height: 40px;\n"
                                    "\n"
                                    "color: #FFFFFF;\n"
                                    "")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.next_on_page_2_button = QtWidgets.QPushButton(self.page_setting_1)
        self.next_on_page_2_button.setGeometry(QtCore.QRect(890, 14, 31, 26))
        self.next_on_page_2_button.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.next_on_page_2_button.setText("")
        self.next_on_page_2_button.setIcon(icon10)
        self.next_on_page_2_button.setObjectName("next_on_page_2_button")
        self.button_language_r = QtWidgets.QPushButton(self.page_setting_1)
        self.button_language_r.setGeometry(QtCore.QRect(740, 324, 31, 26))
        self.button_language_r.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_language_r.setText("")
        self.button_language_r.setIcon(icon10)
        self.button_language_r.setObjectName("button_language_r")
        self.button_behavior_r = QtWidgets.QPushButton(self.page_setting_1)
        self.button_behavior_r.setGeometry(QtCore.QRect(740, 390, 31, 26))
        self.button_behavior_r.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_behavior_r.setText("")
        self.button_behavior_r.setIcon(icon10)
        self.button_behavior_r.setObjectName("button_behavior_r")
        self.button_language_l = QtWidgets.QPushButton(self.page_setting_1)
        self.button_language_l.setGeometry(QtCore.QRect(230, 324, 31, 26))
        self.button_language_l.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_language_l.setText("")
        self.button_language_l.setIcon(icon11)
        self.button_language_l.setObjectName("button_language_l")
        self.button_behavior_l = QtWidgets.QPushButton(self.page_setting_1)
        self.button_behavior_l.setGeometry(QtCore.QRect(230, 390, 31, 26))
        self.button_behavior_l.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_behavior_l.setText("")
        self.button_behavior_l.setIcon(icon11)
        self.button_behavior_l.setObjectName("button_behavior_l")
        self.button_character_r = QtWidgets.QPushButton(self.page_setting_1)
        self.button_character_r.setGeometry(QtCore.QRect(640, 130, 31, 26))
        self.button_character_r.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_character_r.setText("")
        self.button_character_r.setIcon(icon10)
        self.button_character_r.setObjectName("button_character_r")
        self.button_character_l = QtWidgets.QPushButton(self.page_setting_1)
        self.button_character_l.setGeometry(QtCore.QRect(450, 130, 31, 26))
        self.button_character_l.setStyleSheet("background: rgba(33, 24, 24, 0.0);")
        self.button_character_l.setText("")
        self.button_character_l.setIcon(icon11)
        self.button_character_l.setObjectName("button_character_l")
        self.stackedWidget_setting_page.addWidget(self.setting_page_1)
        self.stackedWidget_setting_page.setCurrentIndex(1)
        """set button"""
        self.button_save.clicked.connect(self.save_global_setting)
        return self.setting_page



    def Next_main_window_size(self):
        self.next_main_frame = not self.next_main_frame
        if self.next_main_frame:
            self.main_window_size = "min"
        else:
            self.main_window_size = "normal"
        self.label_normal_window_page_2.setText(self.main_window_size)

    # def Next_language(self):
    #     """allows you to change the language in the settings
    #        param language_index: needed to determine the current language
    #        """
    #     language_index = self.language_list.index(self.language)
    #     language_index += 1
    #     if language_index == len(self.language_list):
    #         language_index = 0
    #     self.language = self.language_list[language_index]
    #     if self.language == "russian":
    #         self.set_ru()
    #     elif self.language == "english":
    #         self.set_en()






