
# GPA Calculator

num = int(input("أدخل عدد المواد: "))

courses_names = []
courses_grades = []
courses_hours = []

grade_points = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

for i in range(num):
    print("Course:", i + 1)

    name = input("أدخل اسم المادة: ")

    while True:
        try:
            hours = int(input("أدخل عدد الساعات المعتمدة للمادة: "))
            if hours > 0:
                break
            print("يجب أن يكون عدد الساعات أكبر من صفر.")
        except ValueError:
            print("أدخل عددًا صحيحًا للساعات.")

    while True:
        grade = input("أدخل التقدير (A, B, C, D, F): ").strip().upper()

        if grade in grade_points:
            break
        else:
            print("تقدير غير صحيح. اختر A أو B أو C أو D أو F.")

    courses_names.append(name)
    courses_grades.append(grade)
    courses_hours.append(hours)

total_points = 0
total_hours = 0

for i in range(num):
    points = grade_points[courses_grades[i]]
    total_points += points * courses_hours[i]
    total_hours += courses_hours[i]

if total_hours > 0:
    gpa = total_points / total_hours
else:
    gpa = 0.0

print("\n----- GPA Results -----")

for i in range(num):
    print(
        f"{courses_names[i]}: "
        f"{courses_grades[i]} - "
        f"{courses_hours[i]} hours"
    )

print(f"إجمالي الساعات المعتمدة: {total_hours}")
print(f"Total Grade Points: {total_points:.2f}")
print(f"GPA: {gpa:.2f}")

# GPA Calculator

num = int(input("أدخل عدد المواد: "))

courses_names = []
courses_grades = []
courses_hours = []

grade_points = {
    'A': 4.0,
    'B': 3.0,
    'C': 2.0,
    'D': 1.0,
    'F': 0.0
}

for i in range(num):
    print("Course:", i + 1)

    name = input("أدخل اسم المادة: ")

    while True:
        try:
            hours = int(input("أدخل عدد الساعات المعتمدة للمادة: "))
            if hours > 0:
                break
            print("يجب أن يكون عدد الساعات أكبر من صفر.")
        except ValueError:
            print("أدخل عددًا صحيحًا للساعات.")

    while True:
        grade = input("أدخل التقدير (A, B, C, D, F): ").strip().upper()

        if grade in grade_points:
            break
        else:
            print("تقدير غير صحيح. اختر A أو B أو C أو D أو F.")

    courses_names.append(name)
    courses_grades.append(grade)
    courses_hours.append(hours)

total_points = 0
total_hours = 0

for i in range(num):
    points = grade_points[courses_grades[i]]
    total_points += points * courses_hours[i]
    total_hours += courses_hours[i]

if total_hours > 0:
    gpa = total_points / total_hours
else:
    gpa = 0.0

print("\n----- GPA Results -----")

for i in range(num):
    print(
        f"{courses_names[i]}: "
        f"{courses_grades[i]} - "
        f"{courses_hours[i]} hours"
    )

print(f"إجمالي الساعات المعتمدة: {total_hours}")
print(f"Total Grade Points: {total_points:.2f}")
print(f"GPA: {gpa:.2f}")
