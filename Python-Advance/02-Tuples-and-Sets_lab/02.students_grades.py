students_number = int(input())
students_and_grades = {}

for num in range(students_number):
    student, grade = input().split(' ')

    if student not in students_and_grades.keys():
        students_and_grades[student] = []

    students_and_grades[student].append(float(grade))

for student, grade in students_and_grades.items():
    ave_grade = sum(grade) / len(grade)
    grade_p = [f'{grade[x]:.2f}' for x in range(len(grade))]
    print(f"{student} -> {' '.join(grade_p)} (avg: {ave_grade:.2f})")
