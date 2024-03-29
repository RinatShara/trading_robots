import os
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets

icons_way = os.getcwd()


class Ui_ChooseModeWindow(object):
    def setupUi(self, ChooseModeWindow):
        ChooseModeWindow.setObjectName("ChooseModeWindow")
        ChooseModeWindow.setEnabled(True)
        ChooseModeWindow.setFixedSize(309, 469)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChooseModeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ChooseModeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg1_label = QtWidgets.QLabel(self.centralwidget)
        self.bg1_label.setGeometry(QtCore.QRect(-4, -10, 321, 611))
        self.bg1_label.setStyleSheet("background-color:  #7743DB;")
        self.bg1_label.setText("")
        self.bg1_label.setIndent(2)
        self.bg1_label.setObjectName("bg1_label")
        self.choose_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_label.setGeometry(QtCore.QRect(30, 161, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.choose_label.setFont(font)
        self.choose_label.setStyleSheet("color: white;")
        self.choose_label.setObjectName("choose_label")
        self.euro_icon = QtWidgets.QLabel(self.centralwidget)
        self.euro_icon.setGeometry(QtCore.QRect(160, 78, 31, 41))
        self.euro_icon.setText("")
        self.euro_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/euro_icon.png"))
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
        self.current_time = QtWidgets.QLabel(self.centralwidget)
        self.current_time.setGeometry(QtCore.QRect(80, 28, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.current_time.setFont(font)
        self.current_time.setStyleSheet("color: white;")
        self.current_time.setObjectName("current_time")
        self.calen_icon = QtWidgets.QLabel(self.centralwidget)
        self.calen_icon.setGeometry(QtCore.QRect(160, 28, 31, 41))
        self.calen_icon.setText("")
        self.calen_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/calen_icon.png"))
        self.calen_icon.setObjectName("calen_icon")
        self.current_date = QtWidgets.QLabel(self.centralwidget)
        self.current_date.setGeometry(QtCore.QRect(190, 28, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.current_date.setFont(font)
        self.current_date.setStyleSheet("color: white;")
        self.current_date.setObjectName("current_date")
        self.dollar_icon = QtWidgets.QLabel(self.centralwidget)
        self.dollar_icon.setGeometry(QtCore.QRect(50, 78, 31, 41))
        self.dollar_icon.setText("")
        self.dollar_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/dollar_icon.png"))
        self.dollar_icon.setObjectName("dollar_icon")
        self.dollar_price = QtWidgets.QLabel(self.centralwidget)
        self.dollar_price.setGeometry(QtCore.QRect(80, 78, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.dollar_price.setFont(font)
        self.dollar_price.setStyleSheet("color: white;")
        self.dollar_price.setObjectName("dollar_price")
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
        self.clock_icon = QtWidgets.QLabel(self.centralwidget)
        self.clock_icon.setGeometry(QtCore.QRect(50, 28, 31, 41))
        self.clock_icon.setText("")
        self.clock_icon.setPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/clock_icon.png"))
        self.clock_icon.setObjectName("clock_icon")
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
        ChooseModeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChooseModeWindow)
        QtCore.QMetaObject.connectSlotsByName(ChooseModeWindow)

    def retranslateUi(self, ChooseModeWindow):
        time = datetime.now()
        _translate = QtCore.QCoreApplication.translate
        ChooseModeWindow.setWindowTitle(_translate("ChooseModeWindow", "Cash Counter"))
        self.choose_label.setText(_translate("ChooseModeWindow", "Выберите режим запуска "))
        self.sand_btn.setText(_translate("ChooseModeWindow", "Торговля в \"песочнице\""))
        self.current_time.setText(_translate("ChooseModeWindow", f"{time.hour}:{str(time.minute).rjust(2, '0')}"))
        self.current_date.setText(_translate("ChooseModeWindow", "23.11.2022"))
        self.dollar_price.setText(_translate("ChooseModeWindow", "60.26"))
        self.test_btn.setText(_translate("ChooseModeWindow", "Тестирование стратегий"))
        self.euro_price.setText(_translate("ChooseModeWindow", "70.51"))
        self.real_btn.setText(_translate("ChooseModeWindow", "Торговля на реальном рынке"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ChooseModeWindow = QtWidgets.QMainWindow()
    ui = Ui_ChooseModeWindow()
    ui.setupUi(ChooseModeWindow)
    ChooseModeWindow.show()
    sys.exit(app.exec_())
