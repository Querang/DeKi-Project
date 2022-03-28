from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMinFrame(object):
    def setup_main_min_frame(self):
        self.page_main_min = QtWidgets.QWidget()
        self.page_main_min.setObjectName("page_main_min")
        self.main_min_frame = QtWidgets.QFrame(self.page_main_min)
        self.main_min_frame.setGeometry(QtCore.QRect(490, 230, 481, 281))
        self.main_min_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_min_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_min_frame.setObjectName("main_min_frame")
        self.main_min_button_panel = QtWidgets.QFrame(self.main_min_frame)
        self.main_min_button_panel.setGeometry(QtCore.QRect(30, 60, 350, 111))
        self.main_min_button_panel.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                                 "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                 "border-radius: 13px;")
        self.main_min_button_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_min_button_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_min_button_panel.setObjectName("main_min_button_panel")
        self.character_s_min = QtWidgets.QLabel(self.main_min_button_panel)
        self.character_s_min.setEnabled(True)
        self.character_s_min.setGeometry(QtCore.QRect(240, 10, 92, 90))
        self.character_s_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;")
        self.character_s_min.setText("")
        self.character_s_min.setPixmap(QtGui.QPixmap("material/Neko/Neko_s.png"))
        self.character_s_min.setScaledContents(False)
        self.character_s_min.setObjectName("character_s_min")
        self.area_min_main = QtWidgets.QScrollArea(self.main_min_button_panel)
        self.area_min_main.setGeometry(QtCore.QRect(20, 20, 211, 71))
        self.area_min_main.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 13px;")
        self.area_min_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_min_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.area_min_main.setWidgetResizable(True)
        self.area_min_main.setObjectName("area_min_main")
        self.area_min_main_container = QtWidgets.QWidget()
        self.area_min_main_container.setGeometry(QtCore.QRect(0, 0, 211, 71))
        self.area_min_main_container.setStyleSheet("background: rgba(23, 23, 23, 0.0);")
        self.area_min_main_container.setObjectName("area_min_main_container")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.area_min_main_container)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_note_min = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.button_note_min.setEnabled(True)
        self.button_note_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;")
        self.button_note_min.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("material/image 50.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.button_note_min.setIcon(icon1)
        self.button_note_min.setIconSize(QtCore.QSize(50, 50))
        self.button_note_min.setAutoDefault(False)
        self.button_note_min.setDefault(False)
        self.button_note_min.setObjectName("button_note_min")
        self.gridLayout_3.addWidget(self.button_note_min, 0, 0, 1, 1)
        self.command_list_button_min = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.command_list_button_min.setEnabled(True)
        self.command_list_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                                   "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                   "border-radius: 13px;")
        self.command_list_button_min.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("material/image 41.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.command_list_button_min.setIcon(icon2)
        self.command_list_button_min.setIconSize(QtCore.QSize(50, 50))
        self.command_list_button_min.setAutoDefault(False)
        self.command_list_button_min.setDefault(False)
        self.command_list_button_min.setObjectName("command_list_button_min")
        self.gridLayout_3.addWidget(self.command_list_button_min, 0, 1, 1, 1)
        self.tag_button_min = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.tag_button_min.setEnabled(True)
        self.tag_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                          "border-radius: 13px;")
        self.tag_button_min.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material/image 42.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.tag_button_min.setIcon(icon)
        self.tag_button_min.setIconSize(QtCore.QSize(50, 50))
        self.tag_button_min.setAutoDefault(False)
        self.tag_button_min.setDefault(False)
        self.tag_button_min.setObjectName("tag_button_min")
        self.gridLayout_3.addWidget(self.tag_button_min, 0, 2, 1, 1)
        self.area_min_main.setWidget(self.area_min_main_container)
        self.wrap_button = QtWidgets.QPushButton(self.main_min_frame)
        self.wrap_button.setGeometry(QtCore.QRect(30, 180, 344, 41))
        self.wrap_button.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;\n"
                                       "font-size: 18px;\n"
                                       "line-height: 27px;\n"
                                       "\n"
                                       "color: #FFFFFF;")
        self.wrap_button.setObjectName("wrap_button")
        self.label_dialog_min_frame = QtWidgets.QLabel(self.main_min_frame)
        self.label_dialog_min_frame.setGeometry(QtCore.QRect(390, 70, 83, 73))
        self.label_dialog_min_frame.setStyleSheet("background: rgba(23, 23, 23, 0.9);\n"
                                                  "border: 1px solid #A7A7A7;\n"
                                                  "\n"
                                                  "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                  "border-radius: 13px;\n"
                                                  "font-family: Titillium Web;\n"
                                                  "font-style: normal;\n"
                                                  "font-weight: normal;\n"
                                                  "font-size: 12px;\n"
                                                  "line-height: 27px;\n"
                                                  "text-align: center;\n"
                                                  "padding: 0 0 0 13px;\n"
                                                  "color: #FFFFFF;")
        self.label_dialog_min_frame.setObjectName("label_dialog_min_frame")
        self.teg_list_frame_2 = QtWidgets.QFrame(self.page_main_min)
        self.teg_list_frame_2.setGeometry(QtCore.QRect(230, 280, 251, 161))
        self.teg_list_frame_2.setStyleSheet("background: rgba(23, 23, 23, 0.83);\n"
                                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                            "border-radius: 13px;")
        self.teg_list_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teg_list_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teg_list_frame_2.setObjectName("teg_list_frame_2")
        self.teg_area_2 = QtWidgets.QScrollArea(self.teg_list_frame_2)
        self.teg_area_2.setGeometry(QtCore.QRect(-20, -10, 281, 181))
        self.teg_area_2.setStyleSheet("background: rgba(23, 23, 23, 0);\n"
                                      "border-radius: 13px;")
        self.teg_area_2.setWidgetResizable(True)
        self.teg_area_2.setObjectName("teg_area_2")
        self.teg_area_container_3 = QtWidgets.QWidget()
        self.teg_area_container_3.setGeometry(QtCore.QRect(0, 0, 281, 181))
        self.teg_area_container_3.setObjectName("teg_area_container_3")
        self.setting_button_min = QtWidgets.QPushButton(self.teg_area_container_3)
        self.setting_button_min.setGeometry(QtCore.QRect(40, 30, 200, 32))
        self.setting_button_min.setStyleSheet("border-radius: 2px;\n"
                                              "font: 12pt \"MS Shell Dlg 2\";\n"
                                              "color: rgba(255, 255, 255, 0.67);\n"
                                              "\n"
                                              "background: rgba(23, 23, 23, 0.31);\n"
                                              "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                              "box-sizing: border-box;\n"
                                              "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.setting_button_min.setObjectName("setting_button_min")
        self.rule_button_min = QtWidgets.QPushButton(self.teg_area_container_3)
        self.rule_button_min.setGeometry(QtCore.QRect(40, 80, 200, 32))
        self.rule_button_min.setStyleSheet("border-radius: 2px;\n"
                                           "font: 12pt \"MS Shell Dlg 2\";\n"
                                           "color: rgba(255, 255, 255, 0.67);\n"
                                           "\n"
                                           "background: rgba(23, 23, 23, 0.31);\n"
                                           "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                           "box-sizing: border-box;\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.rule_button_min.setObjectName("rule_button_min")
        self.q_a_button_3 = QtWidgets.QPushButton(self.teg_area_container_3)
        self.q_a_button_3.setGeometry(QtCore.QRect(40, 130, 200, 32))
        self.q_a_button_3.setStyleSheet("border-radius: 2px;\n"
                                        "font: 12pt \"MS Shell Dlg 2\";\n"
                                        "color: rgba(255, 255, 255, 0.67);\n"
                                        "\n"
                                        "background: rgba(23, 23, 23, 0.31);\n"
                                        "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                        "box-sizing: border-box;\n"
                                        "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.q_a_button_3.setObjectName("q_a_button_3")
        self.teg_area_2.setWidget(self.teg_area_container_3)
        """add variable"""
        self.teg_list_frame_2.hide()
        self.tag_button_flag = False
        """button connect"""
        self.tag_button_min.clicked.connect(self.tag_button_switch_2)
        return self.page_main_min

    def tag_button_switch_2(self):
        if self.tag_button_flag:
            self.teg_list_frame_2.hide()
        else:
            self.teg_list_frame_2.show()
        self.tag_button_flag = not self.tag_button_flag
