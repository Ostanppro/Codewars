# https://www.codewars.com//kata/5ae43ed6252e666a6b0000a4

def jumbled_string(s, n):
    iterations = [s]
    
    while True:
        s = s[::2] + s[1::2]
        if s == iterations[0]: break
        iterations.append(s)
    
    return iterations[n % len(iterations)]