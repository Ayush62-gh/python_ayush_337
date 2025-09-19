student = {
    "name": "ayush",
    "roll_no": "2400320100337",
    "branch": "CSE"
}
print("student name " + student["name"])
print("student roll number is " + student["roll_no"])
print("student branch is "+student["branch"])

student["year"] = "1st Year"
student["course"] = "Computer Science"

print("\nUpdated Dictionary:")
for key, value in student.items():
    print(key, ":", value)