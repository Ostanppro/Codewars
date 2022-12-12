# https://www.codewars.com/kata/589d5c80c31aa590e300006b

def subsets_parity(n, k):
    return 'EVEN' if ~n & k else 'ODD'