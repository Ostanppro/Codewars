# https://www.codewars.com/kata/579e646353ba33cce2000093

def to_brainfuck(s):
    lst = [""]*len(s)
    ans = ">"
    for i in s:
        ans += "+"*ord(i)
        ans += "."
        ans += ">"
    return ans