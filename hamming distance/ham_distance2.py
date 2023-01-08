# We will define the weight of a vector u as the Hamming distance of this vector from the zero vector. So in the case of vector '1001001', its weight will be equal to the Hamming distance of vector '1001001' from vector '0000000'.
# Implement a function called hamming_weight() that will return the weight of the vector determined as above. In the solution, you can use the hamming_distance() function. It is also worth noting a slightly simpler implementation. The weight of the vector will be equal to the number of 1's in the vector.

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