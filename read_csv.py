import csv

def read_csv(name_file):
    with open(name_file) as csvfile:
        list_students = []
        students = csv.reader(csvfile, delimiter=',')
        h = next(students)
        for student in students:
            iterador = zip(h,student)
            list_students.append({clave: valor for clave, valor in iterador})
        return list_students

if __name__=='__main__':
    l = read_csv('./arch.csv')
    print(l)