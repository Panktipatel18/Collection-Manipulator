# ========================================
# Student Data Organizer
# Collection Manipulator Project
# ========================================

print("=" * 50)
print(" WELCOM TO STUDENT DATA ORGANIZER")
print("=" * 50)
print("This program allows you to:")
print("1. Add Student")
print("2. Display All Students")
print("3. Update Student")
print("4. Delete Student")
print("5. Display Subjects Offered")
print("6. Exit")

students = []
student_dict = {}
subjects_set = set()

# --------------------------------------
# Add Student
# --------------------------------------
def add_student():
    sid = input("Enter Student ID: ")

    if sid in student_dict:
        print("Student ID Already exists!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    grade = input("Enter Grade: ")
    dob = input("Enter Date Of Birth (YYYY-MM-DD): ")

    sub = input("Enter Subjects (comma seperated): ")
    subjects = [s.strip() for s in sub.split(",")]

    id_dob = (sid, dob)

    student = {
        "student_id": sid,
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects,
        "tuple": id_dob

    }

    students.append(student)

    student_dict[sid] = {
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects,
    }

    for s in subjects:
        subjects_set.add(s)

    print("\nStudents Added Successfully!\n")


# --------------------------------------
# Display Students 
# --------------------------------------
def display_students():
    if len(students) == 0:
        print("No Student Records Found.\n")
        return
    print("\n========== STUDENT RECORDS ==========\n")

    for stu in students:

        # f-string
        print(f"Student ID : {stu['student_id']}")

        # .format()
        print("Name : {}".format(stu["name"]))

        # % Formatting
        print("Age : %d" % stu["age"])

        print(f"Grade : {stu['grade']}")
        print(f"DOB : {stu['dob']}")
        print("Subjects :", ", ".join(stu["subjects"]))
        print("-" * 40)


# --------------------------------------
# Update Student 
# --------------------------------------
def update_student():
    sid = input("Enter Student ID to Update: ")

    if sid not in student_dict:
        print("Student Not Found.\n")
        return

    for stu in students:
        if stu["student_id"] == sid:

            print("Leave blank to keep old value. ")

            new_age = input("New Age: ")
            new_grade = input("New Grade: ")
            new_subjects = input("New Subjects (comma seperated): ")

            if new_age != "":
                stu["age"] = int(new_age)
                student_dict[sid]["age"] = int(new_age)

            if new_grade != "":
                stu["grade"] = (new_grade)
                student_dict[sid]["grade"] = new_grade

            if new_subjects != "":
                stu["subjects"] = [x.strip() for x in new_subjects.split(",")]
                student_dict[sid]["subjects"] = stu["subjects"]

                subjects_set.clear()

                for s in students:
                    for sub in s["subjects"]:
                        subjects_set.add(sub)

            print("Student Updated Successfully!\n")
            return


                


# --------------------------------------
# Delete Student 
# --------------------------------------
def delete_student():
    sid = input("Enter Student ID to Delete: ")

    for i in range(len(students)):
        if students[i]["student_id"] == sid:

            del students[i]
            del student_dict[sid]

            subjects_set.clear()

            for s in students:
                for sub in s["subjects"]:
                    subjects_set.add(sub)

            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found. \n")


# --------------------------------------
# Display Subjects 
# --------------------------------------
def display_subjects():
    print("\nUnique Subjects Offered:")

    if len(subjects_set) == 0:
        print("No Subjects Available.\n")
        return

    for sub in sorted(subjects_set):
        print("-", sub)

    print()


# --------------------------------------
# Main Menu 
# --------------------------------------
while True:

    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_subjects()

    elif choice == "6":
        print("\nThank you for using Student Data Organizer!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
