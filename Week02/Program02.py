from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(5)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.outputLabel.setIndent(0)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(95, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(180, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(265, 110, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(180, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(265, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(95, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(180, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(265, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(95, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(180, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(265, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(95, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.decimaButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.dot_it())
        self.decimaButton.setGeometry(QtCore.QRect(180, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.decimaButton.setFont(font)
        self.decimaButton.setObjectName("decimaButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(265, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(95, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(48)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(42)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # remove character
    def remove_it(self):
        # grab what's on the screen already
        screen = self.outputLabel.text()
        # remove the last item in the string
        screen = screen[:-1]
        # output the string back to the screen
        self.outputLabel.setText(screen)

    # change from negative/positive
    def plus_minus_it(self):
        # grab what's on the screen already
        screen = self.outputLabel.text()
        if "-" == screen[0]:
            screen = screen[1:]
            self.outputLabel.setText(screen)
        else:
            self.outputLabel.setText(f'-{screen}')

    # Let's do some math
    def math_it(self):
        # grab what's on the screen already
        screen = self.outputLabel.text()
        try:
            # do the math
            answer = eval(screen)
            # if the string is too long than cut off some of them
            answer=str(answer)
            if len(answer)>13:
                answer=answer[0:13]
            # output the answer back to the screen
            self.outputLabel.setText(answer)
        except:
            # output the error message back to the screen
            self.outputLabel.setText("ERROR")

    # add a decimal
    def dot_it(self):
        # grab what's on the screen already
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # Check to see if starts with 0 and deletes it
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.multiplyButton.setText(_translate("MainWindow", "×"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.decimaButton.setText(_translate("MainWindow", "·"))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
