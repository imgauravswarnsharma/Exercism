def is_armstrong_number(number):
    number = str(number)
    n = len(number)
    x = 0
    for digit in range(n):
        x += (int(number[digit]))**n
    if x == int(number):
        print(number)
        return True
    return False