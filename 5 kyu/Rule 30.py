# https://www.codewars.com//kata/5581e52ac76ffdea700000c1

def rule30(a, n):
    for _ in range(n):
        a = [int(0 < 4*x + 2*y + z < 5) for x, y, z in
                zip([0, 0] + a, [0] + a + [0], a + [0, 0])]
    return a