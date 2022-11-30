# https://www.codewars.com//kata/57dab71714e53f4bc9000310

def rotate_and_remove(arr):
    while len(arr)>1:
        arr = [popMinMax([*r]) for r in zip(*arr)][::-1]
    return arr[0][0]

def popMinMax(r):
    for f in min,max:
        r.remove(f(r))
    return r