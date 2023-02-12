def convert(number):
    result = ""
    if number%3!=0 and number%5!=0 and number%7!=0:
        return str(number)
    else:
        if not number%3:
            result+='Pling'
        if not number%5:
            result +='Plang'
        if not number%7:
            result += 'Plong'
        return result
