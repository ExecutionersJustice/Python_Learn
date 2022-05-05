from re import I


def find_needle(haystack):
    message = ""
    for i in haystack:
        if i == "needle":
            message = "Found the needle at position "+str(haystack.index(i))
            return message

print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False, 'found the needle at position 3']))

def find_needle2(haystack):
    return f'Found the needle at position {haystack.index("needle")}'