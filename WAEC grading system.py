exam_score=int(input("Enter your exam score"))
if exam_score < 0 or exam_score > 100:
    print("Invalid score")
elif exam_score>= 80:
     print("Grade: A")
elif exam_score >= 70:
    print("Grade: B")
elif exam_score >= 60:
    print("Grade: C")
elif exam_score >= 50:
    print("Grade: D")
elif exam_score >= 40:
    print("Grade: E")
else :
    print("Grade: F")

