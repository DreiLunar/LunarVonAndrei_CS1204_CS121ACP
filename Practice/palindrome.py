def is_palindrome(n):
    convert = str(n)
    if convert == convert[::-1]:
        return "is a palindrome"
    else:
        return "is not a palindrome"

num = int(input("Enter number: "))
print(f"{num} {is_palindrome(num)}")