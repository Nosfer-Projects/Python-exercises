# Implement a function that returns a prime number in the 100th position.

def is_prime():   
    list_nums= []
    for i in range(1000):
        if i < 2:
            continue
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
        if flag:
            list_nums.append(i)
        if len(list_nums) == 100:
            return list_nums[-1]




print(is_prime())