# https://www.codewars.com/kata/5fad08d083d5600032d9edd7

get_ = lambda s: lambda cb: (f := lambda v: cb(v) if isinstance(v, int) else (cb(s[v]) if isinstance(v, str) else get_(s)(lambda x: f(v(x)))))
start = lambda nx: nx({})
return_ = lambda s: get_(s)(lambda v: v)
let = lambda s: lambda n: get_(s)(lambda v: lambda nx: nx({**s, **{n:v}}))
add = lambda a: lambda b: a + b
sub = lambda a: lambda b: a - b
mul = lambda a: lambda b: a * b
div = lambda a: lambda b: a // b