# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time

import os


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Registration")

        self.setWindowTitle("Add student")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addstudent)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("РФМШ")
        self.branchinput.addItem("НИШ")
        self.branchinput.addItem("БИЛ")
        self.branchinput.addItem("Школа №165")
        self.branchinput.addItem("Школа №120")
        self.branchinput.addItem("Школа №166")
        self.branchinput.addItem("Школа №34")
        self.branchinput.addItem("Школа №134")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1 class")
        self.seminput.addItem("2 class")
        self.seminput.addItem("3 class")
        self.seminput.addItem("4 class")
        self.seminput.addItem("5 class")
        self.seminput.addItem("6 class")
        self.seminput.addItem("7 class")
        self.seminput.addItem("8 class")
        self.seminput.addItem("9 class")
        self.seminput.addItem("10 class")
        self.seminput.addItem("11 class")
        layout.addWidget(self.seminput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Number")
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Adress")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):

        name = ""
        branch = ""
        sem = -1
        mobile = -1
        address = ""

        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)", (name, branch, sem, mobile, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find student from database.')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("ID")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from students WHERE roll=" + str(searchrol))
            row = result.fetchone()
            searchresult = "ID : " + str(row[0]) + '\n' + "Имя : " + str(row[1]) + '\n' + "Школа : " + str(row[2]) + '\n' + "Класс : " + str(row[3]) + '\n' + "Адрес : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Успешно', searchresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not find student from database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete student")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("ID")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):

        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE roll=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Sucsessful', 'You have successfully deleted a student')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Failed to remove student from database.')


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(300)
        self.setFixedHeight(120)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Password")
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")
        self.setWindowTitle('Login')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        if(self.passinput.text() == " "):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong password, try again')


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&Functions")

        help_menu = self.menuBar().addMenu("&Info")
        self.setWindowTitle("Student Data")

        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("ID", "Name", "School", "Class", "Number", "Adress"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("add.png"), "Add student", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add student")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("refresh.png"), "Refresh", self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("search.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("trash.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete")
        toolbar.addAction(btn_ac_delete)

        adduser_action = QAction(QIcon("add.png"), "Add student", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("search.png"), "Search", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("delete.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)

        about_action = QAction(QIcon("info.png"), "Info", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database.db")
        query = "SELECT * FROM students"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()
        
class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(300)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Автор программы Ким Максим")
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/logo.png')
        pixmap = pixmap.scaledToWidth(275) 
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(200)

        layout.addWidget(title)

        layout.addWidget(QLabel("Эта программа создана для хранения базы данных учеников города Алматы"))
        layout.addWidget(QLabel("Вы можете вводить данные ученика и они будут храниться в этой базе"))
        layout.addWidget(QLabel("Также вы можете по ID ученика найти его данные"))
        layout.addWidget(QLabel(" "))
        layout.addWidget(QLabel(" "))
        layout.addWidget(QLabel("По всем вопросам обращаться по номеру: +7 (775) 654 77-77"))
        layout.addWidget(QLabel("Писать на почту: maximkim.29.06.2k5@gmail.com"))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


app = QApplication(sys.argv)
passdlg = LoginDialog()
if(passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
