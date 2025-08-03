# Given the names and grades for each student in a class of  students,
# store them in a nested list
# and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])

    lowest = students[0][1]
    second_lowest = None

    for student in students:
        if student[1] > lowest:
            second_lowest = student[1]
            break

    names = []
    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    names.sort()
    for name in names:
        print(name)
