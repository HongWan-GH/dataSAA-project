# Hong Kong Metropolitan University
# COMP8090SEF Data Structures and Algorithms
## Course Project Report - Task 1

**Submission date:** April 12, 2026
**NAME:** [Your Name Here]
**SID:** [Your SID Here]

**(Please insert the official compulsory declaration statement here on the actual PDF cover page)**

---

## 1. Problem Definition & Core Functions
**Background:**
When retail investors trade stocks, they usually get monthly statements from their brokers in different formats, like CSV files or sometimes even simple PDFs. It’s actually quite annoying and error-prone to manually go through all these files, match up the buy and sell orders across different months, and figure out how much money was actually made or lost on each stock. 

**What this project does:**
To solve this, I built a automated "Stock Profit Calculator." The main idea is that it can look at a folder full of these statements, automatically figure out if a file is a `.csv` or a `.pdf`, read the trade histories, and then calculate the total realized profit. It uses a moving average cost approach to match up the shares bought and sold, and finally prints out a report showing the most profitable stocks.

## 2. Object-Oriented Programming (OOP) Concepts
To meet the requirements of Task 1, the whole system is designed using OOP. I split the code into several files (modules) like `models.py`, `parsers.py`, and `main.py` so it's not just one messy script. Here is how I applied the core OOP concepts we learned in class:

*   **Classes and Objects:** In `models.py`, I created `Trade` and `StockPosition` classes. They act as the blueprints. When the program reads a line from a CSV file saying "Bought 100 shares of AAPL", it creates a new `Trade` object to hold that specific transaction.
*   **Encapsulation:** I wanted to make sure the core data of a trade couldn't be accidentally messed up by other parts of the code. So, things like the stock ticker (`__ticker`), price, and quantity are made private by putting two underscores in front of them. To read them, I used `@property` decorators (getters), which gives safe, read-only access.
*   **Inheritance and Polymorphism:** This was the most useful part for handling different file types. In `parsers.py`, I made a general parent class called `StatementParser`. Then, I created two child classes: `CSVParser` and `PDFParser` that inherit from it. The magic of polymorphism is that the main program just tells the parser to run its `.parse()` method. The program doesn't need to know *how* to parse; the specific child class handles its own logic automatically.
*   **Static Methods:** Sometimes I needed a function that belonged logically to the `Trade` class but didn't need to look at any specific trade's data. For example, verifying if a date string is valid. I used the `@staticmethod` decorator for this.
*   **Magic Methods:** Whenever I wanted to print out a trade or a stock's final position, I didn't want to write a separate print function. Instead, I overrode the `__str__` magic method so that if I just call `print(trade)`, it automatically formats it into a nice, readable sentence in the terminal.

## 3. User Guide
1. Ensure Python 3 is installed along with the `pypdf` library (`pip install pypdf`).
2. Run `python3 main.py` in the terminal.
3. A menu will appear. Select `[1]` for the auto-demo, which parses the 12 generated monthly CSV statements in the `monthly_statements` directory.
4. Select `[2]` to input a custom folder or file path. If reading an encrypted PDF, provide the password when prompted.

## 4. Declaration of External Resources
*   **Libraries:** Python built-in modules (`os`, `csv`, `datetime`); Third-party package `pypdf` for baseline PDF parsing and decryption.
*   **Generative AI:** Large Language Models (AI) were consulted during the brainstorming, architecture structuring, and debugging stages of this project, complying with university guidelines.

## 5. Conclusion and Self-Reflection
**Weaknesses:** Currently, the `PDFParser` uses basic text-containment checks rather than advanced OCR or complex table extraction algorithms (like traversing tabular boundaries). Additionally, average cost calculation is simplified and might not fully reflect complex FIFO/LIFO tax requirements.
**Future Improvements:** Introducing Regex libraries or sophisticated NLP to parse irregular bank PDF tables. Implementing a Graphical User Interface (GUI) utilizing `Tkinter` or `PyQt` would significantly enhance non-technical user accessibility.

## Links & References
*   **GitHub Repository:** [Insert your GitHub Link Here]
*   **5-Minute Intro Video:** [Insert your Video Link Here]

---
## Appendix
*(Place your diagrams, flowcharts, and output screenshots here)*