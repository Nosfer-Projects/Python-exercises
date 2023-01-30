#Move all zeros in unsorted array

array = [0,1,0,3,12]
#1 solve
new_arr = []
count = array.count(0)
for i in array:
    if i != 0:
        new_arr.append(i)
for _ in range(count):
    new_arr.append(0)


#2 solve

for i in array:
    if i == 0:
        idx = array.index(i)
        array.pop(idx)
        array.append(i)

print(array)