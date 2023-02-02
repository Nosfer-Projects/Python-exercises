# #Show the number of boats needed to take all the people.


def rescue_boats(people: list[int], limit: int) -> int:
    people.sort()
    left = 0
    right= len(people) -1
    boats = 0
    while left <= right:
        if left == right:
            boats +=1
            break
        if people[left] + people[right] <= limit:
            left += 1
        right -=1
        boats +=1


    return boats

print(rescue_boats([3,3,3,4],4))




    