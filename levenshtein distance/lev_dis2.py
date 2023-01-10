# Implement a function called get_similar() that, given a snippet of a user-entered word, will return the top 5 suggestions from our words database in the form of a list as shown below.


words = [
    'friend',
    'friends',
    'friendship',
    'fry',
    'data',
    'database',
    'data science'
    'big data',
    'data cleaning',
    'database',
    'date'
]
def lev(a, b):
 
    if len(b) == 0:
        return len(a)
 
    if len(a) == 0:
        return len(b)
 
    if a[0] == b[0]:
        return lev(a[1:], b[1:])
 
    residual = 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))
 
    return residual

def get_similar(word):
    result = []
    for i in words:
        r= lev(word, i)
        result.append((i, r))
    return sorted(result, key = lambda x : x[1])[0:5]


get_similar('dat')


