import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title
        self.setWindowTitle("Hello World!!!")

        # set layout
        self.setLayout(qtw.QHBoxLayout())

        # Create A Label
        my_label = qtw.QLabel("Hello World!!!")
        # Change the font size
        my_label.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_label)

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
