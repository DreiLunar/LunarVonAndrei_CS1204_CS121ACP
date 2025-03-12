fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[2][1])

for food in groceries:
    print(food)

for elements in groceries:
    for foods in elements:
        print(foods, end=" ")
    print()