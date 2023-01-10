# The Levenshtein distance is a measure of the dissimilarity of finite strings. The Levenshtein distance between two finite strings is the smallest number of simple operations that lead one string to another. We will call a simple operation on a finite string of characters:
# inserting a new character into a string
# remove a character from a string
# replace a character in a string with another character
# This measure is used in information processing, processing data in the form of symbol strings, in machine speech recognition, DNA analysis, plagiarism recognition or spelling correction

def lev(a, b):
 
    if len(b) == 0:
        return len(a)
 
    if len(a) == 0:
        return len(b)
 
    if a[0] == b[0]:
        return lev(a[1:], b[1:])
 
    residual = 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))
    return residual

print(lev("pythonxx", "cython"))