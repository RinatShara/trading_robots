import os

from PyQt5 import QtCore, QtGui, QtWidgets

icons_way = os.getcwd()


class Ui_StrategyParamsWindow(object):
    def setupUi(self, StrategyParamsWindow):
        StrategyParamsWindow.setObjectName("StrategyParamsWindow")
        StrategyParamsWindow.setFixedSize(586, 306)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StrategyParamsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(StrategyParamsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg3_label = QtWidgets.QLabel(self.centralwidget)
        self.bg3_label.setGeometry(QtCore.QRect(-10, 0, 611, 341))
        self.bg3_label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, "
            "stop:0.494318 rgba(119, 67, 219, 255), stop:0.551136 rgba(119, 105, 219, 255));")
        self.bg3_label.setText("")
        self.bg3_label.setIndent(2)
        self.bg3_label.setObjectName("bg3_label")
        self.money_label = QtWidgets.QLabel(self.centralwidget)
        self.money_label.setGeometry(QtCore.QRect(50, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.money_label.setFont(font)
        self.money_label.setStyleSheet("color: white;")
        self.money_label.setObjectName("money_label")
        self.bag_risk_label = QtWidgets.QLabel(self.centralwidget)
        self.bag_risk_label.setGeometry(QtCore.QRect(20, 94, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.bag_risk_label.setFont(font)
        self.bag_risk_label.setStyleSheet("color: white;")
        self.bag_risk_label.setAlignment(QtCore.Qt.AlignCenter)
        self.bag_risk_label.setWordWrap(True)
        self.bag_risk_label.setObjectName("bag_risk_label")
        self.risk_profit_label = QtWidgets.QLabel(self.centralwidget)
        self.risk_profit_label.setGeometry(QtCore.QRect(0, 170, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.risk_profit_label.setFont(font)
        self.risk_profit_label.setStyleSheet("color: white;")
        self.risk_profit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.risk_profit_label.setWordWrap(True)
        self.risk_profit_label.setObjectName("risk_profit_label")
        self.set_money = QtWidgets.QLineEdit(self.centralwidget)
        self.set_money.setGeometry(QtCore.QRect(330, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.set_money.setFont(font)
        self.set_money.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.set_money.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.set_money.setStyleSheet("QLineEdit{\n"
                                     "    padding-left: 7px;\n"
                                     "    background-color: #5DA7DB;\n"
                                     "    color: white;\n"
                                     "    border-radius: 10px;\n"
                                     "}\n"
                                     "\n"
                                     ":hover, :focus{\n"
                                     "    background-color: #81C6E8;\n"
                                     "}")
        self.set_money.setAlignment(QtCore.Qt.AlignCenter)
        self.set_money.setObjectName("set_money")
        self.set_bag_risk = QtWidgets.QLineEdit(self.centralwidget)
        self.set_bag_risk.setGeometry(QtCore.QRect(330, 100, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.set_bag_risk.setFont(font)
        self.set_bag_risk.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.set_bag_risk.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.set_bag_risk.setStyleSheet("QLineEdit{\n"
                                          "    padding-left: 7px;\n"
                                          "    background-color: #5DA7DB;\n"
                                          "    color: white;\n"
                                          "    border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          ":hover, :focus{\n"
                                          "    background-color: #81C6E8;\n"
                                          "}")
        self.set_bag_risk.setAlignment(QtCore.Qt.AlignCenter)
        self.set_bag_risk.setObjectName("set_bag_risk")
        self.set_risk_profit = QtWidgets.QLineEdit(self.centralwidget)
        self.set_risk_profit.setGeometry(QtCore.QRect(330, 170, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.set_risk_profit.setFont(font)
        self.set_risk_profit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.set_risk_profit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.set_risk_profit.setStyleSheet("QLineEdit{\n"
                                           "    padding-left: 7px;\n"
                                           "    background-color: #5DA7DB;\n"
                                           "    color: white;\n"
                                           "    border-radius: 10px;\n"
                                           "}\n"
                                           "\n"
                                           ":hover, :focus{\n"
                                           "    background-color: #81C6E8;\n"
                                           "}")
        self.set_risk_profit.setAlignment(QtCore.Qt.AlignCenter)
        self.set_risk_profit.setObjectName("set_risk_profit")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(150, 245, 290, 41))
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
        self.return_btn = QtWidgets.QPushButton(self.centralwidget)
        self.return_btn.setEnabled(True)
        self.return_btn.setGeometry(QtCore.QRect(180, 240, 241, 51))
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
                                      "    background-color: #00FFAE;\n"
                                      "}\n"
                                      "\n"
                                      ":disabled{\n"
                                      "    color: rgba(255, 255, 255, 100);\n"
                                      "    background-color: #67207D;\n"
                                      "}\n"
                                      "\n"
                                      "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/return_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.return_btn.setIcon(icon1)
        self.return_btn.setCheckable(False)
        self.return_btn.setObjectName("return_btn")
        self.bg3_label.raise_()
        self.return_btn.raise_()
        self.money_label.raise_()
        self.bag_risk_label.raise_()
        self.risk_profit_label.raise_()
        self.set_money.raise_()
        self.set_bag_risk.raise_()
        self.set_risk_profit.raise_()
        self.error_label.raise_()
        StrategyParamsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StrategyParamsWindow)
        QtCore.QMetaObject.connectSlotsByName(StrategyParamsWindow)

    def retranslateUi(self, StrategyParamsWindow):
        _translate = QtCore.QCoreApplication.translate
        StrategyParamsWindow.setWindowTitle(_translate("StrategyParamsWindow", "Cash Counter"))
        self.money_label.setText(_translate("StrategyParamsWindow", "Свободные средства"))
        self.bag_risk_label.setText(_translate("StrategyParamsWindow", "% риска для портфеля на одну сделку"))
        self.risk_profit_label.setText(_translate("StrategyParamsWindow", "Соотношение риск/прибыль"))
        self.set_money.setPlaceholderText(_translate("StrategyParamsWindow", "Введите сумму"))
        self.set_bag_risk.setPlaceholderText(_translate("StrategyParamsWindow", "Введите процент"))
        self.set_risk_profit.setPlaceholderText(_translate("StrategyParamsWindow", "Введите коэффициент"))
        self.error_label.setToolTip(_translate("StrategyParamsWindow", "Ошибка"))
        self.error_label.setText(_translate("StrategyParamsWindow", "Неверный формат данных"))
        self.return_btn.setToolTip(_translate("StrategyParamsWindow", "На главный экран"))
        self.return_btn.setText(_translate("StrategyParamsWindow", "Вернуться назад"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    StrategyParamsWindow = QtWidgets.QMainWindow()
    ui = Ui_StrategyParamsWindow()
    ui.setupUi(StrategyParamsWindow)
    StrategyParamsWindow.show()
    sys.exit(app.exec_())
