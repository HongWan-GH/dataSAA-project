# Smart Inventory Management System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

A simple yet powerful inventory management system built with Python, demonstrating core Object-Oriented Programming (OOP) concepts including encapsulation, inheritance, polymorphism, and modular design.

## 📌 Features

- Manage products with different categories (Electronics, Food, General)
- Add, remove, search products by ID or name
- Categorize products automatically
- Extensible class hierarchy for new product types
- Clean separation of concerns with multiple modules

## 🧱 OOP Concepts Demonstrated

- **Encapsulation**: Private attributes with getters/setters (`_product_id`, `_price`, etc.)
- **Inheritance**: `ElectronicProduct` and `FoodProduct` inherit from `Product`
- **Polymorphism**: Overridden `get_info()` method in subclasses
- **Modularity**: Code split into `product.py`, `category.py`, `inventory.py`, `main.py`

## 🚀 How to Run

1. Ensure you have Python 3.8+ installed.
2. Clone this repository and navigate to the `Task1` folder.
3. Run the main script:
   ```bash
   python main.py
