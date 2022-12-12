# https://www.codewars.com/kata/584dee06fe9c9aef810001e8

def green(n):
    if n==1:return n
    a,b,m,p=5,6,3,10
    while m<n:
        c=pow(a,2,p)
        d=p+1-c
        a,b,p,m=c,d,p*10,m+2-(a==c)-(b==d)
    return max(a,b) if m==n else min(a,b)