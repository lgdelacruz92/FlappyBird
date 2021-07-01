def collide(rect1, rect2):


    x1 = rect1[0]
    y1 = rect1[1]
    w1 = rect1[2]
    h1 = rect1[3]

    x2 = rect2[0]
    y2 = rect2[1]
    w2 = rect2[2]
    h2 = rect2[3]

    return not (x1 + w1 < x2 or x1 > x2 + w2 or y1 + h1 < y2 or y1 > y2 + h2)