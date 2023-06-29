dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

def ltt(dict):
    new_dict = {}
    for key, value in dict.items():
        if value >= 3:
            new_dict[key] = value
    return new_dict

print(ltt(dict))