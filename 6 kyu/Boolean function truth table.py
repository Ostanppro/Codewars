# https://www.codewars.com/kata/5e67ce1b32b02d0028148094

def param_count(f):
    n = 1
    while True:
        try:
            f(*[1]*n)
            return n
        except:
            n += 1
            
def truth_table (f):
    nargs = param_count(f)
    abc = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:nargs]]
    fname = "f" if f.__name__ == "<lambda>" else f.__name__
    res = f'{" ".join(abc)}\t\t{fname}({",".join(abc)})\n\n'
    arg = 0
    mx = 2 ** nargs
    
    while arg < mx:
        a = bin(arg)[2:].zfill(nargs)
        b = map(int, a)
        res += f'{" ".join([*a])}\t\t{int(f(*b))}\n'
        arg += 1
    return res