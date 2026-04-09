# Stock Profit Calculator (COMP 8090SEF Course Project)

## Repository Contents
This repository contains the source code for both **Task 1** and **Task 2** of the course project.

### 🎥 Introduction Video Links
> **Task 1 Video:** [INSERT YOUR 5-MINUTE YOUTUBE/GOOGLE DRIVE VIDEO LINK HERE]
> 
> **Task 2 Video:** [INSERT YOUR 5-MINUTE YOUTUBE/GOOGLE DRIVE VIDEO LINK HERE]

## Task 1: OOP-based Application Development
The `Task1_OOP_Project/` directory contains a robust, multi-modular Python application calculating stock profitability across various statement files. 
It fully utilizes the required Object-Oriented Programming (OOP) paradigms taught in this course:
- **Modules**: `main.py`, `models.py`, `parsers.py`
- **Encapsulation**: Used in data models and parser wrappers.
- **Inheritance & Polymorphism**: Handled via abstract base classes (`StatementParser`) and specialized subclasses (`CSVParser`).
- **Magic Methods & Static Methods**: Extensively used for internal computation and terminal representation.

### 📖 User Guide for Task 1
1. **Prerequisites**: Ensure Python 3.9+ is installed.
2. **Setup**: Run `pip install -r requirements.txt` if using PDF features (requires `pypdf`).
3. **Execution**: Run the main program via terminal:
   ```bash
   python Task1_OOP_Project/main.py
   ```
4. **Interaction**: Use the numbered Command Line Interface (CLI) to load files from `Task1_OOP_Project/monthly_statements/` and view calculated portfolios.

---

## Task 2: Self-Study on Data Structure & Algorithm
The `Task2_SelfStudy/` directory contains pure Python implementations of algorithms and structures **not covered in the course material**.

- **Algorithm**: **Quick Sort** ($O(N \log N)$), used to sort trades chronologically and by profit margin efficiently instead of brute-force.
- **Data Structure**: **Max-Heap (Priority Queue)** ($O(\log N)$ extraction), used to discover the extreme top $N$ most profitable trades dynamically from unsorted streams.

### 📖 User Guide for Task 2
1. **Execution**: To run the standalone demonstration of sorting and priority queue behaviors, run:
   ```bash
   python Task2_SelfStudy/main.py
   ```
2. **Expected Output**: The terminal will display the mock dataset, its chronologically sorted state (via Quick Sort), and the absolute top 3 most profitable moments extracted instantly (via Max Heap).

---
*Developed for COMP 2090SEF / 8090SEF Project.*
