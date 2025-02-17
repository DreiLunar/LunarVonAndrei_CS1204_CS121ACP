#grade input
grade = int(input("Input Grade: "))

#conversion
if grade >= 98 and grade <= 100:
    print("You Got 1.00!")

#palindrome
word = input("Enter a word to check if it's a palindrome: ")
if word == word[::-1]:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

