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

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for numbers in num_pad:
    for elements in numbers:
        print(elements, end=" ")
    print()

for a in fruits:
    print(a)