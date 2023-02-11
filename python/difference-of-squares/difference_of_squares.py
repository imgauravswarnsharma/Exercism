def square_of_sum(number):
    sum_x = 0
    for i in range(1,number+1):
        sum_x += i
    return sum_x**2

def sum_of_squares(number):
    sum_x_square = 0
    for i in range(1,number+1):
        sum_x_square +=i**2
    return sum_x_square

def difference_of_squares(number):
    diff_x = square_of_sum(number) - sum_of_squares(number)
    return diff_x
