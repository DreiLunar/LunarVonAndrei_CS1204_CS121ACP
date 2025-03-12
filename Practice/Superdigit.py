def get_superdigit(n):
    if n < 10:
        return n
    return get_superdigit(sum(int(digit) for digit in str(n)))

number = int(input("Enter a number more than 9: "))

print (get_superdigit(number))