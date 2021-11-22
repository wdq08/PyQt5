import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title
        self.setWindowTitle("Hello, what's your name?")

        # set layout
        self.setLayout(qtw.QVBoxLayout())

        # Create A Label
        my_label = qtw.QLabel("Pick something form the list")
        # Change the font size
        my_label.setFont(qtg.QFont("Arial", 24))
        self.layout().addWidget(my_label)

        # Create a text box
        my_text = qtw.QTextEdit(self,
                                # plainText="This is real text!!!",
                                html="<center><h1>Big Header Text!</h1></center>",
                                acceptRichText=True,
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
                                lineWrapColumnOrWidth=80,
                                placeholderText="Hello World!",
                                readOnly=False)
        # Change the font size of the spin box
        # my_spin.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_text)

        # Create a button
        my_button = qtw.QPushButton("Press me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # add name to the label
            my_label.setText(f'You typed , {my_text.toPlainText()}')
            my_text.setPlainText("You pressed the button!")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
