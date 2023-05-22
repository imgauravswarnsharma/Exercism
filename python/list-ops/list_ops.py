def append(list1, list2):
    return list1+list2

def concat(lists):
    list_c = []
    for x in lists:
        if x not in list_c:
            for i in x:
                list_c.append(i)
    return list_c
    


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    result = 0
    for item in list:
        result += 1
    return result


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    while list:
        accumulator = function(accumulator, list.pop(0))
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    while list:
        accumulator = function(accumulator, list.pop())
    return accumulator


def reverse(list):
    reversed_list = []
    while list:
        reversed_list.append(list.pop())
    return reversed_list

