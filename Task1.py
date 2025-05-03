# Create a Dictionary of Student Marks .

students_marks={
                "John":80,
                "Sandip":95,
                "Sunny":90,
                "Alice":85
                }

s_name=input("Enter the student's name:").strip().capitalize()

if s_name in students_marks:
    print(f"{s_name}'s marks are {students_marks[s_name]}")

else:
    print("Student not found")
    