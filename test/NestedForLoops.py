rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))
sign = input("What you would like to display: ")

for x in range(rows):
    for y in range(columns):
        print(sign, end= "")
    print()
