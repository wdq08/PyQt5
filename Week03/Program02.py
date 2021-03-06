from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# Create a database or connect to one
connect = sqlite3.connect('myList.db')
# Create a cursor
cursor = connect.cursor()

# Create a table
cursor.execute("""CREATE TABLE if not exists todo_list(
    list_item text)
""")

# Commit the changes
connect.commit()

# Close the connections
connect.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(20, 110, 360, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addItem_pushButton.setFont(font)
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(20, 190, 360, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myList_listWidget.setFont(font)
        self.myList_listWidget.setObjectName("myList_listWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 30, 360, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(20, 70, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.deleteItem_pushButton.setFont(font)
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(210, 70, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clearAll_pushButton.setFont(font)
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")
        self.savedb_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_it())
        self.savedb_pushButton.setGeometry(QtCore.QRect(20, 150, 360, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.savedb_pushButton.setFont(font)
        self.savedb_pushButton.setObjectName("savedb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Grab all the items from the database
        self.grab_all()

    def grab_all(self):
        # Create a database or connect to one
        connect = sqlite3.connect('myList.db')

        # Create a cursor
        cursor = connect.cursor()

        cursor.execute("SELECT * FROM todo_list")
        records = cursor.fetchall()

        # Commit the changes
        connect.commit()

        # Close the connections
        connect.close()

        # Loop through the records and add to the screen
        for record in records:
            self.myList_listWidget.addItem(str(record[0]))

    # Add item to the list
    def add_it(self):
        # Grab the item from the input box
        item = self.lineEdit.text()

        # Add the item to the list box
        self.myList_listWidget.addItem(item)

        # Clear the input box
        self.lineEdit.setText("")

    # Delete item from the list
    def delete_it(self):
        # Grab the selected row or current row
        clicked = self.myList_listWidget.currentRow()

        # Delete the current row
        self.myList_listWidget.takeItem(clicked)

    # Clear the list
    def clear_it(self):
        self.myList_listWidget.clear()

    # Save the list to the database
    def save_it(self):
        # Create a database or connect to one
        connect = sqlite3.connect('myList.db')

        # Create a cursor
        cursor = connect.cursor()

        # Delete everything in the database
        cursor.execute('DELETE FROM todo_list;', )

        # Create a blank list to hold the list items
        items = []
        # loop through the listWidget and pull out all the items
        for index in range(self.myList_listWidget.count()):
            items.append(self.myList_listWidget.item(index))
        for item in items:
            # print(item.text())
            # Add stuff to the table
            cursor.execute('INSERT INTO todo_list VALUES (:item)',
                           {
                               'item': item.text(),
                           })

        # Commit the changes
        connect.commit()

        # Close the connections
        connect.close()

        # Pop up the message box
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your todo list has been saved")
        msg.setIcon(QMessageBox.Information)
        execute = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item to the List"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Clear All"))
        self.savedb_pushButton.setText(_translate("MainWindow", "Save to Database"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
