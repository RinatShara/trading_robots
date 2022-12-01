import os

from PyQt5 import QtCore, QtGui, QtWidgets

icons_way = os.getcwd()

class Ui_WaitWindow(object):
    def setupUi(self, WaitWindow):
        WaitWindow.setObjectName("WaitWindow")
        WaitWindow.resize(424, 253)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{icons_way}/design/Icons/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WaitWindow.setWindowIcon(icon)
        WaitWindow.setStyleSheet("background-color:  rgb(119, 67, 219);")
        self.centralwidget = QtWidgets.QWidget(WaitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(94, 50, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 120, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setObjectName("label_2")
        WaitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(WaitWindow)
        QtCore.QMetaObject.connectSlotsByName(WaitWindow)

    def retranslateUi(self, WaitWindow):
        _translate = QtCore.QCoreApplication.translate
        WaitWindow.setWindowTitle(_translate("WaitWindow", "Cash Counter"))
        self.label.setText(_translate("WaitWindow", "Тестирование началось"))
        self.label_2.setText(_translate("WaitWindow", "Пожалуйста, подождите"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WaitWindow = QtWidgets.QMainWindow()
    ui = Ui_WaitWindow()
    ui.setupUi(WaitWindow)
    WaitWindow.show()
    sys.exit(app.exec_())
