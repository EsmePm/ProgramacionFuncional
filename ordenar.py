from statistics import mean 

def mean2(students):
    sum = 0
    avg_list = []
    for i in students:
        for j in i[1]:
            sum += j
        avg = sum/len(i[3])
        avg_list.append(avg)
    return avg_list

def mean3(student):
    sum = 0
    for i in student[1]:
        sum += i
        avg = sum/len(student[1])
    return avg

def mean4(grades):
    sum = 0
    for i in grades:
        sum += i
    avg = sum/len(grades)
    return avg

t = (('Carlos', [7.7, 6.6, 8.9], 19, 'H'),
         ('Anabel', [8.1, 8.8, 7.9], 18, 'M'),
         ('Octavio', [7.9, 8.9, 6.9], 17, 'H'),
         ('Angel', [7.7, 6.6, 8.9], 16, 'H'),
         ('Denisse', [7.7, 6.6, 8.9], 21, 'M'))

students = [i[0] for i in t]
student_by_name = sorted(students, reverse=True)
#student_by_mean = sorted(students, key = mean3)
student_by_mean = sorted(students, key = lambda x : mean(x[1]))
student_by_age = sorted(students, key = lambda x : x[2])

print(student_by_name)
print(student_by_mean)
print(student_by_age)