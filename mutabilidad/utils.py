from statistics import mean

def tail(x):
    return x[1:]

#Función para ordenar por nombre de forma ascendente
def nameAsc(students):
    l = list(students)
    l = tail(l)
    students_by_asc = sorted(l)
    students = tuple(students_by_asc)
    return students

#Función para ordenar por nombre de forma descendente
def nameDesc(students):
    l = tuple(students)
    u = l[:4] + l[4+1:]
    students_by_desc = sorted(u, reverse=True)
    students = tuple(students_by_desc)
    return students

#Función para ordenar por promedio
def prom(students):
    l = [i for i in students if mean(i[1]) >= 6.0]
    students_by_prom = tuple(l)
    return students_by_prom

#Función para ordenar por edad de forma ascendente
def ageAsc(students):
    l = list(students)
    students_by_age_asc = sorted(l, key= lambda student: student[2])
    students = tuple(students_by_age_asc)
    return students

#Función para ordenar por edad de forma descendente
def ageDesc(students):
    l = list(students)
    students_by_age_desc = sorted(l, key= lambda student:student[2], reverse=True)
    students = tuple(students_by_age_desc)
    return students