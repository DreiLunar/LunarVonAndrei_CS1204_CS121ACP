def get_union(convert_1, convert_2):
    union = convert_1.union(convert_2)
    return union
def get_intersection(convert_1, convert_2):
    intersection = convert_1.intersection(convert_2)
    return intersection

set_1 = input("Enter set 1: ")
set_2 = input("Enter set 2: ")
convert_1 = set(map(int, set_1.split()))
convert_2 = set(map(int, set_2.split()))

print(f"The union of set 1 and set 2 is: {get_union(convert_1, convert_2)}")
print(f"The intersection of set 1 and set 2 is: {get_intersection(convert_1, convert_2)}")