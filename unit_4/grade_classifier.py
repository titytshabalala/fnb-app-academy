""""
Build a grade classifier:
Take learner's:
1. Name
2. Marks for 3 Subjects (Math, Science, English)
3. Calculate the Average
4. Assign a Grade & a status (Pass/Fail)
5. Display Full report card.

Note: Program must correctly use conditionals for all grade and status logic.
"""

# gather the learner's name to record who's marks we collecting
learner_name = input("Enter the learner's name: ").title().strip()

math_marks = float(input(f"Enter the {learner_name}'s marks for Mathematics: "))
science_marks = float(input(f"Enter the {learner_name}'s marks for Science: "))
eng_marks = float(input(f"Enter the {learner_name}'s for English: "))

average_result = (math_marks + science_marks + eng_marks) / 3

status = "Pass"
grade = ""

if average_result < 50:
    status = "Fail"
    grade = "F"
    print(f"Intervention needed!\n")
elif average_result >= 50 and average_result < 60:
    grade = "D" 
    status
elif average_result >=60 and average_result < 70:
    grade = "C"
    status
elif average_result >=70 and average_result <80:
    grade = "B"
    status
elif average_result >=80:
    if average_result > 100:
        print(f"Results sent for review!")
    else:
        grade = "A"
        status


learner_marks ={
    'name' : learner_name,
    'maths': math_marks,
    'science': science_marks,
    'english': eng_marks,
    'average': round(average_result,2),
    'passing_grade': grade,
    'status': status
}


for key, value in learner_marks.items():
    print(f'{key}:\t{value}')
