import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from database import init_db
from app import CashFlowApp

def main():
    app = QApplication(sys.argv)

    if not init_db("cashflow.db"):
        QMessageBox.critical(None, "Error", "Could not open your database")
        sys.exit(1)

    window = CashFlowApp()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
