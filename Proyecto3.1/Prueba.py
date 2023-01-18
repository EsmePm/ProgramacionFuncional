import csv
from statistics import mean
from typing import Any

def e18(students: list)-> Any:
    def e18b(g: int,j: str)-> Any:
        conjunto13 = set()
        conjunto15 = set()
        conjuntoFinal = set()
        for student in students:
            list_aux = []
            for a in range(5,8):
                list_aux.append(int(student[a]))
            promedio = (lambda x : mean(x))(list_aux)
            if promedio >=  g:
                conjunto13.add(tuple([student[0],student[1],promedio]))
            if student[0] ==  j:
                conjunto15.add(tuple([student[0],student[1],promedio])) 
        conjuntoFinal = conjunto13.symmetric_difference(conjunto13.intersection(conjunto15))
        print(conjuntoFinal)
    return e18b

with open('./exams.csv') as csvfile:
    students = csv.reader(csvfile, delimiter = ',')
    columnas = next(students)
    f = e18(list(students)[1:])
    f(60,'female')
