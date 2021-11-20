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

        # Create a spin box
        my_spin = qtw.QSpinBox(self,
                               value=10,
                               maximum=100,
                               minimum=0,
                               singleStep=5,
                               prefix="Your order is: # ")
                               # suffix=" Order")
        # my_spin = qtw.QDoubleSpinBox(self,
        #                        value=10.00,
        #                        maximum=100,
        #                        minimum=0,
        #                        singleStep=5.50,
        #                        prefix="# ",
        #                        suffix=" Order")
        # Change the font size of the spin box
        my_spin.setFont(qtg.QFont("Arial", 18))
        self.layout().addWidget(my_spin)

        # Create a button
        my_button = qtw.QPushButton("Press me!", clicked=lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            # add name to the label
            my_label.setText(f'You picked , {my_spin.value()}')


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
