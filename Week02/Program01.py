from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_me_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it())
        self.click_me_button.setGeometry(QtCore.QRect(60, 390, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.click_me_button.setFont(font)
        self.click_me_button.setObjectName("click_me_button")
        self.hello_world_label = QtWidgets.QLabel(self.centralwidget)
        self.hello_world_label.setGeometry(QtCore.QRect(110, 130, 371, 171))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.hello_world_label.setFont(font)
        self.hello_world_label.setObjectName("hello_world_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # press the button function
    def press_it(self):
        self.hello_world_label.setText("Boom!")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_me_button.setText(_translate("MainWindow", "Click Me!"))
        self.hello_world_label.setText(_translate("MainWindow", "Hello World!"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
