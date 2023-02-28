def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    max_ab = None
    factors_ab = []
    for num in range(max_factor, min_factor-1, -1):
        if max_ab and num * max_factor < max_ab:
            break
        for i in range(num, min_factor-1, -1):
            multiple = num*i
            if str(multiple) == str(multiple)[::-1]:
                if not max_ab:
                    max_ab = multiple
                    factors_ab.append([num, i])
                elif multiple > max_ab:
                    max_ab = multiple
                    factors_ab = [[num, i]]
                elif multiple == max_ab:
                    factors_ab.append([num, i])
    return(max_ab, factors_ab)

def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    min_ab = None
    factors_ab = []
    for num in range(min_factor, max_factor+1):
        if min_ab and num * min_factor > min_ab:
            break
        for i in range(num,max_factor+1):
            multiple = num*i
            if str(multiple) == str(multiple)[::-1]:
                if not min_ab:
                    min_ab = multiple
                    factors_ab.append([num, i])
                elif multiple < min_ab:
                    min_ab = multiple
                    factors_ab = [[num, i]]
                elif multiple == min_ab:
                    factors_ab.append([num, i])
    return(min_ab, factors_ab)

'''
More Optimized Approach reducing further iterations:


'''
