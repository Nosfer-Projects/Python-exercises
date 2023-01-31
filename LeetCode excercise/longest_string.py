# String without repeat
def longest_string(string_input):
    chars = []
    for i in string_input:
        if i in chars:
            break
        else:
            chars.append(i)
    return len(chars)

a = longest_string("abcabcbb")
print(a)