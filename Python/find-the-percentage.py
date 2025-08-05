# Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Input Format
# The first line contains the integer , the number of students' records.
# The next  lines contain the names and marks obtained by a student, each value separated by a space.
# The final line contains query_name, the name of a student to query.

# Output Format

# Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    for key, value in student_marks.items():
        if key == query_name:
            average = sum(value) / 3
            print(f"{average:.2f}")
