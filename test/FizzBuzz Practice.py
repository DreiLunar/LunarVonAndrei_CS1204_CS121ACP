while True:
    # Input Number
    Number = int(input("Enter a number: "))

    # FizzBuzz counter
    if Number % 3 == 0 and Number % 5 == 0:
        print("FizzBuzz")

    # Fizz counter
    elif Number % 3 == 0:
        print("Fizz")

    # Buzz counter
    elif Number % 5 == 0:
        print("Buzz")

    # Number
    else:
        print(Number)