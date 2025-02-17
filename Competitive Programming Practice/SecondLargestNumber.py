def second_largest_number():
    size = int(input("Enter size of array: "))

    print("Enter elements:")
    arr = [int(input()) for _ in range(size)]

    # Find unique numbers and sort them in descending order
    unique_numbers = sorted(set(arr), reverse = True)

    # Check if a second-largest exists
    if len(unique_numbers) > 1:
        print(f"Result: {unique_numbers[1]}")
    else:
        print("Result: None")


second_largest_number()
