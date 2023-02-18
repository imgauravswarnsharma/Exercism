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