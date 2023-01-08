# Implement a function that will return the number of all three-digit palindromic numbers.


def palin_num():
    count = 0
    for i in range(100,1000):
        i = str(i)
        if i == i[::-1]:
            count += 1
        else:
            continue
    return count

print(palin_num())
