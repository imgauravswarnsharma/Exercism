def score(x, y):
    x = abs(x)
    y = abs(y)
    distance = ((x**2)+(y**2))**(1/2)
    if distance>=0 and distance<=1:
        return 10
    if distance>1 and distance<=5:
        return 5
    if distance>5 and distance<=10:
        return 1
    if distance>10:
        return 0