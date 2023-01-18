def codestr(c):
    return(hex(ord(c)))

h = codestr('a')
print(h)

def compose(f,g):
    def fn(x):
        return f(g(x))
    return fn

codestr2 = compose(hex, ord)