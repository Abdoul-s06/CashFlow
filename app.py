#App Design
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)

from PyQt6.QtCore import QDate, Qt

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()

    def settings(self):
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle("Expense Tracker App")


    def initUI(self):
        #Create all objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.btn_add = QPushButton("Add Expense")
        self.btn_delete = QPushButton("Delete Expense")

        self.table = QTableWidget(0,5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_dropdown()

        #Add widgets to layout
        self.setup_layout()


    def setup_layout(self):
        master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        #Row 1
        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        #Row 2
        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        #Row 3
        row3.addWidget(self.btn_add)
        row3.addWidget(self.btn_delete)

        #Add rows to master layout
        master.addLayout(row1)
        master.addLayout(row2)
        master.addLayout(row3)
        master.addWidget(self.table)

        #Set master layout
        self.setLayout(master)

    def populate_dropdown(self):
        categories = ["Food", "Rent", "Bills", "Entertainment", "Shopping", "Other"]
        self.dropdown.addItems(categories)