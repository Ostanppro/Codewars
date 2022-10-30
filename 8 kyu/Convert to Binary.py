def to_binary(n):
    r = ''
    while n > 0:
        r = str(n % 2) + r
        n = n // 2
    return int(r)