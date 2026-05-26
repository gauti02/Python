# def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
items = [
    {"name": "Notebook", "price": 250, "category": "Stationery"},
    {"name": "Pen", "price": 100, "category": "Stationery"},
    {"name": "Bag", "price": 1200, "category": "Accessories"},
    {"name": "Bottle", "price": 400, "category": "Utensils"},
]

affordable_items = [items["name"] for items in items if items["price"] < 500]
print(affordable_items)
unique_categories = {items["category"] for items in items}
print(unique_categories)
name_price_mapping = {items["name"]: items["price"] for items in items}
print(name_price_mapping)
prices = (items["price"]*0.9 for items in items)
print(prices)
#combine all above in tuples
result = (affordable_items, unique_categories, name_price_mapping, list(prices))
print(result)