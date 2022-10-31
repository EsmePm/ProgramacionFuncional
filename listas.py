def func():
    t = (('Carlos', [7.7, 6.6, 8.9], 19, 'H'),
         ('Anabel', [8.1, 8.8, 7.9], 15, 'M'),
         ('Octavio', [5.9, 4.9, 5.9], 17, 'H'),
         ('Angel', [7.7, 6.6, 8.9], 16, 'H'),
         ('Denisse', [7.7, 6.6, 8.9], 21, 'M'))
    
    students = [ i for i in t if i[2] >= 18]  #mayor de 18
    #students = [ i for i in t if i[2] >= 18 and i[3]=='M']    #mujer
    #students = [ i for i in t if sum(i[1])/len(i[1]) > 6]
    print(students)

if __name__ == '__main__':
    func()