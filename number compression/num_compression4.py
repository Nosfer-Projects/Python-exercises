# Implement a function called decompress() that converts the result of the compression back to a number.
# [IN]: decompress('14_53_22_51_02')
# [OUT]: 111155522500

def decompress(main_string):
    list_nums = main_string.split("_")
    number = []
    print(list_nums)
    for i in list_nums:
        new = i[0] * int(i[1])
        number.append(new)
    return("".join(number))


print(int(decompress('14_53_22_51_02')))
