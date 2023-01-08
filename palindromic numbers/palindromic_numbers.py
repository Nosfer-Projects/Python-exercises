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
