# category.py
from typing import List
from .product import Product

class Category:
    """类别类，包含多个产品"""
    def __init__(self, name: str, description: str = ""):
        self._name = name
        self._description = description
        self._products: List[Product] = []      # 组合关系

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def add_product(self, product: Product):
        self._products.append(product)

    def remove_product(self, product_id: str):
        self._products = [p for p in self._products if p.product_id != product_id]

    def list_products(self):
        return [p.get_info() for p in self._products]

    def __str__(self):
        return f"类别: {self._name}, 产品数量: {len(self._products)}"
