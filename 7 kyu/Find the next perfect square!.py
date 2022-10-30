def find_next_square(sq):
    num = sq**(0.5)
    if num % 1 == 0:
        return (num+1)**2
    return -1