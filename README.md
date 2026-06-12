# CashFlow

A modular desktop application for tracking personal expenditures. CashFlow provides a lightweight interface for recording transactions and managing spending data with persistent local storage.

**Tech stack:** Python · PyQt6 · SQLite

## Features

- Record and remove transactions with date, category, amount, and description
- Local persistence through an SQLite database
- Custom dark-themed interface with input validation and confirmation dialogs

## Requirements

- Python 3.10 or later
- [PyQt6](https://pypi.org/project/PyQt6/)

## Installation

```bash
pip install PyQt6
```

## Usage

```bash
python main.py
```

## Project Structure

| File | Description |
|------|-------------|
| `main.py` | Application entry point and database initialization |
| `app.py` | PyQt6 user interface and event handling |
| `database.py` | SQLite connection and data operations |

## Acknowledgments

Project structure and implementation were informed by [this PyQt6 tutorial](https://www.youtube.com/watch?v=I8S9V8AYjtA&t=2043s).

## License

This project is licensed under the [MIT License](LICENSE).
