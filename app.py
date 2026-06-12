from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QDateEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import QDate, Qt
from database import fetch_expenses, add_expense_to_db, delete_expense_from_db

class CashFlowApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_table_data()

    def init_ui(self):
        self.setWindowTitle("CashFlow")
        self.resize(560, 520)

        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("Add Transaction")
        self.delete_button = QPushButton("Remove Entry")

        self.table = QTableWidget(0, 5)
        self.table.setHorizontalHeaderLabels(["ID", "Date", "Category", "Amount", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)

        self.setup_layout()
        self.populate_dropdown()
        self.apply_styles()

    def setup_layout(self):
        layout = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        row3.addWidget(self.add_button)
        row3.addWidget(self.delete_button)

        layout.addLayout(row1)
        layout.addLayout(row2)
        layout.addLayout(row3)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def populate_dropdown(self):
        categories = ["Rent", "Food", "Bills", "Transportation", "Shopping", "Entertainment", "Other"]
        self.dropdown.addItems(categories)

    def apply_styles(self):
        self.setStyleSheet("""
    QWidget {
        background-color: #1e2430;
        font-family: 'Segoe UI', sans-serif;
        font-size: 14px;
        color: #e0e6ed;
    }

    QLabel {
        font-size: 16px;
        color: #b8c5d6;
        font-weight: bold;
        padding: 5px;
    }

    QLineEdit, QComboBox, QDateEdit {
        background-color: #2a3140;
        font-size: 14px;
        color: #e0e6ed;
        border: 1px solid #4a5568;
        border-radius: 5px;
        padding: 5px;
    }
    QLineEdit:hover, QComboBox:hover, QDateEdit:hover {
        border: 1px solid #3d8b7a;
    }
    QLineEdit:focus, QComboBox:focus, QDateEdit:focus {
        border: 1px solid #4a9e8c;
        background-color: #2f3849;
    }

    QTableWidget {
        background-color: #252d3a;
        alternate-background-color: #2a3140;
        gridline-color: #4a5568;
        selection-background-color: #3d8b7a;
        selection-color: white;
        font-size: 14px;
        border: 1px solid #4a5568;
        color: #e0e6ed;
    }
    QHeaderView::section {
        background-color: #3d8b7a;
        color: white;
        font-weight: bold;
        padding: 4px;
        border: 1px solid #4a5568;
    }

    QScrollBar:vertical {
        width: 12px;
        background-color: #2a3140;
        border: none;
    }
    QScrollBar::handle:vertical {
        background-color: #3d8b7a;
        min-height: 20px;
        border-radius: 5px;
    }
    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
        background: none;
    }

    QPushButton {
        background-color: #3d8b7a;
        color: white;
        padding: 10px 15px;
        border-radius: 5px;
        font-size: 14px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #4a9e8c;
    }
    QPushButton:pressed {
        background-color: #2f6f61;
    }
    QPushButton:disabled {
        background-color: #3a3f4b;
        color: #6e6e6e;
    }

    QToolTip {
        background-color: #2a3140;
        color: #e0e6ed;
        border: 1px solid #4a5568;
        font-size: 12px;
        padding: 5px;
        border-radius: 4px;
    }
""")


    def load_table_data(self):
        expenses = fetch_expenses()
        self.table.setRowCount(0)
        for row_idx, expense in enumerate(expenses):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(expense):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        if not amount or not description:
            QMessageBox.warning(self, "CashFlow — Input Error", "Amount and Description cannot be empty!")
            return

        if add_expense_to_db(date, category, amount, description):
            self.load_table_data()
            self.clear_inputs()
        else:
            QMessageBox.critical(self, "CashFlow — Error", "Failed to add expense")

    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "CashFlow — No Selection", "Please select an expense to delete.")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(self, "CashFlow — Confirm Delete", "Are you sure you want to delete this expense?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if confirm == QMessageBox.StandardButton.Yes and delete_expense_from_db(expense_id):
            self.load_table_data()

    def clear_inputs(self):
        self.date_box.setDate(QDate.currentDate())
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()
