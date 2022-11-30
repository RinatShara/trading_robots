import os

from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

icons_way = os.getcwd()


class Ui_TestingWindow(object):
    def setupUi(self, TestingWindow):
        TestingWindow.setObjectName("TestingWindow")
        TestingWindow.setFixedSize(763, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TestingWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TestingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg2_label = QtWidgets.QLabel(self.centralwidget)
        self.bg2_label.setGeometry(QtCore.QRect(-10, 0, 781, 611))
        self.bg2_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.994318, y2:0, "
            "stop:0.375 rgba(119, 67, 219, 255), stop:0.426136 rgba(119, 105, 219, 255));")
        self.bg2_label.setText("")
        self.bg2_label.setIndent(2)
        self.bg2_label.setObjectName("bg2_label")
        self.first_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.first_calendar.setMinimumDate(QDate(2020, 1, 1))
        self.first_calendar.setMaximumDate(QDate(datetime.now()))
        self.first_calendar.setEnabled(True)
        self.first_calendar.setGeometry(QtCore.QRect(421, 288, 241, 170))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.first_calendar.setFont(font)
        self.first_calendar.setAutoFillBackground(True)
        self.first_calendar.setStyleSheet("#qt_calendar_navigationbar {\n"
                                          "    font-size: 15px;\n"
                                          "    font-weight: 700;\n"
                                          "    background-color: #8D9EFF;\n"
                                          "    min-height: 30px;\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
                                          "    qproperty-icon: none;\n"
                                          "    color: white;\n"
                                          "    font-weight: 700;\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_prevmonth {\n"
                                          "    qproperty-text: \"<\";\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_nextmonth {\n"
                                          "    qproperty-text: \">\";\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
                                          "    background-color: rgba(141, 119, 255, 150);\n"
                                          "    border: none;\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
                                          "    width: 90px;\n"
                                          "    margin-right: 10px;\n"
                                          "    color: white;\n"
                                          "    border-radius: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
                                          "    background-color: rgba(141, 119, 255, 150);\n"
                                          "}\n"
                                          "\n"
                                          "#qt_calendar_calendarview {\n"
                                          "    outline: 2px solid rgb(0, 188, 212);\n"
                                          "    selection-color: #3C00FF;\n"
                                          "    selection-background-color: transparent;\n"
                                          "}\n"
                                          "")
        self.first_calendar.setGridVisible(False)
        self.first_calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.first_calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.first_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.first_calendar.setNavigationBarVisible(True)
        self.first_calendar.setDateEditEnabled(True)
        self.first_calendar.setObjectName("first_calendar")
        self.choose_strat = QtWidgets.QComboBox(self.centralwidget)
        self.choose_strat.setGeometry(QtCore.QRect(420, 103, 241, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_strat.sizePolicy().hasHeightForWidth())
        self.choose_strat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.choose_strat.setFont(font)
        self.choose_strat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_strat.setStyleSheet("QComboBox{\n"
                                        "    padding-left: 10px;\n"
                                        "    color: white;\n"
                                        "    background-color: #5DA7DB;\n"
                                        "    border-radius: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox:hover{\n"
                                        "    background-color: #81C6E8;\n"
                                        "}\n"
                                        "\n"
                                        "QComboBox QAbstractItemView {\n"
                                        "    outline: none;\n"
                                        "    background-color: #4691E2;\n"
                                        "    selection-background-color: #7DE5ED;\n"
                                        "    color: white;\n"
                                        "    padding: 10px;\n"
                                        "    padding-left: 5px;\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.choose_strat.setEditable(False)
        self.choose_strat.setObjectName("choose_strat")
        self.choose_strat.addItem("")
        self.choose_strat.addItem("")
        self.choose_strat.addItem("")
        self.choose_strat.addItem("")
        self.choose_strat_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_strat_label.setGeometry(QtCore.QRect(440, 63, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.choose_strat_label.setFont(font)
        self.choose_strat_label.setStyleSheet("color: white;")
        self.choose_strat_label.setObjectName("choose_strat_label")
        self.first_date_btn = QtWidgets.QPushButton(self.centralwidget)
        self.first_date_btn.setEnabled(True)
        self.first_date_btn.setGeometry(QtCore.QRect(340, 234, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.first_date_btn.setFont(font)
        self.first_date_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.first_date_btn.setToolTipDuration(-3)
        self.first_date_btn.setAutoFillBackground(False)
        self.first_date_btn.setStyleSheet("QPushButton{\n"
                                          "    background-color: #5DA7DB;\n"
                                          "    color: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          ":hover{\n"
                                          "    background-color: #81C6E8;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.first_date_btn.setCheckable(False)
        self.first_date_btn.setObjectName("first_date_btn")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(339, 20, 230, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.error_label.setFont(font)
        self.error_label.setToolTipDuration(-2)
        self.error_label.setStyleSheet("QLabel{\n"
                                       "    color: white;\n"
                                       "    border: 3px solid #FF1E6D;\n"
                                       "    border-radius: 8px;\n"
                                       "}")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.choose_share = QtWidgets.QLineEdit(self.centralwidget)
        self.choose_share.setGeometry(QtCore.QRect(430, 168, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.choose_share.setFont(font)
        self.choose_share.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.choose_share.setStyleSheet("QLineEdit{\n"
                                        "    padding-left: 7px;\n"
                                        "    background-color: #5DA7DB;\n"
                                        "    color: white;\n"
                                        "    border-radius: 10px;\n"
                                        "}\n"
                                        "\n"
                                        ":hover, :focus{\n"
                                        "    background-color: #81C6E8;\n"
                                        "}")
        self.choose_share.setObjectName("choose_share")
        self.second_date_btn = QtWidgets.QPushButton(self.centralwidget)
        self.second_date_btn.setEnabled(True)
        self.second_date_btn.setGeometry(QtCore.QRect(550, 234, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.second_date_btn.setFont(font)
        self.second_date_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.second_date_btn.setToolTipDuration(-3)
        self.second_date_btn.setAutoFillBackground(False)
        self.second_date_btn.setStyleSheet("QPushButton{\n"
                                           "    background-color: #5DA7DB;\n"
                                           "    color: white;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           ":hover{\n"
                                           "    background-color: #81C6E8;\n"
                                           "}\n"
                                           "\n"
                                           "\n"
                                           "")
        self.second_date_btn.setCheckable(False)
        self.second_date_btn.setObjectName("second_date_btn")
        self.set_param_btn = QtWidgets.QPushButton(self.centralwidget)
        self.set_param_btn.setEnabled(True)
        self.set_param_btn.setGeometry(QtCore.QRect(403, 300, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.set_param_btn.setFont(font)
        self.set_param_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_param_btn.setToolTipDuration(-3)
        self.set_param_btn.setAutoFillBackground(False)
        self.set_param_btn.setStyleSheet("QPushButton{\n"
                                         "    background-color: #5DA7DB;\n"
                                         "    color: white;\n"
                                         "    border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         ":hover{\n"
                                         "    background-color: #81C6E8;\n"
                                         "}\n"
                                         "\n"
                                         ":disabled{\n"
                                         "    color: rgba(255, 255, 255, 100);\n"
                                         "    background-color: #5837D0;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.set_param_btn.setCheckable(False)
        self.set_param_btn.setObjectName("set_param_btn")
        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setEnabled(True)
        self.reset_btn.setGeometry(QtCore.QRect(360, 397, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.reset_btn.setFont(font)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_btn.setAutoFillBackground(False)
        self.reset_btn.setStyleSheet("QPushButton{\n"
                                     "    background-color: #6C4AB6;\n"
                                     "    color: white;\n"
                                     "    border-radius: 10px;\n"
                                     "}\n"
                                     "\n"
                                     ":hover{\n"
                                     "    background-color: #FF1E6D;\n"
                                     "}\n"
                                     "\n"
                                     ":disabled{\n"
                                     "    color: rgba(255, 255, 255, 100);\n"
                                     "    background-color: #67207D;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.reset_btn.setCheckable(False)
        self.reset_btn.setObjectName("reset_btn")
        self.hist_tests_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hist_tests_btn.setEnabled(True)
        self.hist_tests_btn.setGeometry(QtCore.QRect(590, 20, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.hist_tests_btn.setFont(font)
        self.hist_tests_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hist_tests_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.hist_tests_btn.setAutoFillBackground(False)
        self.hist_tests_btn.setStyleSheet("QPushButton{\n"
                                          "    background-color: #6C4AB6;\n"
                                          "    color: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          ":hover{\n"
                                          "    background-color: #8D9EFF;\n"
                                          "}\n"
                                          "\n"
                                          ":disabled{\n"
                                          "    color: rgba(255, 255, 255, 100);\n"
                                          "    background-color: #6C27B6;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.hist_tests_btn.setCheckable(False)
        self.hist_tests_btn.setObjectName("hist_tests_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setEnabled(True)
        self.start_btn.setGeometry(QtCore.QRect(510, 397, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.start_btn.setFont(font)
        self.start_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn.setToolTipDuration(-3)
        self.start_btn.setAutoFillBackground(False)
        self.start_btn.setStyleSheet("QPushButton{\n"
                                     "    background-color: #6C4AB6;\n"
                                     "    color: white;\n"
                                     "    border-radius: 10px;\n"
                                     "}\n"
                                     "\n"
                                     ":hover{\n"
                                     "    background-color: #00FFAE;\n"
                                     "}\n"
                                     "\n"
                                     ":disabled{\n"
                                     "    color: rgba(255, 255, 255, 100);\n"
                                     "    background-color: #67207D;\n"
                                     "}\n"
                                     "\n"
                                     "")
        self.start_btn.setCheckable(False)
        self.start_btn.setObjectName("start_btn")
        self.dollar_price = QtWidgets.QLabel(self.centralwidget)
        self.dollar_price.setGeometry(QtCore.QRect(80, 78, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.dollar_price.setFont(font)
        self.dollar_price.setStyleSheet("color: white;")
        self.dollar_price.setObjectName("dollar_price")
        self.euro_icon = QtWidgets.QLabel(self.centralwidget)
        self.euro_icon.setGeometry(QtCore.QRect(160, 78, 31, 41))
        self.euro_icon.setText("")
        self.euro_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/"
                                               f"Icons/euro_icon.png"))
        self.euro_icon.setObjectName("euro_icon")
        self.sand_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sand_btn.setEnabled(False)
        self.sand_btn.setGeometry(QtCore.QRect(10, 308, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.sand_btn.setFont(font)
        self.sand_btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: #8D72E1;\n"
                                    "    color: white;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    ":hover{\n"
                                    "    background-color: #8D9EFF;\n"
                                    "}\n"
                                    "\n"
                                    ":disabled{\n"
                                    "    color: rgba(255, 255, 255, 100);\n"
                                    "    background-color: #6C27B6;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.sand_btn.setObjectName("sand_btn")
        self.clock_icon = QtWidgets.QLabel(self.centralwidget)
        self.clock_icon.setGeometry(QtCore.QRect(50, 28, 31, 41))
        self.clock_icon.setText("")
        self.clock_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/"
                                                f"Icons/clock_icon.png"))
        self.clock_icon.setObjectName("clock_icon")
        self.calen_icon = QtWidgets.QLabel(self.centralwidget)
        self.calen_icon.setGeometry(QtCore.QRect(160, 28, 31, 41))
        self.calen_icon.setText("")
        self.calen_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/"
                                                f"Icons/calen_icon.png"))
        self.calen_icon.setObjectName("calen_icon")
        self.current_date = QtWidgets.QLabel(self.centralwidget)
        self.current_date.setGeometry(QtCore.QRect(190, 28, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.current_date.setFont(font)
        self.current_date.setStyleSheet("color: white;")
        self.current_date.setObjectName("current_date")
        self.test_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_btn.setEnabled(True)
        self.test_btn.setGeometry(QtCore.QRect(10, 228, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.test_btn.setFont(font)
        self.test_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.test_btn.setAutoFillBackground(False)
        self.test_btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: #8D72E1;\n"
                                    "    color: white;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    ":hover{\n"
                                    "    background-color: #8D9EFF;\n"
                                    "}\n"
                                    "\n"
                                    ":disabled{\n"
                                    "    color: rgba(255, 255, 255, 100);\n"
                                    "    background-color: #67207D;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.test_btn.setCheckable(False)
        self.test_btn.setObjectName("test_btn")
        self.euro_price = QtWidgets.QLabel(self.centralwidget)
        self.euro_price.setGeometry(QtCore.QRect(190, 78, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.euro_price.setFont(font)
        self.euro_price.setStyleSheet("color: white;")
        self.euro_price.setObjectName("euro_price")
        self.real_btn = QtWidgets.QPushButton(self.centralwidget)
        self.real_btn.setEnabled(False)
        self.real_btn.setGeometry(QtCore.QRect(10, 388, 291, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.real_btn.setFont(font)
        self.real_btn.setStyleSheet("QPushButton{\n"
                                    "    background-color: #8D72E1;\n"
                                    "    color: white;\n"
                                    "    border-radius: 10px;\n"
                                    "}\n"
                                    "\n"
                                    ":hover{\n"
                                    "    background-color: #8D9EFF;\n"
                                    "}\n"
                                    "\n"
                                    ":disabled{\n"
                                    "    color: rgba(255, 255, 255, 100);\n"
                                    "    background-color: #6C27B6;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.real_btn.setObjectName("real_btn")
        self.current_time = QtWidgets.QLabel(self.centralwidget)
        self.current_time.setGeometry(QtCore.QRect(80, 28, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.current_time.setFont(font)
        self.current_time.setStyleSheet("color: white;")
        self.current_time.setObjectName("current_time")
        self.dollar_icon = QtWidgets.QLabel(self.centralwidget)
        self.dollar_icon.setGeometry(QtCore.QRect(50, 78, 31, 41))
        self.dollar_icon.setText("")
        self.dollar_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/"
                                                 f"Icons/dollar_icon.png"))
        self.dollar_icon.setObjectName("dollar_icon")
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(30, 161, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.choose_label.setFont(font)
        self.choose_label.setStyleSheet("color: white;")
        self.choose_label.setObjectName("choose_label")
        self.second_calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.second_calendar.setEnabled(True)
        self.second_calendar.setGeometry(QtCore.QRect(421, 288, 241, 170))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.second_calendar.setFont(font)
        self.second_calendar.setAutoFillBackground(True)
        self.second_calendar.setStyleSheet("#qt_calendar_navigationbar {\n"
                                           "    font-size: 15px;\n"
                                           "    font-weight: 700;\n"
                                           "    background-color: #8D9EFF;\n"
                                           "    min-height: 30px;\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_prevmonth, #qt_calendar_nextmonth {\n"
                                           "    qproperty-icon: none;\n"
                                           "    color: white;\n"
                                           "    font-weight: 700;\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_prevmonth {\n"
                                           "    qproperty-text: \"<\";\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_nextmonth {\n"
                                           "    qproperty-text: \">\";\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
                                           "    background-color: rgba(141, 119, 255, 150);\n"
                                           "    border: none;\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
                                           "    width: 90px;\n"
                                           "    margin-right: 10px;\n"
                                           "    color: white;\n"
                                           "    border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
                                           "    background-color: rgba(141, 119, 255, 150);\n"
                                           "}\n"
                                           "\n"
                                           "#qt_calendar_calendarview {\n"
                                           "    outline: 2px solid rgb(0, 188, 212);\n"
                                           "    selection-color: #3C00FF;\n"
                                           "    selection-background-color: transparent;\n"
                                           "}\n"
                                           "")
        self.second_calendar.setGridVisible(False)
        self.second_calendar.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.second_calendar.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.second_calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.second_calendar.setNavigationBarVisible(True)
        self.second_calendar.setDateEditEnabled(True)
        self.second_calendar.setMinimumDate(QDate(2020, 1, 1))
        self.second_calendar.setMaximumDate(QDate(datetime.now()))
        self.second_calendar.setObjectName("second_calendar")
        self.bg2_label.raise_()
        self.reset_btn.raise_()
        self.set_param_btn.raise_()
        self.choose_strat.raise_()
        self.choose_strat_label.raise_()
        self.first_date_btn.raise_()
        self.error_label.raise_()
        self.choose_share.raise_()
        self.second_date_btn.raise_()
        self.hist_tests_btn.raise_()
        self.start_btn.raise_()
        self.dollar_price.raise_()
        self.euro_icon.raise_()
        self.sand_btn.raise_()
        self.clock_icon.raise_()
        self.calen_icon.raise_()
        self.current_date.raise_()
        self.test_btn.raise_()
        self.euro_price.raise_()
        self.real_btn.raise_()
        self.current_time.raise_()
        self.dollar_icon.raise_()
        self.choose_label.raise_()
        self.second_calendar.raise_()
        self.first_calendar.raise_()
        TestingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestingWindow)
        QtCore.QMetaObject.connectSlotsByName(TestingWindow)

    def retranslateUi(self, TestingWindow):
        time = datetime.now()
        _translate = QtCore.QCoreApplication.translate
        TestingWindow.setWindowTitle(_translate("TestingWindow", "Cash Counter"))
        self.choose_strat.setItemText(0, _translate("TestingWindow", "MACD + SuperTrend + EMA"))
        self.choose_strat.setItemText(1, _translate("TestingWindow", "Releasing"))
        self.choose_strat.setItemText(2, _translate("TestingWindow", "Releasing"))
        self.choose_strat.setItemText(3, _translate("TestingWindow", "Releasing"))
        self.choose_strat_label.setText(_translate("TestingWindow", "Выберите стратегию"))
        self.first_date_btn.setToolTip(_translate("TestingWindow", "Изменить дату"))
        self.first_date_btn.setText(_translate("TestingWindow", "Задать начальную дату"))
        self.error_label.setToolTip(_translate("TestingWindow", "Ошибка"))
        self.error_label.setText(_translate("TestingWindow", "Ошибка"))
        self.choose_share.setPlaceholderText(_translate("TestingWindow", "Введите название акции"))
        self.second_date_btn.setToolTip(_translate("TestingWindow", "Изменить дату"))
        self.second_date_btn.setText(_translate("TestingWindow", "Задать конечную дату"))
        self.set_param_btn.setToolTip(
            _translate("TestingWindow", "<html><head/><body><p>Задать дополнительные параметры</p></body></html>"))
        self.set_param_btn.setText(_translate("TestingWindow", "Задать параметры стратегии"))
        self.reset_btn.setText(_translate("TestingWindow", "Сбросить"))
        self.hist_tests_btn.setToolTip(
            _translate("TestingWindow", "<html><head/><body><p>Исторические тесты</p></body></html>"))
        self.hist_tests_btn.setText(_translate("TestingWindow", "История"))
        self.start_btn.setText(_translate("TestingWindow", "Начать тестирование"))
        self.dollar_price.setText(_translate("TestingWindow", "60.26"))
        self.sand_btn.setText(_translate("TestingWindow", "Торговля в \"песочнице\""))
        self.current_date.setText(_translate("TestingWindow", "23.11.2022"))
        self.test_btn.setText(_translate("TestingWindow", "Тестирование стратегий"))
        self.euro_price.setText(_translate("TestingWindow", "70.51"))
        self.real_btn.setText(_translate("TestingWindow", "Торговля на реальном рынке"))
        self.current_time.setText(_translate("TestingWindow", f"{time.hour}:{str(time.minute).rjust(2, '0')}"))
        self.choose_label.setText(_translate("TestingWindow", "Выберите режим запуска "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TestingWindow = QtWidgets.QMainWindow()
    ui = Ui_TestingWindow()
    ui.setupUi(TestingWindow)
    TestingWindow.show()
    sys.exit(app.exec_())
