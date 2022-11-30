# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res