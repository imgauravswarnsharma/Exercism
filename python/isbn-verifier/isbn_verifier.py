def is_valid(isbn):
    if len(isbn)>=10:
        count = 10
        test = 0
        lst_index = len(isbn) -1
        lst_elmnt = isbn[len(isbn) -1]
        for element in range(lst_index):
            if isbn[element].isalpha():
                return False
            if isbn[element].isnumeric():
                test += int(isbn[element])*count
                count -=1
        if not(lst_elmnt.isnumeric() or lst_elmnt == 'X'):
            return False
        elif lst_elmnt == 'X':
            test += 10
        else:
            test +=int(lst_elmnt)

        if test % 11 ==0:
            return True
        return False
    else:
        return False

    '''
    Alternate Solution:

    def is_valid(isbn):
    nums = list(isbn.replace("-", ""))
    if len(nums)!=10: return False
    if nums[-1] == "X": nums[-1] = "10"
    if not all([c.isdigit() for c in nums]): return False
    return sum(int(x)*y for x,y in zip(nums, range(10, 0, -1)))%11 == 0

    '''