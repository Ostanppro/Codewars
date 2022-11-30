# https://www.codewars.com//kata/605f4035f38ca800072b6d06

class Function:
    def init(self, f, df):
        self.f = f
        self.df = df
    
    def add(self, other):
        f = lambda x:self.f(x) + other.f(x)
        df = lambda x:self.df(x) + other.df(x)
        return Function(f, df)
    
    def sub(self, other):
        f = lambda x:self.f(x) - other.f(x)
        df = lambda x:self.df(x) - other.df(x)
        return Function(f, df)
    
    def mul(self, other):
        f = lambda x:self.f(x) * other.f(x)
        df = lambda x:self.df(x) * other.f(x) + self.f(x) * other.df(x)
        return Function(f, df)
    
    def truediv(self, other):
        f = lambda x:self.f(x) / other.f(x)
        df = lambda x:(self.df(x) * other.f(x) - self.f(x) * other.df(x)) / other.f(x)**2
        return Function(f, df)
    
    def matmul(self, other):
        f = lambda x:self.f(other.f(x))
        df = lambda x:other.df(x) * self.df(other.f(x))
        return Function(f, df)
    
    def call(self, x, grad=False):
        return (self.f, self.df)[grad](x)