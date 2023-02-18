def sum_of_multiples(limit, multiples):
    sum_limit = 0
    for i in range(1,limit):
        for num in range(len(multiples)):
            try:
                if i%multiples[num]==0:
                    sum_limit += i
                    break
            except ZeroDivisionError:
                continue
    return sum_limit

'''
Alternate more efficient approach wrt Time Complexity:

def sum_of_multiples(limit, multiples):
    sum_set = set()
    for num in multiples:
        try:
            for i in range(num,limit,num):
                sum_set.add(i)
        except ValueError:
            continue

    return sum(sum_set)

'''