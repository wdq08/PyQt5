from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.push_1())
        self.button1_pushButton.setGeometry(QtCore.QRect(20, 20, 220, 200))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button1_pushButton.setFont(font)
        self.button1_pushButton.setObjectName("button1_pushButton")
        self.button2_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.push_2())
        self.button2_pushButton.setGeometry(QtCore.QRect(260, 20, 220, 200))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.button2_pushButton.setFont(font)
        self.button2_pushButton.setObjectName("button2_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Change the status bar font
        self.statusbar.setFont(QFont('Arial',16))
        self.statusbar.showMessage("Press a button!")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def push_1(self):
        self.statusbar.showMessage("You pressed button 1 !!!")

    def push_2(self):
        self.statusbar.showMessage("You pressed button 2 !!!")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Status Bar Stuff"))
        self.button1_pushButton.setText(_translate("MainWindow", "Button 1"))
        self.button2_pushButton.setText(_translate("MainWindow", "Button 2"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
