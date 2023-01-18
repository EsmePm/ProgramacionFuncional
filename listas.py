
def func():
    """
    numbers = []
    numbers.append(i**2)
    list comprehentions
    """

    t = (('Carlos', [7.7, 6.6, 8.9], 19, 'H'),
         ('Anabel', [8.1, 8.8, 7.9], 18, 'M'),
         ('Octavio', [7.9, 8.9, 6.9], 17, 'H'),
         ('Angel', [7.7, 6.6, 8.9], 16, 'H'),
         ('Denisse', [7.7, 6.6, 8.9], 21, 'M'))         

    students = [ i for i in t if sum(i[1])/len(i[1]) >6]
    print(students)

if __name__ == '__main__':
    func()