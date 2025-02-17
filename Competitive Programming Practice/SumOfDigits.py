def sum_of_digits(n):
    return sum(int(digits) for digits in str(n))

if __name__ == "__main__":
    n = int(input("Enter N: "))
    print (f"Sum of digits: ", sum_of_digits(n))