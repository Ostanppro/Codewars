# https://www.codewars.com//kata/59b166f0a35510270800018d

def find_area(points):
    return sum((p2.X - p1.X) * (p1.Y + p2.Y) / 2 for p1, p2 in zip(points, points[1:]))