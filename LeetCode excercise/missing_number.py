# Find missing number

def find_missing_number(input_list):
    input_list.sort()
    complete_list = {num for num in range(max(input_list))}
    return complete_list.difference(input_list)


a = find_missing_number([4,0,1])
print(a)
