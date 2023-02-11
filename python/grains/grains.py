def square(number):
    if number in range(1,65):
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")

def total():
    i=1
    sum_total = 0
    while i<=64:
        sum_total += square(i)
        i +=1
    return sum_total