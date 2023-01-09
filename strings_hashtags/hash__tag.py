# Implement a function called clean_hashtags() that will read the included hashtags.txt file and do some hashtag cleaning. Cleaning consists in leaving hashtags with a maximum length of 4 characters. The '#' character is not included in the length of the hashtag. For example, the hashtag '#gym' has a length of 3.

# Also, make sure to remove duplicates if there are any. Then return the cleaned and alphabetically sorted hashtags as a list






def clean_hashtags(text):
    all_tags= []
    with open(text, "r") as file:
        data = file.readlines()
        for i in data:
            i = i.split()
            for x in i:
                all_tags.append(x)
    return sorted(list(set([x for x in all_tags if len(x)<=5])), key= lambda x: x[1])

print(clean_hashtags("hashtags.txt"))