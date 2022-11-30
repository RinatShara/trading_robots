import os

from PyQt5 import QtCore, QtGui, QtWidgets

icons_way = os.getcwd()


class Ui_CertainResultWindow(object):
    def setupUi(self, CertainResultWindow):
        CertainResultWindow.setObjectName("CertainResultWindow")
        CertainResultWindow.setFixedSize(892, 571)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CertainResultWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CertainResultWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg4_label = QtWidgets.QLabel(self.centralwidget)
        self.bg4_label.setGeometry(QtCore.QRect(-30, -12, 931, 611))
        self.bg4_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0.539773 rgba(119, 67, 219, 255), stop:0.596591 rgba(119, 105, 219, 255));")
        self.bg4_label.setText("")
        self.bg4_label.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/long_icon.png"))
        self.bg4_label.setIndent(2)
        self.bg4_label.setObjectName("bg4_label")
        self.long_icon = QtWidgets.QLabel(self.centralwidget)
        self.long_icon.setGeometry(QtCore.QRect(93, 250, 31, 31))
        self.long_icon.setText("")
        self.long_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/long_icon.png"))
        self.long_icon.setObjectName("long_icon")
        self.profit_icon = QtWidgets.QLabel(self.centralwidget)
        self.profit_icon.setGeometry(QtCore.QRect(93, 447, 31, 31))
        self.profit_icon.setText("")
        self.profit_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/profit_icon.png"))
        self.profit_icon.setObjectName("profit_icon")
        self.take_prof_icon = QtWidgets.QLabel(self.centralwidget)
        self.take_prof_icon.setGeometry(QtCore.QRect(93, 330, 31, 31))
        self.take_prof_icon.setText("")
        self.take_prof_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/take_profit_icon.png"))
        self.take_prof_icon.setObjectName("take_prof_icon")
        self.stop_icon = QtWidgets.QLabel(self.centralwidget)
        self.stop_icon.setGeometry(QtCore.QRect(93, 370, 31, 31))
        self.stop_icon.setText("")
        self.stop_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/loss_icon.png"))
        self.stop_icon.setObjectName("stop_icon")
        self.short_icon = QtWidgets.QLabel(self.centralwidget)
        self.short_icon.setGeometry(QtCore.QRect(93, 290, 31, 31))
        self.short_icon.setText("")
        self.short_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/short_icon.png"))
        self.short_icon.setObjectName("short_icon")
        self.money_icon = QtWidgets.QLabel(self.centralwidget)
        self.money_icon.setGeometry(QtCore.QRect(93, 414, 31, 31))
        self.money_icon.setText("")
        self.money_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/cash_icon.png"))
        self.money_icon.setObjectName("money_icon")
        self.long_label = QtWidgets.QLabel(self.centralwidget)
        self.long_label.setGeometry(QtCore.QRect(150, 248, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.long_label.setFont(font)
        self.long_label.setStyleSheet("color: white;")
        self.long_label.setObjectName("long_label")
        self.short_label = QtWidgets.QLabel(self.centralwidget)
        self.short_label.setGeometry(QtCore.QRect(150, 288, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.short_label.setFont(font)
        self.short_label.setStyleSheet("color: white;")
        self.short_label.setObjectName("short_label")
        self.money_label = QtWidgets.QLabel(self.centralwidget)
        self.money_label.setGeometry(QtCore.QRect(150, 408, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.money_label.setFont(font)
        self.money_label.setStyleSheet("color: white;")
        self.money_label.setObjectName("money_label")
        self.profit_label = QtWidgets.QLabel(self.centralwidget)
        self.profit_label.setGeometry(QtCore.QRect(150, 448, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.profit_label.setFont(font)
        self.profit_label.setStyleSheet("color: white;")
        self.profit_label.setObjectName("profit_label")
        self.take_prof_label = QtWidgets.QLabel(self.centralwidget)
        self.take_prof_label.setGeometry(QtCore.QRect(150, 328, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.take_prof_label.setFont(font)
        self.take_prof_label.setStyleSheet("color: white;")
        self.take_prof_label.setObjectName("take_prof_label")
        self.stop_label = QtWidgets.QLabel(self.centralwidget)
        self.stop_label.setGeometry(QtCore.QRect(150, 368, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.stop_label.setFont(font)
        self.stop_label.setStyleSheet("color: white;")
        self.stop_label.setObjectName("stop_label")
        self.long_info = QtWidgets.QLabel(self.centralwidget)
        self.long_info.setGeometry(QtCore.QRect(596, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.long_info.setFont(font)
        self.long_info.setStyleSheet("color: white;\n"
                                     "border: 2px solid #5DA7DB;\n"
                                     "text-align: center;\n"
                                     "border-radius: 8px;")
        self.long_info.setAlignment(QtCore.Qt.AlignCenter)
        self.long_info.setObjectName("long_info")
        self.short_info = QtWidgets.QLabel(self.centralwidget)
        self.short_info.setGeometry(QtCore.QRect(596, 290, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.short_info.setFont(font)
        self.short_info.setStyleSheet("color: white;\n"
                                      "border: 2px solid #5DA7DB;\n"
                                      "text-align: center;\n"
                                      "border-radius: 8px;")
        self.short_info.setAlignment(QtCore.Qt.AlignCenter)
        self.short_info.setObjectName("short_info")
        self.take_prof_info = QtWidgets.QLabel(self.centralwidget)
        self.take_prof_info.setGeometry(QtCore.QRect(596, 330, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.take_prof_info.setFont(font)
        self.take_prof_info.setStyleSheet("color: white;\n"
                                          "border: 2px solid #5DA7DB;\n"
                                          "text-align: center;\n"
                                          "border-radius: 8px;")
        self.take_prof_info.setAlignment(QtCore.Qt.AlignCenter)
        self.take_prof_info.setObjectName("take_prof_info")
        self.stop_info = QtWidgets.QLabel(self.centralwidget)
        self.stop_info.setGeometry(QtCore.QRect(596, 370, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.stop_info.setFont(font)
        self.stop_info.setStyleSheet("color: white;\n"
                                     "border: 2px solid #5DA7DB;\n"
                                     "text-align: center;\n"
                                     "border-radius: 8px;")
        self.stop_info.setAlignment(QtCore.Qt.AlignCenter)
        self.stop_info.setObjectName("stop_info")
        self.money_info = QtWidgets.QLabel(self.centralwidget)
        self.money_info.setGeometry(QtCore.QRect(596, 410, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.money_info.setFont(font)
        self.money_info.setStyleSheet("color: white;\n"
                                      "border: 2px solid #5DA7DB;\n"
                                      "text-align: center;\n"
                                      "border-radius: 8px;")
        self.money_info.setAlignment(QtCore.Qt.AlignCenter)
        self.money_info.setObjectName("money_info")
        self.profit_info = QtWidgets.QLabel(self.centralwidget)
        self.profit_info.setGeometry(QtCore.QRect(596, 450, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.profit_info.setFont(font)
        self.profit_info.setStyleSheet("color: white;\n"
                                       "border: 2px solid #5DA7DB;\n"
                                       "text-align: center;\n"
                                       "border-radius: 8px;")
        self.profit_info.setAlignment(QtCore.Qt.AlignCenter)
        self.profit_info.setObjectName("profit_info")
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setEnabled(True)
        self.return_btn.setGeometry(QtCore.QRect(250, 500, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.return_btn.setFont(font)
        self.return_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.return_btn.setAutoFillBackground(False)
        self.return_btn.setStyleSheet("QPushButton{\n"
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
                                      "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/return_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.return_btn.setIcon(icon1)
        self.return_btn.setCheckable(False)
        self.return_btn.setObjectName("return_btn")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setEnabled(True)
        self.save_btn.setGeometry(QtCore.QRect(500, 500, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.save_btn.setFont(font)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_btn.setToolTipDuration(-3)
        self.save_btn.setAutoFillBackground(False)
        self.save_btn.setStyleSheet("QPushButton{\n"
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
        self.save_btn.setCheckable(False)
        self.save_btn.setObjectName("save_btn")
        self.detailed_table = QtWidgets.QTableWidget(self.centralwidget)
        self.detailed_table.setGeometry(QtCore.QRect(20, 10, 851, 221))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.detailed_table.setFont(font)
        self.detailed_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.detailed_table.setAutoFillBackground(False)
        self.detailed_table.setStyleSheet("QTableWidget{\n"
                                          "    background-color: transparent;\n"
                                          "    border: 2px solid white;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QTableWidget::item {\n"
                                          "    border: 2px solid white;\n"
                                          "}\n"
                                          "\n"
                                          "QHeaderView::section {\n"
                                          "    font-size: 14px;\n"
                                          "    font-weight: 700;\n"
                                          "    background-color: #6C4AB6;\n"
                                          "    border: 3px solid white;\n"
                                          "    color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar:vertical {\n"
                                          "    width: 10px;\n"
                                          "    background-color: white;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::handle:vertical {\n"
                                          "    margin-left: 2px;\n"
                                          "    border: none;\n"
                                          "    background-color: #6C4AB6;\n"
                                          "    width: 10px;\n"
                                          "    min-height: 20px;\n"
                                          "    max-height: 40px;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::add-line:vertical {\n"
                                          "    width: 0;\n"
                                          "    height: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QScrollBar::sub-line:vertical {\n"
                                          "    width: 0;\n"
                                          "    height: 0;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.detailed_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.detailed_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.detailed_table.setAutoScroll(True)
        self.detailed_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.detailed_table.setAlternatingRowColors(False)
        self.detailed_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.detailed_table.setShowGrid(False)
        self.detailed_table.setGridStyle(QtCore.Qt.NoPen)
        self.detailed_table.setWordWrap(False)
        self.detailed_table.setColumnCount(7)
        self.detailed_table.setObjectName("detailed_table")
        self.detailed_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.detailed_table.setHorizontalHeaderItem(6, item)
        self.detailed_table.horizontalHeader().setVisible(True)
        self.detailed_table.verticalHeader().setVisible(False)
        self.detailed_table.verticalHeader().setStretchLastSection(False)
        CertainResultWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CertainResultWindow)
        QtCore.QMetaObject.connectSlotsByName(CertainResultWindow)

    def retranslateUi(self, CertainResultWindow):
        _translate = QtCore.QCoreApplication.translate
        CertainResultWindow.setWindowTitle(_translate("CertainResultWindow", "Cash Counter"))
        self.long_label.setText(_translate("CertainResultWindow", "Количество long-сделок"))
        self.short_label.setText(_translate("CertainResultWindow", "Количество short-сделок"))
        self.money_label.setText(_translate("CertainResultWindow", "Вложенные средства"))
        self.profit_label.setText(_translate("CertainResultWindow", "Прибыль"))
        self.take_prof_label.setText(_translate("CertainResultWindow", "Количество сделок с \"плюсом\""))
        self.stop_label.setText(_translate("CertainResultWindow", "Количество сделок с \"минусом\""))
        self.long_info.setText(_translate("CertainResultWindow", "54"))
        self.short_info.setText(_translate("CertainResultWindow", "42"))
        self.take_prof_info.setText(_translate("CertainResultWindow", "79"))
        self.stop_info.setText(_translate("CertainResultWindow", "17"))
        self.money_info.setText(_translate("CertainResultWindow", "100000"))
        self.profit_info.setText(_translate("CertainResultWindow", "110000"))
        self.return_btn.setToolTip(_translate("CertainResultWindow", "На главный экран"))
        self.return_btn.setText(_translate("CertainResultWindow", "Вернуться"))
        self.save_btn.setToolTip(_translate("CertainResultWindow", "Сохранить в историю"))
        self.save_btn.setText(_translate("CertainResultWindow", "Сохранить результат"))
        self.detailed_table.setSortingEnabled(True)
        item = self.detailed_table.horizontalHeaderItem(0)
        item.setText(_translate("CertainResultWindow", "Время"))
        item = self.detailed_table.horizontalHeaderItem(1)
        item.setText(_translate("CertainResultWindow", "Тип сделки"))
        item = self.detailed_table.horizontalHeaderItem(2)
        item.setText(_translate("CertainResultWindow", "Цена акции"))
        item = self.detailed_table.horizontalHeaderItem(3)
        item.setText(_translate("CertainResultWindow", "Take-profit"))
        item = self.detailed_table.horizontalHeaderItem(4)
        item.setText(_translate("CertainResultWindow", "Stop-loss"))
        item = self.detailed_table.horizontalHeaderItem(5)
        item.setText(_translate("CertainResultWindow", "Количество акций"))
        item = self.detailed_table.horizontalHeaderItem(6)
        item.setText(_translate("CertainResultWindow", "Сумма сделки"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    CertainResultWindow = QtWidgets.QMainWindow()
    ui = Ui_CertainResultWindow()
    ui.setupUi(CertainResultWindow)
    CertainResultWindow.show()
    sys.exit(app.exec_())
