def print_table():
    numbers = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]

    for row in range(5):
        if row == 0:
            print("+---+---+---+---+---+")

        separator = "|"
        for column in range(5):
            separator += f" {numbers[row][column]:2}|"
        print(separator)

        print("+---+---+---+---+---+")

print_table()