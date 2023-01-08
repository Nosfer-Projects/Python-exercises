# Implement a function called hamming_distance() that will return the Hamming distance of two vectors. To be able to calculate the Hamming distance, the vectors must be of the same length. If the passed vectors are of different lengths, raise a ValueError with the text 'Both vectors must be the same length.'

def hamming_distance(num1, num2):
    count = 0
    if len(num1) != len(num2):
        raise ValueError ("Both vectors must be the same length.")
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            count +=1
    return count




print(hamming_distance('01101010', '11011011'))