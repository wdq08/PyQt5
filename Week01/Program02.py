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

        # Create a combo box
        my_combo = qtw.QComboBox(self,
                                 editable=True,
                                 insertPolicy=qtw.QComboBox.InsertAtTop)
        # my_combo = qtw.QComboBox(self,
        #                          editable=True,
        #                          insertPolicy=qtw.QComboBox.InsertAtBottom)
        # Add items to the combo box
        my_combo.addItem("Hello")
        my_combo.addItem("Goodbye")
        my_combo.addItem("Nothing")
        my_combo.addItems(["default", "Create", "anything"])
        my_combo.insertItems(2, ["One", "Two", "Third thing"])
        # Show the combo box
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = qtw.QPushButton("Press me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # add name to the label
            my_label.setText(f'You picked , {my_combo.currentText()}')
            # my_label.setText(f'You picked , {my_combo.currentData()}')
            # my_label.setText(f'You picked , {my_combo.currentIndex()}')


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
