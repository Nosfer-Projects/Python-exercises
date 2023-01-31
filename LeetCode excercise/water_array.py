# Calculate bigest area in array


def max_calculate_area(height):
    max_area = 0
    l = 0
    r = len(height)-1

    while(l<r):
        max_area = max(max_area, min(height[l], height[r]) * (r-l))
        if height[l]<height[r]:
            l+=1
        else:
            r-=1

    return max_area

a = max_calculate_area([2,1,1,2])
print(a)