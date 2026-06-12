# Running the app
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp
from databse import init_db

def main():
    app = QApplication(sys.argv)

    if not init_db("expense.db"):
        QMessageBox.critical(None, "Database Error", "Failed to initialize database...")
        return

    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())






if __name__ == "__main__":
    main()