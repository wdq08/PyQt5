from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(500, 200)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 440, 120))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate("SecondWindow", "Type something in the other window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
