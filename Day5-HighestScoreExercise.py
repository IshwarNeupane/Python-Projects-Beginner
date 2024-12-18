#Write a program that generates the highest score from the list of available scores using for loop.
student_scores=input("Enter a list of student scores").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"The highest score in the class is: {highest_score}")
#Maximum score can be done by max function too i.e. print(max(student_scores))
#Similarly, for minimum score, print(min(student_scores))