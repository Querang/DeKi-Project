from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.icon_buttons_area.setGeometry(QtCore.QRect(4, 9, 72, 281))
        self.icon_buttons_area.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                             "")
        self.icon_buttons_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.icon_buttons_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.icon_buttons_area.setWidgetResizable(True)
        self.icon_buttons_area.setObjectName("icon_buttons_area")
        self.icon_buttons_area_container = QtWidgets.QWidget()
        self.icon_buttons_area_container.setGeometry(QtCore.QRect(0, 0, 72, 281))
        self.icon_buttons_area_container.setObjectName("icon_buttons_area_container")
        self.gridLayout = QtWidgets.QGridLayout(self.icon_buttons_area_container)
        self.gridLayout.setObjectName("gridLayout")
        self.tag_button = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.tag_button.setEnabled(True)
        self.tag_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                      "border-radius: 13px;")
        self.tag_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material/image 42.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.tag_button.setIcon(icon)
        self.tag_button.setIconSize(QtCore.QSize(50, 50))
        self.tag_button.setAutoDefault(False)
        self.tag_button.setDefault(False)
        self.tag_button.setObjectName("tag_button")
        self.gridLayout.addWidget(self.tag_button, 3, 0, 1, 1)
        self.button_note = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.button_note.setEnabled(True)
        self.button_note.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                       "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                       "border-radius: 13px;")
        self.button_note.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("material/image 50.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.button_note.setIcon(icon1)
        self.button_note.setIconSize(QtCore.QSize(50, 50))
        self.button_note.setAutoDefault(False)
        self.button_note.setDefault(False)
        self.button_note.setObjectName("button_note")
        self.gridLayout.addWidget(self.button_note, 0, 0, 1, 1)
        self.command_list_button = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.command_list_button.setEnabled(True)
        self.command_list_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                               "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                               "border-radius: 13px;")
        self.command_list_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("material/image 41.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.command_list_button.setIcon(icon2)
        self.command_list_button.setIconSize(QtCore.QSize(50, 50))
        self.command_list_button.setAutoDefault(False)
        self.command_list_button.setDefault(False)
        self.command_list_button.setObjectName("command_list_button")
        self.gridLayout.addWidget(self.command_list_button, 1, 0, 1, 1)
        self.remain_button = QtWidgets.QPushButton(self.icon_buttons_area_container)
        self.remain_button.setEnabled(True)
        self.remain_button.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                         "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                         "border-radius: 13px;")
        self.remain_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("material/image 63.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.remain_button.setIcon(icon3)
        self.remain_button.setIconSize(QtCore.QSize(50, 50))
        self.remain_button.setAutoDefault(False)
        self.remain_button.setDefault(False)
        self.remain_button.setObjectName("remain_button")
        self.gridLayout.addWidget(self.remain_button, 2, 0, 1, 1)
        self.icon_buttons_area.setWidget(self.icon_buttons_area_container)
        """add variable"""
        self.teg_list_frame.hide()
        self.tag_button_flag = False
        """button connect"""


        return self.page_main_frame

    def append_icon_button(self):
        pass

class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=20, hspacing=15, vspacing=20):
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
    def __init__(self):
        super(IconButton, self).__init__()
        self.setEnabled(True)
        self.setStyleSheet("background: rgba(23, 23, 23, 0.0);\n"
                                      "box-shadow: 2px 4px 4px rgba(0, 0, 0, 0.25);\n"
                                      "border-radius: 13px;")
        self.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("material/image 42.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(50, 50))