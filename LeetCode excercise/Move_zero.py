#Move all zeros in unsorted array

array = [0,1,0,3,12]
new_arr = []
count = array.count(0)
for i in array:
    if i != 0:
        new_arr.append(i)
for _ in range(count):
    new_arr.append(0)

print(new_arr)
