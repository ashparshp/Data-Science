fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Calculate the sum of all the scores in the list: Using sum()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89, 81, 94, 78, 61]
total_exam_score = sum(student_scores)
print(total_exam_score)

# Calculate the average score of all the scores in the list: Custom function
total_score = 0
for score in student_scores:
    total_score += score
print(total_score)

# Calculate the largest score in the list: Using max()
highest_score = max(student_scores)
print(highest_score)

# Calculate the largest score in the list: Custom function
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(highest_score)

