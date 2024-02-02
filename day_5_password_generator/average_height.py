student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = int(sum(student_heights))

print(f"total height = {total_height}")
print(f"number of students = {n + 1}")
print(f"average height = {int(total_height / (n + 1))}")