items = [1, 2, 7, "ram", "josh", 2, 3, "jack", 4, 4, "ram", "smith"]
unique_items = []

for item in items:
    if item not in unique_items:
        unique_items.append(item)

print(unique_items)
