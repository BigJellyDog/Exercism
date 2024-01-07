def equilateral(sides):
    a = sides[0], b = sides[1], c = sides[2]
    if a > 0 and b > 0 and c > 0:
        return a == b == c


def isosceles(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a == b or a == c or b == c


def scalene(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return a != b and b != c