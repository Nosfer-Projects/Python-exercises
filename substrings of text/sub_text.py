# Consider the following problem. We are given a sequence of characters and we want to extract from it all substrings of length n in the order they appear in the sequence.
# For example, from the string 'python' we can extract 3-digit series:
# ['ask', 'yth', 'tho', 'hon']
# or 4-digit:
# ['pyth', 'ytho', 'thon']
# Implement a function called get_slices() that takes two arguments:
# sequence - sequence of characters to be processed
# length - the length of the substrings to be extracted from the sequence


def get_slices(sequence, length):
    if length < 0 :
        raise ValueError ("The length cannot be less than 1.")
    if length > len(sequence):
        raise ValueError ("The length cannot be greater than sequence.")
    return [
        sequence[i : i + length]
        for i in range(len(sequence) - length + 1)
    ]
print(get_slices('esmartdata', 5))