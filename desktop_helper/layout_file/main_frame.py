import os
import subprocess
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
import desktop_helper.sqlite_Neko as sqlite_Neko

class Ui_MainFrame(object):
    def setup_Main_frame(self):
        self.page_main_frame = QtWidgets.QWidget()
        self.page_main_frame.setObjectName("page_main_frame")
        self.mainframe = QtWidgets.QFrame(self.page_main_frame)
        self.mainframe.setGeometry(QtCore.QRect(290, 80, 911, 571))
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.character_label = QtWidgets.QLabel(self.mainframe)
        self.character_label.setGeometry(QtCore.QRect(370, 210, 171, 241))
        self.character_label.setText("")
        self.character_label.setObjectName("character_label")
        self.dialog_character = QtWidgets.QLabel(self.mainframe)
        self.dialog_character.setGeometry(QtCore.QRect(50, 430, 451, 71))
        self.dialog_character.setStyleSheet("font-size: 18px;\n"
                                            "line-height: 40px;\n"
                                            "\n"
                                            "color: #FFFFFF;\n"
                                            "background: rgba(23, 23, 23, 0.85);\n"
                                            "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                            "border-radius: 13px;")
        self.dialog_character.setAlignment(QtCore.Qt.AlignCenter)
        self.dialog_character.setObjectName("dialog_character")
        self.teg_list_frame = QtWidgets.QFrame(self.mainframe)
        self.teg_list_frame.setGeometry(QtCore.QRect(50, 250, 251, 161))
        self.teg_list_frame.setStyleSheet("background: rgba(23, 23, 23, 0.83);\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                          "border-radius: 13px;")
        self.teg_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.teg_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.teg_list_frame.setObjectName("teg_list_frame")
        self.teg_area = QtWidgets.QScrollArea(self.teg_list_frame)
        self.teg_area.setGeometry(QtCore.QRect(-20, -10, 281, 181))
        self.teg_area.setStyleSheet("background: rgba(23, 23, 23, 0);\n"
                                    "border-radius: 13px;")
        self.teg_area.setWidgetResizable(True)
        self.teg_area.setObjectName("teg_area")
        self.teg_area_container = QtWidgets.QWidget()
        self.teg_area_container.setGeometry(QtCore.QRect(0, 0, 281, 181))
        self.teg_area_container.setObjectName("teg_area_container")
        self.setting_button = QtWidgets.QPushButton(self.teg_area_container)
        self.setting_button.setGeometry(QtCore.QRect(40, 30, 200, 32))
        self.setting_button.setStyleSheet("border-radius: 2px;\n"
                                          "font: 12pt \"MS Shell Dlg 2\";\n"
                                          "color: rgba(255, 255, 255, 0.67);\n"
                                          "\n"
                                          "background: rgba(23, 23, 23, 0.31);\n"
                                          "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                          "box-sizing: border-box;\n"
                                          "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.setting_button.setObjectName("setting_button")
        self.rule_button = QtWidgets.QPushButton(self.teg_area_container)
        self.rule_button.setGeometry(QtCore.QRect(40, 80, 200, 32))
        self.rule_button.setStyleSheet("border-radius: 2px;\n"
                                       "font: 12pt \"MS Shell Dlg 2\";\n"
                                       "color: rgba(255, 255, 255, 0.67);\n"
                                       "\n"
                                       "background: rgba(23, 23, 23, 0.31);\n"
                                       "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                       "box-sizing: border-box;\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.rule_button.setObjectName("rule_button")
        self.q_a_button = QtWidgets.QPushButton(self.teg_area_container)
        self.q_a_button.setGeometry(QtCore.QRect(40, 130, 200, 32))
        self.q_a_button.setStyleSheet("border-radius: 2px;\n"
                                      "font: 12pt \"MS Shell Dlg 2\";\n"
                                      "color: rgba(255, 255, 255, 0.67);\n"
                                      "\n"
                                      "background: rgba(23, 23, 23, 0.31);\n"
                                      "border: 1px solid rgba(233, 233, 233, 0.22);\n"
                                      "box-sizing: border-box;\n"
                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);")
        self.q_a_button.setObjectName("q_a_button")
        self.teg_area.setWidget(self.teg_area_container)
        self.frame_icon_other_frame = QtWidgets.QFrame(self.mainframe)
        self.frame_icon_other_frame.setGeometry(QtCore.QRect(550, 180, 81, 291))
        self.frame_icon_other_frame.setStyleSheet("background: rgba(23, 23, 23, 0.83);\n"
                                                  "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                                  "border-radius: 13px;")
        self.frame_icon_other_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_other_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_other_frame.setObjectName("frame_icon_other_frame")
        self.icon_buttons_area = QtWidgets.QScrollArea(self.frame_icon_other_frame)
        self.icon_buttons_area.setGeometry(QtCore.QRect(12, 24, 60, 281))
        self.icon_buttons_area.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "")
        self.icon_buttons_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.icon_buttons_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.icon_buttons_area.setWidgetResizable(True)
        self.icon_buttons_area.setObjectName("icon_buttons_area")
        self.icon_buttons_area_container = QtWidgets.QWidget()
        self.icon_buttons_area_container.setGeometry(QtCore.QRect(0, 0, 60, 281))
        self.icon_buttons_area_container.setObjectName("icon_buttons_area_container")

        self.Flowlayout_for_button = FlowLayout(self.icon_buttons_area_container)
        self.Flowlayout_for_button.setObjectName("Flowlayout_for_button")
        self.icon_buttons_area.setWidget(self.icon_buttons_area_container)
        """add variable"""
        self.teg_list_frame.hide()


        """button connect"""

        self.append_icon_button()
        "like frame"
        self.command_panel_frame = QtWidgets.QFrame(self.mainframe)
        self.command_panel_frame.setGeometry(QtCore.QRect(690, 60, 171, 491))
        self.command_panel_frame.setGeometry(QtCore.QRect(690, 60, 161, 491))
        self.command_panel_frame.setStyleSheet("background: rgba(23, 23, 23, 0.83);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;")
        self.command_panel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.command_panel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.command_panel_frame.setObjectName("command_panel_frame")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.command_panel_frame)
        self.scrollArea_9.setGeometry(QtCore.QRect(10, 16, 151, 461))
        self.scrollArea_9.setGeometry(QtCore.QRect(0, 16, 171, 461))
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 151, 461))
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 161, 461))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_9)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_9.setAlignment(QtCore.Qt.AlignLeft)
        self.gridLayout_9.setAlignment(QtCore.Qt.AlignTop)
        self.scrollArea_9.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.command_panel_frame.hide()
        self.command_panel_frame_button_update()
        return self.page_main_frame

    def command_panel_frame_button_update(self):
        """обновляет кнопки, содержащие команды для выполнения"""
        conn = sqlite_Neko.create_connection("Neko.db")
        with conn:
            name = sqlite_Neko.select_all_command(conn)
            print(name)
        for i, j in enumerate(name):
            self.scrollArea_9.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
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
                        os.system(f"start {i}")
                        subprocess.call(('cmd', '/c', 'start', '', i))
                    elif os.path.exists(i) is False:
                        pass
                        # if i == "":
                        #     pass
                        # else:
                        #     self.del_list.append(button_name)
                        #     self.del_command()
                        #     self.clear_note(self.gridLayout_9)
                        #     self.command_panel_frame_button_update()

    def append_icon_button(self):
        self.tag_button = IconButton("material/teg_icon.png")
        self.tag_button.clicked.connect(  lambda: self.teg_list_frame.show() if self.teg_list_frame.isHidden() else self.teg_list_frame.hide())
        self.command_list_button = IconButton("material/like.png")
        self.command_list_button.clicked.connect(
            lambda: self.command_panel_frame.show() if self.command_panel_frame.isHidden() else self.command_panel_frame.hide())
        self.move_to_adding_section = IconButton("material/add_command.png")
        # self.info_button = IconButton("material/info.png")
        # self.setting_button_icon = IconButton("material/setting_icon.png")
        self.setting_voice = IconButton("material/voice_setting.png")
        self.Flowlayout_for_button.addWidget(self.tag_button)
        self.Flowlayout_for_button.addWidget(self.command_list_button)
        self.Flowlayout_for_button.addWidget(self.move_to_adding_section)
        self.Flowlayout_for_button.addWidget(self.setting_voice)
        # self.Flowlayout_for_button.addWidget(self.setting_button_icon)
        # self.Flowlayout_for_button.addWidget(self.info_button)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.MiddleButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()
class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, hspacing=0, vspacing=10):
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

class IconButton(QtWidgets.QPushButton):
    def __init__(self,icon_path):
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
