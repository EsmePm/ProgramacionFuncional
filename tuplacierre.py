from statistics import mean 

def cierre(t):
    def x(s):
        d = tuple(i for i in t if i[3]==s)
        print(d)
    return x
    
def addn(t):
    c = map(lambda x : mean(x[1]), t)
    def p():
        s = tuple((i, c) for i in t for i in c)
        print(s)
    return p     

if __name__ == '__main__':
    t = (('Carlos', [7.7, 6.6, 8.9], 19, 'H'),
            ('Anabel', [8.1, 8.8, 7.9], 18, 'M'),
            ('Octavio', [7.9, 8.9, 6.9], 17, 'H'),
            ('Angel', [7.7, 6.6, 8.9], 16, 'H'),
            ('Denisse', [7.7, 6.6, 8.9], 21, 'M')) 
    fn = cierre(t)
    fn('M')

    fn = addn(t)
    fn()