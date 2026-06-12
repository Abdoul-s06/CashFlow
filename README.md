# CashFlow

A desktop personal finance app for tracking expenditures. Built with Python, PyQt6, and SQLite.

## Features

- Add and remove transactions with date, category, amount, and description
- Persistent storage via SQLite (`cashflow.db`)
- Dark-themed UI with form validation and confirmation dialogs

## Requirements

- Python 3.10+
- [PyQt6](https://pypi.org/project/PyQt6/)

## Getting Started

```bash
pip install PyQt6
python main.py
```

## Project Structure

```
CashFlow/
├── main.py       # Entry point
├── app.py        # PyQt6 UI
└── database.py   # SQLite operations
```

## License

MIT
