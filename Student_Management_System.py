students = {}

welcome = """
========================================
      STUDENT MANAGEMENT SYSTEM
========================================

Welcome to Student Management System
"""

menu = """
============== MENU ==============

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Exit
"""

def display_student(roll, details):
    print("\nStudent Details")
    print("-" * 30)
    print("Name :", details["Name"])
    print("Roll Number :", roll)
    print("Branch :", details["Branch"])
    print("Phone Number :", details["Phone Number"])
    print("Address :", details["Address"])

def add_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        print("Student Already Exists!")
        return

    name = input("Enter Name : ")
    branch = input("Enter Branch : ")
    phone = input("Enter Phone Number : ")
    address = input("Enter Address : ")

    students[roll] = {
        "Name": name,
        "Branch": branch,
        "Phone Number": phone,
        "Address": address
    }

    print("\nStudent Added Successfully!")
    display_student(roll, students[roll])

def view_students():
    if len(students) == 0:
        print("No Student Found.")
    else:
        for roll, details in students.items():
            display_student(roll, details)
            print("-" * 30)

def search_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        display_student(roll, students[roll])
    else:
        print("Student Not Found.")

def update_student():
    roll = input("Enter Roll Number : ")

    if roll in students:
        print("Enter New Details")

        students[roll]["Branch"] = input("Enter Branch : ")
        students[roll]["Phone Number"] = input("Enter Phone Number : ")
        students[roll]["Address"] = input("Enter Address : ")

        print("\nStudent Updated Successfully!")
        display_student(roll, students[roll])

    else:
        print("Student Not Found.")

print(welcome)

while True:
    print(menu)

    try:
        choice = int(input("Choose Your Option : "))
    except ValueError:
        print("Invalid Choice.")
        continue

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")