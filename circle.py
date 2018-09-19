from math import*


def checkio(data):
    x1 = int(data[1])
    y1 = int(data[3])
    x2 = int(data[7])
    y2 = int(data[9])
    x3 = int(data[13])
    y3 = int(data[15])
    a = 1
    if x1 != x2:
        if y1 != y2:
            k1 = (x2 - x1) / (y1 - y2)
            b1 = (y2**2 - y1**2 + x2**2 - x1**2) / (2 * (y2 - y1))
        else:
            a = 0

        if x1 != x3:
            if y1 != y3:
                k2 = (x3 - x1) / (y1 - y3)
                b2 = (y3**2 - y1**2 + x3**2 - x1**2) / (2 * (y3 - y1))
            else:
                a = 0
        else:
            if y3 != y2:
                k2 = (x2 - x3) / (y3 - y2)
                b2 = (y2**2 - y3**2 + x2**2 - x3**2) / (2 * (y2 - y3))
            else:
                a = 0

        if a:
            xr = (b1 - b2) / (k2 - k1)
            yr = k1 * xr + b1
            r = (x1 - xr) ** 2 + (y1 - yr) ** 2
            r = sqrt(r)
        elif y1 == y2:
            xr = (x1 + x2) / 2
            yr = k2 * xr + b2
            r = (x1 - xr) ** 2 + (y1 - yr) ** 2
            r = sqrt(r)
        elif y1 == y3:
            xr = (x1 + x3) / 2
            yr = k1 * xr + b1
            r = (x1 - xr) ** 2 + (y1 - yr) ** 2
            r = sqrt(r)
        else:
            xr = (x3 + x2) / 2
            yr = k1 * xr + b1
            r = (x2 - xr) ** 2 + (y2 - yr) ** 2
            r = sqrt(r)
    else:
        k1 = (x3 - x1) / (y1 - y3)
        b1 = (y3**2 - y1**2 + x3**2 - x1**2) / (2 * (y3 - y1))
        k2 = (x2 - x3) / (y3 - y2)
        b2 = (y2**2 - y3**2 + x2**2 - x3**2) / (2 * (y2 - y3))
        xr = (b1 - b2) / (k2 - k1)
        yr = k1 * xr + b1
        r = (x1 - xr) ** 2 + (y1 - yr) ** 2
        r = sqrt(r)
        
    if int(yr) == yr:
        yr = int(yr)
    else:
        yr = round(yr, 2)
        if int(yr) == yr:
            yr = int(yr)
    if int(xr) == xr:
        xr = int(xr)
    else:
        xr = round(xr, 2)
        if int(xr) == xr:
            xr = int(xr)
    if int(r) == r:
        r = int(r)
    else:
        r = round(r, 2)
        if int(r) == r:
            r = int(r)
    # replace this for solution
    return "(x-{})^2+(y-{})^2={}^2".format(xr, yr, r)

# These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio("(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio("(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
