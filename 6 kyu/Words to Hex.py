# https://www.codewars.com/kata/596e91b48c92ceff0c00001f

def words_to_hex(words):
    wo = words.split()
    res = []
    for i in wo:
        s ='#'
        for j in range(3):
            if j < len(i):
                a = i[j]                    
                s += hex(ord(a))[2:]
            else:
                s += '00'

        res.append(s)
    return res