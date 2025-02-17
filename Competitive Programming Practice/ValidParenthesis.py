def is_valid_brackets(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != bracket_pairs[char]:
                return "NO"
    return "YES" if not stack else "NO"

#user input
s =  input("Enter S: ")
result = is_valid_brackets(s)
print("Result:", result)