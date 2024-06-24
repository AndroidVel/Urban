grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}

students_grades = {}
students_list = sorted(list(students))

for i in range(0, len(students_list)):
    students_grades[students_list[i]] = sum(int(j) for j in grades[i].split()) / len(grades[i].split())

print(students_grades)

