

def hamming_distance(num1, num2):
    count = 0
    if len(num1) != len(num2):
        raise ValueError ("Both vectors must be the same length.")
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            count +=1
    return count

def hamming_weight(number):
    count = 0
    num_0 = ""
    for _ in range(len(number)):
        num_0+= "0"
    for i in range(len(number)):
        if number[i] != num_0[i]:
            count+=1
    return count



print(hamming_weight("110111"))