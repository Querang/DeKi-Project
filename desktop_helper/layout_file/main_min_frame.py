import os
import subprocess
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
import desktop_helper.sqlite_Neko as sqlite_Neko

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
        self.area_min_main.setGeometry(QtCore.QRect(20, 30, 211, 71))
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
        self.Flowlayout_for_button_1 = FlowLayout(self.area_min_main_container)

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
                                                  "padding: 0 0 0 10px;\n"
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
        self.append_icon_button_1()
        """button connect"""
        
        "like frame"
        self.command_panel_frame_1_1 = QtWidgets.QFrame(self.page_main_min)
        self.command_panel_frame_1_1.setGeometry(QtCore.QRect(880, 60, 171, 491))
        self.command_panel_frame_1_1.setStyleSheet("background: rgba(23, 23, 23, 0.83);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;")
        self.command_panel_frame_1_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.command_panel_frame_1_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.command_panel_frame_1_1.setObjectName("command_panel_frame_1")
        self.scrollArea_9_min = QtWidgets.QScrollArea(self.command_panel_frame_1_1)
        self.scrollArea_9_min.setGeometry(QtCore.QRect(10, 16, 151, 461))
        self.scrollArea_9_min.setGeometry(QtCore.QRect(0, 16, 171, 461))
        self.scrollArea_9_min.setWidgetResizable(True)
        self.scrollArea_9_min.setObjectName("scrollArea_9_min")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 151, 461))
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 161, 461))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_9_min = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_9_min.setObjectName("gridLayout_9_min")
        self.scrollArea_9_min.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_9_min.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout_9_min.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_9_min.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.command_panel_frame_1_1.hide()
        self.command_panel_frame_1_button_update()
        return self.page_main_min
    def clear_note(self, gridLayout):
        """
           Clears the resulting layout from elements
           param gridLayout_note: layout для очистки от элементов
           """
        while gridLayout.count():
            item = gridLayout.takeAt(0)
            widget = item.widget()
            widget.deleteLater()
    def command_panel_frame_1_button_update(self):
        self.clear_note(self.gridLayout_9_min)
        """обновляет кнопки, содержащие команды для выполнения"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i, j in enumerate(name):
            self.scrollArea_9_min.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
            self.pushButton = QtWidgets.QPushButton()
            self.pushButton.setGeometry(QtCore.QRect(11, 11, 129, 429))
            self.pushButton.setMinimumSize(125, 52)
            self.pushButton.setMaximumSize(125, 52)
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
            self.gridLayout_9_min.addWidget(self.pushButton, i, 0)

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
                webbrowser.open_new_tab(str(sql_command_site[index]))
            elif command_type == 'f':
                for i in sql_command_files[index]:
                    print(sql_command_files[index])
                    if os.path.exists(i) is True:
                        subprocess.call(('cmd', '/c', 'start', '', i))
                    elif os.path.exists(i) is False:
                        pass
                        # if i == "":
                        #     pass
                        # else:
                        #     self.del_list.append(button_name)
                        #     self.del_command()
                        #     self.clear_note(self.gridLayout_9_min)
                        #     self.command_panel_frame_1_button_update()

    def append_icon_button_1(self):
        self.tag_button_min = IconButton("material/teg_icon.png")
        self.tag_button_min.clicked.connect(
            lambda: self.teg_list_frame_2.show() if self.teg_list_frame_2.isHidden() else self.teg_list_frame_2.hide())
        self.command_list_button_min = IconButton("material/like.png")
        self.command_list_button_min.clicked.connect(
            lambda: self.command_panel_frame_1_1.show() if self.command_panel_frame_1_1.isHidden() else self.command_panel_frame_1_1.hide())
        self.move_to_adding_section_min = IconButton("material/add_command.png")
        # self.info_button = IconButton("material/info.png")
        # self.setting_button_icon = IconButton("material/setting_icon.png")
        self.setting_voice_min = IconButton("material/voice_setting.png")
        self.Flowlayout_for_button_1.addWidget(self.tag_button_min)
        self.Flowlayout_for_button_1.addWidget(self.command_list_button_min)
        self.Flowlayout_for_button_1.addWidget(self.move_to_adding_section_min)
        self.Flowlayout_for_button_1.addWidget(self.setting_voice_min)




class IconButton(QtWidgets.QPushButton):
    def __init__(self, icon_path):
        super(IconButton, self).__init__()
        self.setMinimumSize(QtCore.QSize(56, 52))
        self.setMaximumSize(QtCore.QSize(56, 52))
        self.setGeometry(QtCore.QRect(0, 0, 56, 52))
        self.setEnabled(True)
        self.setStyleSheet(" QPushButton {"
                           "background: rgba(149, 149, 149, 0.0);\n"


                           "color: rgba(255, 255, 255, 0.7);}\n"
                           "QPushButton:hover {\n"
                           "background: rgba(255, 255, 255, 0.05);}")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(56, 52))
class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, hspacing=15, vspacing=15):
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