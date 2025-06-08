students = [("홍길동", 90),("김철수", 85), ("이영희", 95)]
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)