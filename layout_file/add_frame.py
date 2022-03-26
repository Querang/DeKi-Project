from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_AddFrame(object):
    def setup_add_frame(self):
        self.page_add_frame = QtWidgets.QWidget()
        self.page_add_frame.setObjectName("page_add_frame")
        self.stacked_add_frame = QtWidgets.QStackedWidget(self.page_add_frame)
        self.stacked_add_frame.setGeometry(QtCore.QRect(30, 10, 1281, 734))
        self.stacked_add_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stacked_add_frame.setObjectName("stacked_add_frame")
        self.page_add_1 = QtWidgets.QWidget()
        self.page_add_1.setObjectName("page_add_1")
        self.lineedit_command = QtWidgets.QLineEdit(self.page_add_1)
        self.lineedit_command.setGeometry(QtCore.QRect(220, 450, 286, 44))
        self.lineedit_command.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                            "border-radius: 12px;\n"
                                            "font-size: 20px;\n"
                                            "line-height: 37px;\n"
                                            "\n"
                                            "color: rgba(255, 255, 255, 0.67);")
        self.lineedit_command.setAlignment(QtCore.Qt.AlignCenter)
        self.lineedit_command.setObjectName("lineedit_command")
        self.label_add_1 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_1.setGeometry(QtCore.QRect(230, 10, 271, 40))
        self.label_add_1.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_1.setObjectName("label_add_1")
        self.label_add_4 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_4.setGeometry(QtCore.QRect(300, 230, 201, 29))
        self.label_add_4.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_4.setObjectName("label_add_4")
        self.save_command_button = QtWidgets.QPushButton(self.page_add_1)
        self.save_command_button.setGeometry(QtCore.QRect(250, 500, 226, 37))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_command_button.sizePolicy().hasHeightForWidth())
        self.save_command_button.setSizePolicy(sizePolicy)
        self.save_command_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.save_command_button.setAutoFillBackground(False)
        self.save_command_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 12px;\n"
                                               "font-size: 20px;\n"
                                               "line-height: 37px;\n"
                                               "\n"
                                               "color: rgba(255, 255, 255, 0.67);")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("material/image 32.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.save_command_button.setIcon(icon4)
        self.save_command_button.setObjectName("save_command_button")
        self.label_add_click_1 = QtWidgets.QLabel(self.page_add_1)
        self.label_add_click_1.setGeometry(QtCore.QRect(120, 90, 61, 31))
        self.label_add_click_1.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 6px;\n"
                                             "font: 8pt \"Arial\";\n"
                                             "font-style: normal;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 12px;\n"
                                             "line-height: 18px;\n"
                                             "padding: 0 0 0 5px;\n"
                                             "color: #FFFFFF;")
        self.label_add_click_1.setObjectName("label_add_click_1")
        self.label_29 = QtWidgets.QLabel(self.page_add_1)
        self.label_29.setGeometry(QtCore.QRect(20, 10, 172, 137))
        self.label_29.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                    "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                    "border-radius: 6px;")
        self.label_29.setObjectName("label_29")
        self.label_add_7 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_7.setGeometry(QtCore.QRect(230, 410, 31, 27))
        self.label_add_7.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_7.setObjectName("label_add_7")
        self.lineedit_site = QtWidgets.QLineEdit(self.page_add_1)
        self.lineedit_site.setGeometry(QtCore.QRect(230, 280, 261, 34))
        self.lineedit_site.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 12px;\n"
                                         "font-size: 20px;\n"
                                         "line-height: 37px;\n"
                                         "\n"
                                         "color: rgba(255, 255, 255, 0.67);")
        self.lineedit_site.setAlignment(QtCore.Qt.AlignCenter)
        self.lineedit_site.setObjectName("lineedit_site")
        self.label_add_6 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_6.setGeometry(QtCore.QRect(230, 370, 141, 27))
        self.label_add_6.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_6.setObjectName("label_add_6")
        self.character_add_label = QtWidgets.QLabel(self.page_add_1)
        self.character_add_label.setGeometry(QtCore.QRect(20, 0, 121, 151))
        self.character_add_label.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;")
        self.character_add_label.setText("")
        self.character_add_label.setPixmap(QtGui.QPixmap("material/Firo/Firo_s.png"))
        self.character_add_label.setObjectName("character_add_label")
        self.label_add_2 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_2.setGeometry(QtCore.QRect(230, 60, 251, 27))
        self.label_add_2.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_2.setObjectName("label_add_2")
        self.label_add_5 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_5.setGeometry(QtCore.QRect(230, 330, 261, 27))
        self.label_add_5.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_5.setObjectName("label_add_5")
        self.label_add_click_3 = QtWidgets.QLabel(self.page_add_1)
        self.label_add_click_3.setGeometry(QtCore.QRect(1195, 506, 61, 31))
        self.label_add_click_3.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 6px;\n"
                                             "font: 8pt \"Arial\";\n"
                                             "font-style: normal;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 12px;\n"
                                             "line-height: 18px;\n"
                                             "padding: 0 0 0 5px;\n"
                                             "color: #FFFFFF;")
        self.label_add_click_3.setObjectName("label_add_click_3")
        self.back_from_add_button = QtWidgets.QPushButton(self.page_add_1)
        self.back_from_add_button.setGeometry(QtCore.QRect(20, 200, 171, 38))
        self.back_from_add_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                                "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                "border-radius: 10px;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 27px;\n"
                                                "\n"
                                                "color: #FFFFFF;")
        self.back_from_add_button.setObjectName("back_from_add_button")
        self.background_bread_button = QtWidgets.QFrame(self.page_add_1)
        self.background_bread_button.setGeometry(QtCore.QRect(240, 140, 261, 77))
        self.background_bread_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                                   "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                   "border-radius: 12px;")
        self.background_bread_button.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_bread_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_bread_button.setObjectName("background_bread_button")
        self.bread_button_2 = QtWidgets.QPushButton(self.background_bread_button)
        self.bread_button_2.setGeometry(QtCore.QRect(0, -10, 137, 79))
        self.bread_button_2.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                          "border-radius: 13px;\n"
                                          "font-size: 18px;\n"
                                          "line-height: 27px;\n"
                                          "\n"
                                          "color: #FFFFFF;")
        self.bread_button_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("material/image 43.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.bread_button_2.setIcon(icon5)
        self.bread_button_2.setIconSize(QtCore.QSize(155, 99))
        self.bread_button_2.setObjectName("bread_button_2")
        self.label_add_click_2 = QtWidgets.QLabel(self.background_bread_button)
        self.label_add_click_2.setGeometry(QtCore.QRect(130, 30, 61, 31))
        self.label_add_click_2.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 6px;\n"
                                             "font: 8pt \"Arial\";\n"
                                             "font-style: normal;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 12px;\n"
                                             "line-height: 18px;\n"
                                             "padding: 0 0 0 5px;\n"
                                             "color: #FFFFFF;")
        self.label_add_click_2.setObjectName("label_add_click_2")
        self.file_button = QtWidgets.QPushButton(self.background_bread_button)
        self.file_button.setEnabled(True)
        self.file_button.setGeometry(QtCore.QRect(190, 10, 56, 52))
        self.file_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.file_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("material/image 75.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.file_button.setIcon(icon6)
        self.file_button.setIconSize(QtCore.QSize(50, 50))
        self.file_button.setAutoDefault(False)
        self.file_button.setDefault(False)
        self.file_button.setObjectName("file_button")
        self.label_add_click_4 = QtWidgets.QLabel(self.page_add_1)
        self.label_add_click_4.setGeometry(QtCore.QRect(1195, 636, 61, 31))
        self.label_add_click_4.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                             "border-radius: 6px;\n"
                                             "font: 8pt \"Arial\";\n"
                                             "font-style: normal;\n"
                                             "font-weight: 400;\n"
                                             "font-size: 12px;\n"
                                             "line-height: 18px;\n"
                                             "padding: 0 0 0 5px;\n"
                                             "color: #FFFFFF;")
        self.label_add_click_4.setObjectName("label_add_click_4")
        self.card_board_box_button = QtWidgets.QPushButton(self.page_add_1)
        self.card_board_box_button.setEnabled(True)
        self.card_board_box_button.setGeometry(QtCore.QRect(1170, 430, 102, 106))
        self.card_board_box_button.setStyleSheet("background: rgba(23, 23, 23, 0.7);\n"
                                                 "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                 "border-radius: 13px;")
        self.card_board_box_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("material/image 78.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.card_board_box_button.setIcon(icon7)
        self.card_board_box_button.setIconSize(QtCore.QSize(50, 50))
        self.card_board_box_button.setAutoDefault(False)
        self.card_board_box_button.setDefault(False)
        self.card_board_box_button.setObjectName("card_board_box_button")
        self.info_button = QtWidgets.QPushButton(self.page_add_1)
        self.info_button.setEnabled(True)
        self.info_button.setGeometry(QtCore.QRect(120, 40, 56, 52))
        self.info_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.info_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("material/image 74.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.info_button.setIcon(icon8)
        self.info_button.setIconSize(QtCore.QSize(50, 50))
        self.info_button.setAutoDefault(False)
        self.info_button.setDefault(False)
        self.info_button.setObjectName("info_button")
        self.label_add_8 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_8.setGeometry(QtCore.QRect(20, 152, 171, 41))
        self.label_add_8.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 12px;\n"
                                       "line-height: 18px;\n"
                                       "padding: 0 0 0 5px;\n"
                                       "color: #FFFFFF;")
        self.label_add_8.setObjectName("label_add_8")
        self.label_add_3 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_3.setGeometry(QtCore.QRect(230, 100, 131, 27))
        self.label_add_3.setStyleSheet("background: rgba(233, 209, 209, 0.3);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 6px;\n"
                                       "font-family: \'Titillium Web\';\n"
                                       "font-style: normal;\n"
                                       "font-weight: 400;\n"
                                       "font-size: 13px;\n"
                                       "line-height: 20px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.label_add_3.setObjectName("label_add_3")
        self.trash_can_button = QtWidgets.QPushButton(self.page_add_1)
        self.trash_can_button.setEnabled(True)
        self.trash_can_button.setGeometry(QtCore.QRect(1170, 560, 102, 106))
        self.trash_can_button.setStyleSheet("background: rgba(23, 23, 23, 0.7);\n"
                                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                            "border-radius: 13px;")
        self.trash_can_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("material/image 80.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.trash_can_button.setIcon(icon9)
        self.trash_can_button.setIconSize(QtCore.QSize(50, 50))
        self.trash_can_button.setAutoDefault(False)
        self.trash_can_button.setDefault(False)
        self.trash_can_button.setObjectName("trash_can_button")
        self.background_message = QtWidgets.QLabel(self.page_add_1)
        self.background_message.setEnabled(True)
        self.background_message.setGeometry(QtCore.QRect(210, -1, 303, 550))
        self.background_message.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "border-radius: 13px;\n"
                                              "font-size: 12px;\n"
                                              "line-height: 27px;\n"
                                              "\n"
                                              "color: #FFFFFF;")
        self.background_message.setText("")
        self.background_message.setPixmap(QtGui.QPixmap("material/Component 3 (2).png"))
        self.background_message.setScaledContents(True)
        self.background_message.setWordWrap(False)
        self.background_message.setObjectName("background_message")
        self.label_info_2 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_info_2.setGeometry(QtCore.QRect(530, 260, 311, 61))
        self.label_info_2.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                        "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        "border-radius: 6px;\n"
                                        "font-family: \'Titillium Web\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "font-size: 12px;\n"
                                        "line-height: 18px;\n"
                                        "padding: 0 0 0 5px;\n"
                                        "color: #FFFFFF;")
        self.label_info_2.setObjectName("label_info_2")
        self.label_add_13 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_add_13.setGeometry(QtCore.QRect(530, 150, 311, 61))
        self.label_add_13.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                        "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        "border-radius: 6px;\n"
                                        "font-family: \'Titillium Web\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "font-size: 12px;\n"
                                        "line-height: 18px;\n"
                                        "padding: 0 0 0 5px;\n"
                                        "color: #FFFFFF;")
        self.label_add_13.setObjectName("label_add_13")
        self.label_info_3 = QtWidgets.QTextBrowser(self.page_add_1)
        self.label_info_3.setGeometry(QtCore.QRect(930, 380, 211, 151))
        self.label_info_3.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                        "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                        "border-radius: 6px;\n"
                                        "font-family: \'Titillium Web\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 400;\n"
                                        "font-size: 12px;\n"
                                        "line-height: 18px;\n"
                                        "padding: 0 0 0 5px;\n"
                                        "color: #FFFFFF;")
        self.label_info_3.setObjectName("label_info_3")
        self.del_bar_frame = QtWidgets.QFrame(self.page_add_1)
        self.del_bar_frame.setGeometry(QtCore.QRect(659, 540, 501, 141))
        self.del_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.del_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.del_bar_frame.setObjectName("del_bar_frame")
        self.delite_area = QtWidgets.QScrollArea(self.del_bar_frame)
        self.delite_area.setGeometry(QtCore.QRect(10, 20, 411, 51))
        self.delite_area.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.delite_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delite_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delite_area.setWidgetResizable(True)
        self.delite_area.setObjectName("delite_area")
        self.delite_area_container = QtWidgets.QWidget()
        self.delite_area_container.setGeometry(QtCore.QRect(0, 0, 411, 51))
        self.delite_area_container.setStyleSheet("background: rgba(23, 23, 23, 0.0);")
        self.delite_area_container.setObjectName("delite_area_container")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.delite_area_container)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.delite_area.setWidget(self.delite_area_container)
        self.label_about_delite = QtWidgets.QTextBrowser(self.del_bar_frame)
        self.label_about_delite.setGeometry(QtCore.QRect(10, 80, 171, 41))
        self.label_about_delite.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "border-radius: 6px;\n"
                                              "font-family: \'Titillium Web\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 12px;\n"
                                              "line-height: 18px;\n"
                                              "padding: 0 0 0 5px;\n"
                                              "color: #FFFFFF;")
        self.label_about_delite.setObjectName("label_about_delite")
        self.delite_button = QtWidgets.QPushButton(self.del_bar_frame)
        self.delite_button.setGeometry(QtCore.QRect(430, 20, 70, 34))
        self.delite_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 13px;\n"
                                         "font-size: 13px;\n"
                                         "line-height: 27px;\n"
                                         "\n"
                                         "color: #FFFFFF;")
        self.delite_button.setObjectName("delite_button")
        self.del_bar_frame.raise_()
        self.label_29.raise_()
        self.background_message.raise_()
        self.card_board_box_button.raise_()
        self.trash_can_button.raise_()
        self.lineedit_command.raise_()
        self.label_add_1.raise_()
        self.label_add_4.raise_()
        self.save_command_button.raise_()
        self.label_add_click_1.raise_()
        self.label_add_7.raise_()
        self.lineedit_site.raise_()
        self.label_add_6.raise_()
        self.character_add_label.raise_()
        self.label_add_2.raise_()
        self.label_add_5.raise_()
        self.label_add_click_3.raise_()
        self.back_from_add_button.raise_()
        self.background_bread_button.raise_()
        self.label_add_click_4.raise_()
        self.info_button.raise_()
        self.label_add_8.raise_()
        self.label_add_3.raise_()
        self.label_info_2.raise_()
        self.label_add_13.raise_()
        self.label_info_3.raise_()

        self.label_add_13.hide()
        self.label_info_2.hide()
        self.label_info_3.hide()
        self.label_about_delite.hide()
        self.del_bar_frame.hide()
        return self.page_add_1