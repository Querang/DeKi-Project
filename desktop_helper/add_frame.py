import os
import subprocess
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite_Neko


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
        self.label_add_4.setGeometry(QtCore.QRect(300, 230, 201, 42))
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
        self.back_from_add_button.setStyleSheet(" QPushButton {"
                                                "background: rgba(23, 23, 23, 0.9);\n"
                                                "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                "border-radius: 10px;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 27px;\n"
                                                "color: rgba(255, 255, 255, 0.7);}\n"
                                                "QPushButton:hover {\n"
                                                "color: white;}")
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

                                       "padding: 10px 0 0 5px;\n"
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
        self.delete_area = QtWidgets.QScrollArea(self.del_bar_frame)
        self.delete_area.setGeometry(QtCore.QRect(10, 20, 411, 51))
        self.delete_area.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.delete_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delete_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.delete_area.setWidgetResizable(True)
        self.delete_area.setObjectName("delete_area")
        self.delete_area_container = QtWidgets.QWidget()
        self.delete_area_container.setGeometry(QtCore.QRect(0, 0, 411, 51))
        self.delete_area_container.setStyleSheet("background: rgba(23, 23, 23, 0.0);")
        self.delete_area_container.setObjectName("delete_area_container")
        self.delete_bar_grid = QtWidgets.QGridLayout(self.delete_area_container)
        self.delete_bar_grid.setObjectName("delete_bar_grid")
        self.delete_bar_grid.setAlignment(QtCore.Qt.AlignLeft)
        self.delete_area.setWidget(self.delete_area_container)
        self.label_about_delete = QtWidgets.QTextBrowser(self.del_bar_frame)
        self.label_about_delete.setGeometry(QtCore.QRect(10, 80, 171, 41))
        self.label_about_delete.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                              "border-radius: 6px;\n"
                                              "font-family: \'Titillium Web\';\n"
                                              "font-style: normal;\n"
                                              "font-weight: 400;\n"
                                              "font-size: 12px;\n"
                                              "line-height: 18px;\n"
                                              "padding: 0 0 0 5px;\n"
                                              "color: #FFFFFF;")
        self.label_about_delete.setObjectName("label_about_delete")
        self.delete_button = QtWidgets.QPushButton(self.del_bar_frame)
        self.delete_button.setGeometry(QtCore.QRect(430, 20, 70, 34))
        self.delete_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 13px;\n"
                                         "font-size: 13px;\n"
                                         "line-height: 27px;\n"
                                         "\n"
                                         "color: #FFFFFF;")
        self.delete_button.setObjectName("delete_button")
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
        self.label_about_delete.hide()
        self.del_bar_frame.hide()
        self.trash_can_button_flag = False
        self.trash_can_button.clicked.connect(self.delete_command_switch)
        self.container_flow = QtWidgets.QFrame(self.page_add_1)
        self.container_flow.setGeometry(QtCore.QRect(600, 150, 281, 311))
        self.Flowlayout_for_folder = FlowLayout()
        self.container_flow.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                            "border-radius: 13px;\n"
                            "font-size: 12px;\n"
                            "line-height: 27px;\n"
                            "\n"
                            "color: #FFFFFF;")

        """add variable"""
        self.container_flow.setLayout(self.Flowlayout_for_folder)
        return self.page_add_1

    def delete_command_switch(self):
        if self.trash_can_button_flag:
            self.del_bar_frame.hide()
        else:
            self.del_bar_frame.show()
        self.trash_can_button_flag = not self.trash_can_button_flag

    def clear_note(self, gridLayout):
        """
           Clears the resulting layout from elements
           param gridLayout_note: layout для очистки от элементов
           """
        while gridLayout.count():
            item = gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()

    def get_directory(self):
        """select files for action"""
        folder = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", "/")[0]
        self.directory_list.append(folder)
        print(self.directory_list)
        label = QtWidgets.QLabel()
        label.setMinimumSize(121, 151)

        label.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                            "border-radius: 13px;\n"
                            "font-size: 12px;\n"
                            "line-height: 27px;\n"
                            "\n"
                            "color: #FFFFFF;")

        ne = folder[:20] + "\n" + folder[20:40:] + "\n" + folder[40:60:] + "\n" + folder[60::]
        label.setText(ne)
        self.Flowlayout_for_folder.addWidget(label)

    def add_date_in_Neko_bd(self):
        """add command to database"""
        self.link_site = self.lineedit_site.text()
        if self.directory_list != []:
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.lineedit_command.text()
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
                self.clear_note(self.delete_bar_grid)
                self.lineedit_command.setText("access")
        elif self.directory_list == []:
            conn = sqlite_Neko.create_connection("Neko.db")
            command = self.lineedit_command.text()
            with conn:
                task = ("s", "", "", "", "", self.link_site, command)
                sqlite_Neko.create_task(conn, task)
                self.lineedit_command.setText("access")

        else:
            self.lineedit_command.setText("fail")
        self.clear_note(self.delete_bar_grid)
        self.show_update_item_in_area_delete_choice()
        self.clear_note(self.Flowlayout_for_folder)
        self.command_panel_frame_button_update()

    def show_update_item_in_area_delete_choice(self):
        """updates buttons containing commands"""

        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i, j in enumerate(name):
            if len(name) > 3:
                self.delete_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            else:
                self.delete_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.pushButton = QtWidgets.QPushButton()
            self.pushButton.setMinimumSize(112, 19)
            self.pushButton.setMaximumSize(112, 19)
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
            self.delete_bar_grid.addWidget(self.pushButton, 0, i)

    # def command_panel_frame_button_update(self):
    #     """обновляет кнопки, содержащие команды для выполнения"""
    #     conn = sqlite_Neko.create_connection("Neko.db")
    #     with conn:
    #         name = sqlite_Neko.select_all_command(conn)
    #         print(name)
    #     for i, j in enumerate(name):
    #         self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    #         self.pushButton = QtWidgets.QPushButton()
    #         self.pushButton.setMinimumSize(140, 52)
    #         self.pushButton.setMaximumSize(140, 52)
    #         self.pushButton.setStyleSheet("border-radius: 2px;\n"
    #                                       "font: 12pt \"MS Shell Dlg 2\";\n"
    #                                       "color: rgba(255, 255, 255, 0.67);\n"
    #                                       "\n"
    #                                       "background: rgba(23, 23, 23, 0.31);\n"
    #                                       "border: 1px solid rgba(233, 233, 233, 0.22);\n"
    #                                       "box-sizing: border-box;\n"
    #                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
    #         self.pushButton.setText(f"{j}")
    #         self.pushButton.clicked.connect(lambda checked, button=self.pushButton: self.active_command_button(button))
    #         self.gridLayout_9.addWidget(self.pushButton, i, 0)

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
        """delete command from database with name from del_list"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            for i in self.del_list:
                sqlite_Neko.delete_task(conn, i)
        self.clear_note(self.delete_bar_grid)
        self.show_update_item_in_area_delete_choice()


class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, hspacing=15, vspacing=10):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, 0, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        for item in self._items:
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + hspace
            if nextX - hspace > effective.right() and lineheight > 0:
                x = effective.x()
                y = y + lineheight + vspace
                nextX = x + item.sizeHint().width() + hspace
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
