# Task 1: OOP-based Application Development

## Introduction Video
> **Task 1 Video Link:** https://youtu.be/eYSb_bpbAUQ

## Project Overview
This directory contains a robust, multi-modular Python application for calculating stock profitability across various statement files. It fully utilizes the required Object-Oriented Programming (OOP) paradigms taught in the COMP 8090 course.

### Concepts Applied:
- **Modules**: The system is cleanly modularized. `main.py`, `models.py`, and `parsers.py` handle the core OOP logic, while `max_heap.py` and `quick_sort.py` are integrated as algorithmic utilities to sort trade dates and extract the Top 5 most profitable stocks efficiently.
- **Encapsulation**: Used in data models and parser wrappers.
- **Inheritance & Polymorphism**: Handled via abstract base classes (`StatementParser`) and specialized subclasses (`CSVParser`, `PDFParser`).
- **Methods**: Extensively utilizes magic methods, instance methods, and static methods for internal computation.

## 📖 User Guide
1. **Prerequisites**: Ensure Python 3.9+ is installed.
2. **Dependencies**: Run `pip install pypdf` (if you intend to test the PDF parser with real encrypted PDF statements).
3. **Execution**: Run the main program via terminal:
   ```bash
   python main.py
   ```
4. **Interaction**: Use the numbered Command Line Interface (CLI). Choose **Option `1`** to automatically load 12 months of generated mock data from the `monthly_statements/` folder, and then view calculated portfolios and the top 5 highest-yielding stocks.
