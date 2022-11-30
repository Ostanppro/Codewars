# https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

def sum_arrays(array1,array2):
    
    def convert(arr):
        return int(''.join(str(el) for el in arr)) if arr else 0
    
    div = convert(array1) + convert(array2)
    res = [int(el) for el in str(abs(div))] if array1 or array2 else []
    
    if div < 0:
        res[0] = - res[0]
    
    return res