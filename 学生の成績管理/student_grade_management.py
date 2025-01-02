print('学生数を入力してください')
n = int(input())

students = []

for i in range(n):
    print('学生名を点数を入力してください')
    name, score = input().split(',')
    students.append({"name" : name.strip() , "score" : int(score.strip())})


max_point_student_info = students[0]
min_point_student_info = students[0]
total_score = 0

for student in students:
    total_score += student["point"]
    if student["point"] > max_point_student_info["point"]:
        max_point_student_info = student
    if student["point"] < min_point_student_info["point"]:
        min_point_student_info = student

average_score = total_score / n
print(f'全学生の点数の平均: {average_score:.2f}')
print(f'最高点: {max_point_student_info["name"]} ({max_point_student_info["point"]})')
print(f'最低点: {min_point_student_info["name"]} ({min_point_student_info["point"]})')