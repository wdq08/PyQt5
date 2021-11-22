import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title
        self.setWindowTitle("Hello World!")

        # Set Layout
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add Stuff/Widgets
        label_1 = qtw.QLabel("This is a cool label row")
        label_1.setFont(qtg.QFont("Arial", 24))

        f_name = qtw.QLineEdit(self)
        l_name = qtw.QLineEdit(self)

        # Add Rows to app
        form_layout.addRow(label_1)
        form_layout.addRow("First name", f_name)
        form_layout.addRow("Last name", l_name)
        form_layout.addRow(qtw.QPushButton("Press me!",
                                           clicked=lambda: press_it()))

        # Show the app
        self.show()

        def press_it():
            label_1.setText(f"You clicked the button, {f_name.text()} {l_name.text()}")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()
