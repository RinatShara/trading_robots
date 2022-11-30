import os

from PyQt5 import QtCore, QtGui, QtWidgets

icons_way = os.getcwd()


class Ui_HistoryTestsWindow(object):
    def setupUi(self, HistoryTestsWindow):
        HistoryTestsWindow.setObjectName("HistoryTestsWindow")
        HistoryTestsWindow.setFixedSize(989, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HistoryTestsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HistoryTestsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg5_label = QtWidgets.QLabel(self.centralwidget)
        self.bg5_label.setGeometry(QtCore.QRect(-10, -10, 1051, 481))
        self.bg5_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0.431818 rgba(119, 67, 219, 255), stop:0.482955 rgba(119, 105, 219, 255));")
        self.bg5_label.setText("")
        self.bg5_label.setIndent(2)
        self.bg5_label.setObjectName("bg5_label")
        self.general_table = QtWidgets.QTableWidget(self.centralwidget)
        self.general_table.setGeometry(QtCore.QRect(20, 10, 931, 351))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.general_table.setFont(font)
        self.general_table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.general_table.setAutoFillBackground(False)
        self.general_table.setStyleSheet("QTableWidget{\n"
                                         "    background-color: transparent;\n"
                                         "    border: 2px solid white;\n"
                                         "    color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QTableWidget::item {\n"
                                         "    border: 2px solid white;\n"
                                         "}\n"
                                         "\n"
                                         "QTableWidget::item:selected {\n"
                                         "	outline: none;\n"
                                         "	background-color: #8D9EFF;\n"
                                         "   color: white;\n"
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
                                         "")
        self.general_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.general_table.setAutoScroll(True)
        self.general_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.general_table.setAlternatingRowColors(False)
        self.general_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.general_table.setShowGrid(False)
        self.general_table.setGridStyle(QtCore.Qt.NoPen)
        self.general_table.setWordWrap(False)
        self.general_table.setColumnCount(7)
        self.general_table.setObjectName("general_table")
        self.general_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.general_table.setHorizontalHeaderItem(6, item)
        self.general_table.horizontalHeader().setVisible(True)
        self.general_table.verticalHeader().setVisible(False)
        self.general_table.verticalHeader().setStretchLastSection(False)
        self.detailed_btn = QtWidgets.QPushButton(self.centralwidget)
        self.detailed_btn.setEnabled(True)
        self.detailed_btn.setGeometry(QtCore.QRect(520, 390, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.detailed_btn.setFont(font)
        self.detailed_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.detailed_btn.setToolTipDuration(-3)
        self.detailed_btn.setAutoFillBackground(False)
        self.detailed_btn.setStyleSheet("QPushButton{\n"
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
        self.detailed_btn.setCheckable(False)
        self.detailed_btn.setObjectName("detailed_btn")
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setEnabled(True)
        self.return_btn.setGeometry(QtCore.QRect(270, 390, 191, 51))
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
        HistoryTestsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HistoryTestsWindow)
        QtCore.QMetaObject.connectSlotsByName(HistoryTestsWindow)

    def retranslateUi(self, HistoryTestsWindow):
        _translate = QtCore.QCoreApplication.translate
        HistoryTestsWindow.setWindowTitle(_translate("HistoryTestsWindow", "Cash Counter"))
        self.general_table.setSortingEnabled(True)
        item = self.general_table.horizontalHeaderItem(0)
        item.setText(_translate("HistoryTestsWindow", "Стратегия"))
        item = self.general_table.horizontalHeaderItem(1)
        item.setText(_translate("HistoryTestsWindow", "Компания"))
        item = self.general_table.horizontalHeaderItem(2)
        item.setText(_translate("HistoryTestsWindow", "Период тестирования"))
        item = self.general_table.horizontalHeaderItem(3)
        item.setText(_translate("HistoryTestsWindow", "Свободные средства"))
        item = self.general_table.horizontalHeaderItem(4)
        item.setText(_translate("HistoryTestsWindow", "% на одну сделку"))
        item = self.general_table.horizontalHeaderItem(5)
        item.setText(_translate("HistoryTestsWindow", "Риск/прибыль"))
        item = self.general_table.horizontalHeaderItem(6)
        item.setText(_translate("HistoryTestsWindow", "Прибыль"))
        self.detailed_btn.setToolTip(_translate("HistoryTestsWindow", "Вывести больше информации"))
        self.detailed_btn.setText(_translate("HistoryTestsWindow", "Подробнее"))
        self.return_btn.setToolTip(_translate("HistoryTestsWindow", "На главный экран"))
        self.return_btn.setText(_translate("HistoryTestsWindow", "Вернуться"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    HistoryTestsWindow = QtWidgets.QMainWindow()
    ui = Ui_HistoryTestsWindow()
    ui.setupUi(HistoryTestsWindow)
    HistoryTestsWindow.show()
    sys.exit(app.exec_())
