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
        my_label = qtw.QLabel("Hello World!!!")
        # Change the font size
        my_label.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_label)

        # Create a entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        self.layout().addWidget(my_entry)

        # Create a button
        my_button = qtw.QPushButton("Press me!",
                                    clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # add name to the label
            my_label.setText(f'Hello, {my_entry.text()}')
            # clear the entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
