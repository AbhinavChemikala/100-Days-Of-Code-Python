# Calculate the highest score in a list
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

score_high = 0
for score in student_scores:
    if score > score_high:
        score_high = score

print(f"The highest score in the class is: {score_high}")

# Another way to do this is to use the max() method.
print(max(student_scores))
# To get min, use min()
print(min(student_scores))