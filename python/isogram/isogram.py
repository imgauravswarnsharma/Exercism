def is_isogram(string):
    new_string = ""
    for char in string.lower():
        if ord(char)>=97 and ord(char)<=122:
            new_string +=char
    if len(new_string) == len(set(new_string)):
        return True
    return False