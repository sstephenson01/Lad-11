d = ["amy", "adle", "susie"]

def invert_dict(x):
    name_dict = dict()
    for item in d:
        if item[0] in name_dict:
            return name_dict
        else:
            name_dict.append(item[0])
    for key in name_dict:
        val = name_dict[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


a = invert_dict(d)
print(a)
