#Find numbers of right versions

def right_ver(list_intput, bad_version):
    list_intput = [num for num in range(1,11)]
    return [num for num in list_intput if num < bad_version]

a = right_ver(10, 3)
print(a)