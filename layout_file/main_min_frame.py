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
        self.character_s_min.setScaledContents(True)
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
        self.button_note_min = QtWidgets.QPushButton(self.area_min_main_container)
        self.button_note_min.setEnabled(True)
        self.button_note_min.setMinimumSize(QtCore.QSize(50, 50))
        self.button_note_min.setMaximumSize(QtCore.QSize(50, 50))
        self.button_note_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                           "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                           "border-radius: 13px;")
        self.button_note_min.setText("")
        # self.button_note_min.setIcon(icon1)
        self.button_note_min.setIconSize(QtCore.QSize(50, 50))
        self.button_note_min.setAutoDefault(False)
        self.button_note_min.setDefault(False)
        self.button_note_min.setObjectName("button_note_min")
        self.gridLayout_3.addWidget(self.button_note_min, 1, 0, 1, 1)
        self.like_command_button_min = QtWidgets.QPushButton(self.area_min_main_container)
        self.like_command_button_min.setEnabled(True)
        self.like_command_button_min.setMinimumSize(QtCore.QSize(50, 50))
        self.like_command_button_min.setMaximumSize(QtCore.QSize(50, 50))
        self.like_command_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                                   "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                   "border-radius: 13px;")
        self.like_command_button_min.setText("")
        # self.like_command_button_min.setIcon(icon2)
        self.like_command_button_min.setIconSize(QtCore.QSize(50, 50))
        self.like_command_button_min.setAutoDefault(False)
        self.like_command_button_min.setDefault(False)
        self.like_command_button_min.setObjectName("like_command_button_min")
        self.gridLayout_3.addWidget(self.like_command_button_min, 1, 1, 1, 1)
        self.teg_button_min = QtWidgets.QPushButton(self.area_min_main_container)
        self.teg_button_min.setEnabled(True)
        self.teg_button_min.setMinimumSize(QtCore.QSize(50, 50))
        self.teg_button_min.setMaximumSize(QtCore.QSize(50, 50))
        self.teg_button_min.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                          "border-radius: 13px;")
        self.teg_button_min.setText("")
        # self.teg_button_min.setIcon(icon)
        self.teg_button_min.setIconSize(QtCore.QSize(50, 50))
        self.teg_button_min.setAutoDefault(False)
        self.teg_button_min.setDefault(False)
        self.teg_button_min.setObjectName("teg_button_min")
        self.gridLayout_3.addWidget(self.teg_button_min, 1, 2, 1, 1)
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
        self.label_dialog_min_frame.setStyleSheet("background: #2B2525;\n"
                                                  "border: 2px solid #A7A7A7;\n"
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
        return self.page_main_min