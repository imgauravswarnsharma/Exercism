def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    sum_num = 0
    if number%2==0:
        n = int((number/2)+1)
    else:
        n = int((number+1)/2)
    for i in range(1,n):
        if number%i ==0:
            sum_num +=i
    if sum_num>number:
        return "abundant"
    if sum_num<number:
        return "deficient"
    return "perfect"
