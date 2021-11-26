from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 280)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.checked())
        self.pushButton.setGeometry(QtCore.QRect(30, 130, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0.5, x2:0, y2:0.5, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 190, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(0, 85, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Pick a color"))

    def checked(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
