#Show the number of boats needed to take all the people

limit = 4
people = [3,2,1,2]
boats = 0

while people:
    if len(people) == 1:
        boats += 1
        break
    i = people.pop(0)
    if i == 4:
        boats+= 1
    else:
        for j in range(1, len(people)):
            if i + people[j] == 4:
                people.pop(j)
                boats += 1
                break
print(boats)


    