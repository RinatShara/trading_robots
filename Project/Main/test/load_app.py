import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow

from Project.Designs.Python.load_window_design import Ui_LoadWindow
from Project.Designs.Python.choose_mode_design import Ui_ChooseModeWindow
from Project.Designs.Python.testing_mode_design import Ui_TestingWindow


class LoadWindow(Ui_LoadWindow, QMainWindow):
    def __init__(self):
        super(LoadWindow, self).__init__()
        self.setupUi(self)
        self.show()
        time.sleep(10.0)
        self.open_choice()

    def open_choice(self):
        self.hide()
        choose_example = ChooseWindow()
        choose_example.setupUi(self)
        choose_example.show()


class ChooseWindow(Ui_ChooseModeWindow, QMainWindow):
    def __init__(self):
        super(ChooseWindow, self).__init__()
        self.setupUi(self)
        self.add_functions()

    def add_functions(self):
        self.test_btn.clicked.connect(self.open_test_mode)

    def open_test_mode(self):
        self.hide()
        test_window = TestingWindow()
        test_window.setupUi(self)
        test_window.show()


class TestingWindow(QMainWindow, Ui_TestingWindow):
    def __init__(self):
        super(TestingWindow, self).__init__()
        self.setupUi(self)
        self.edit_items()

    def edit_items(self):
        self.error_label.setVisible(False)
        self.calendar.setVisible(False)
        self.start_btn.setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = LoadWindow()
    example.show()
    sys.exit(app.exec())