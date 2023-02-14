def value(colors):
    s = ""
    list_x = ["black", "brown", "red", "orange", "yellow","green","blue", "violet", "grey", "white"]
    for i in range(2):
        s += str(list_x.index(colors[i]))
    return int(s)