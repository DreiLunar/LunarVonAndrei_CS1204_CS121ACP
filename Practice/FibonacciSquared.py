def squared_fibonacci_nth(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a ** 2

# Example usage
n = 10
print(squared_fibonacci_nth(n))  # Output: 121

def squared_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a +b
    return a ** 2

n = int(input("Enter the nth term: "))

print(f"The squared fibonacci is: {squared_fibonacci()}")
