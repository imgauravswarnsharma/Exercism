def abbreviate(words):
    abbreviation = ""
    words = words.replace("-", " ")
    list_w = words.split(" ")

    for char in list_w:
        if char:
            if char[0].isalpha():
                abbreviation +=char[0].upper()
            else:
                abbreviation +=char[1].upper()
                
    return abbreviation