# main.py
from models.product import Product, ElectronicProduct, FoodProduct
from models.inventory import Inventory

def main():
    # 创建库存系统实例
    inv = Inventory()

    # 创建不同产品
    p1 = Product("P001", "普通商品", 29.9, 100)
    p2 = ElectronicProduct("E001", "智能手机", 5999, 50, warranty_months=24)
    p3 = FoodProduct("F001", "牛奶", 15.5, 200, expiry_date="2026-04-01")

    # 添加到库存
    inv.add_product(p1, category_name="杂货")
    inv.add_product(p2, category_name="电子产品")
    inv.add_product(p3, category_name="食品")

    # 打印所有产品
    print("所有产品：")
    for info in inv.get_all_products():
        print("  ", info)

    # 搜索测试
    print("\n搜索 '手机'：")
    results = inv.search_by_name("手机")
    for r in results:
        print("  ", r)

    # 按ID查询
    print("\n查询 ID 'F001'：")
    prod = inv.search_by_id("F001")
    if prod:
        print("  ", prod.get_info())

    # 演示多态：调用不同子类的 get_info()
    print("\n多态演示：")
    products = [p1, p2, p3]
    for p in products:
        print("  ", p.get_info())

if __name__ == "__main__":
    main()
