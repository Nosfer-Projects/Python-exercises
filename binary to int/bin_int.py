# Implement a function called binary_to_int() that reads the included binary.txt file and converts the given numbers to decimal notation. Return the resulting numbers as a list.
# Example of calling the function:
# [IN]: binary_to_int()
# [OUT]: [32293, 44802, 11290, 61820, 19270, 4638, 1749, 10344, 17165, 8129, 31236, 43147, 8728, 17654, 9467

def binary_to_int(file):
    nums = []
    with open (file, "r") as file:
        data = file.read().split("\n")
        for i in data:
            nums.append(int(i, 2))
    print(nums)

binary_to_int("binary.txt")