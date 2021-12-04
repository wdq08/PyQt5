from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(100, 30, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setStyleSheet("color:red;")
        self.red_checkBox.setChecked(False)
        self.red_checkBox.setObjectName("red_checkBox")
        self.blue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(100, 80, 160, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setStyleSheet("color:blue;")
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 150, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 85, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Update check boxes
        # Use stateChanged if you want to know the state of the check boxes
        self.red_checkBox.stateChanged.connect(lambda: self.btnstate())
        # Use toggled is you don't care about the state of the check boxes
        self.blue_checkBox.toggled.connect(lambda: self.btnstate())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.label.setText(_translate("MainWindow", "Pick a color"))

    def btnstate(self):
        if self.red_checkBox.isChecked():
            self.red = "Red"
        else:
            self.red = ""
        if self.blue_checkBox.isChecked():
            self.blue = "Blue"
        else:
            self.blue = ""

        self.label.setText(f'{self.red} {self.blue}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
