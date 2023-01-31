# Find target number in array

def find_num(cust_input, target):
    cust_input.sort()
    target_index = []
    for index, i in enumerate(cust_input):
        if i == target:
            target_index.append(index)
    if len(target_index)==1:
        return [target_index[0]]

    return([min(target_index), max(target_index)])

a = find_num([10,11,11,11,14,15], 11)
print(a)