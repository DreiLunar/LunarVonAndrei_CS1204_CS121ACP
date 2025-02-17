def missing_number():
    size = int(input("Enter the size of array: "))

    n = size +1

    print("Enter elements: ")
    arr = [int(input()) for _ in range(size)]

    total_sum = n * (n + 1) // 2
    missing_number = total_sum - sum(arr)

    print(f"missing number: {missing_number}")

missing_number()
