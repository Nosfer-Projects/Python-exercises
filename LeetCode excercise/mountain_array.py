# An exercise to examine the array and see if the array grows up to a certain point and then something like a mountain falls

def mountain(A : list[int]):
    if len(A)< 3:
        return False
    i = 1
    while i<len(A) and A[i] > A[i-1]:
        i +=1
    if i == 1 or i== len(A):
        return False
    
    while i<len(A) and A[i]<A[i-1]:
        i+=1
    
    return i == len(A)
    


print(mountain([1, 2, 5, 4, 3])) 