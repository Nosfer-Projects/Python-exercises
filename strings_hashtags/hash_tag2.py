# Implement a function called clean_hashtags() that takes three arguments:
# input_file - file name containing hashtags
# output_file - name of the file to which the cleaned hashtags are to be saved
# length - maximum hashtag length
# The '#' character is not included in the length of the hashtag. For example, the hashtag '#gym' has a length of 3.



def clean_hashtags(text,new_file, length):
    all_tags= []
    with open(text, "r") as file:
        data = file.readlines()
        for i in data:
            i = i.split()
            for x in i:
                all_tags.append(x)
    clear_sorted_tags= sorted(list(set([x for x in all_tags if len(x)<=length +1])))
    with open (new_file, "w") as file:
        for i in clear_sorted_tags:
            file.write(i + "\n")
    with open(new_file, "r") as file:
                for i in file.readlines():
                    print(i)


print(clean_hashtags("hashtags.txt", "new", 5))