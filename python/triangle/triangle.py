def valid_triangle(sides):
    for i in range(3):
        if sides[i]==0:
            return False
    if sides[0]+sides[1]>= sides[2]:
        if sides[1]+sides[2]>= sides[0]:
            if sides[2]+sides[0]>= sides[1]:
                return True
    return False

def equilateral(sides):
    if valid_triangle(sides) is True:
        if sides[0]==sides[1]==sides[2]:
            return True
    return False

def isosceles(sides):
    if valid_triangle(sides) is True:
        if sides[0]==sides[1] or sides[1]==sides[2] or sides[0] ==sides[2]:
            return True
    return False

def scalene(sides):
    if valid_triangle(sides) is True:
        if sides[0]!=sides[1] and sides[1]!=sides[2] and sides[0] !=sides[2]:
            return True
    return False