def product(s):
    a1 = 0
    a2 = 0
    for i in s:
        if i == '!':
            a1 += 1
        elif i == '?':
            a2 += 1
    return a1 * a2