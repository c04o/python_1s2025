list_students = list()

def add_student():
    student = input("Input their name: ")
    list_students.append(student)

def show_students():
    print("Students:")
    for student in list_students:
        print(student)

while True:
    add_student()
    show_students()
    if input("add a new student? (y/n): ").lower() != "y":
        break

print("Thank you for using the program!")