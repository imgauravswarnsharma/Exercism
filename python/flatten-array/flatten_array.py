def flatten(x):
    i = 0
    temp_list = []
    while i < len(x):
        if type(x[i]) == list:
            for n in range(len(x[i])):
                if x[i][n] != None:
                    temp_list.append(x[i][n])
        else:
            if x[i] != None:
                temp_list.append(x[i])
        i +=1
    for num in range(len(temp_list)):
        if type(temp_list[num]) == list:
            x = temp_list
            return flatten(x)
    return temp_list

'''
Using same approach as above but
only with for loop and
directly accessing the elements.
Much cleaner than before

def flatten(x):
    i = 0
    temp_list = []
    for iter in x:
        if type(iter) is list:
            for num in iter:
                if num != None:
                    temp_list.append(num)
        else:
            if iter != None:
                temp_list.append(iter)
    for num in temp_list:
        if type(num) is list:
            return flatten(temp_list)
    return temp_list
    '''


'''
Calling function inside for loop itself.
Shortens the code considerably

def flatten(x):
    temp = x
    i = 0
    elem_list = []
    temp_list = []
    for num in x:
        if type(num) == list:
            for temp in flatten(num):
                if temp != None:
                    temp_list.append(temp)
        else:
            if num != None:
                temp_list.append(num)
    return temp_list
    '''
