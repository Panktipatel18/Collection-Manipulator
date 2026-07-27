# 🎓 Student Data Organizer (Collection Manipulator)

A beginner-friendly, menu-driven Python console application that manages student
records using Python's core collection data types — **List, Tuple, Set, and
Dictionary**. Built as a clean, well-commented, PEP 8–compliant project ideal
for learning and college submission.

---

## 📌 Project Description

**Student Data Organizer** is a console-based CRUD (Create, Read, Update,
Delete) application for managing student information. It was designed
specifically to demonstrate practical, real-world usage of Python's built-in
collection types, string formatting techniques, type casting, and the `del`
keyword — all inside a single, easy-to-follow script.

---

## 🎯 Objective

To build a menu-driven Python program that:

- Organizes and manipulates student data using Lists, Tuples, Sets, and
  Dictionaries.
- Demonstrates the difference between mutable and immutable collections.
- Reinforces core Python fundamentals through a practical, hands-on project.

---

## ✨ Features

- Add new student records with full input validation.
- Display all students in a clean, table-like console format.
- Update existing student information (name, age, grade, subjects).
- Delete a student record using the `del` keyword.
- View all unique subjects offered across every student (powered by a `set`).
- Friendly welcome and thank-you messages.
- Graceful handling of invalid menu choices and invalid input.

---

## 🛠️ Technologies Used

| Technology | Purpose                          |
|------------|-----------------------------------|
| Python 3.x | Core programming language         |
| Standard Library only | No external dependencies needed |

---

## 🧠 Python Concepts Used

- Menu-driven program design with functions
- Collection data types: `list`, `tuple`, `set`, `dict`
- String formatting: f-strings, `.format()`, and `%` formatting
- Mutability (List, Dictionary) vs. Immutability (Tuple)
- Type casting (`str` → `int`)
- The `del` keyword for record deletion
- Input validation using `try` / `except` and loops
- PEP 8 coding style and meaningful naming conventions

---

## 📦 Collection Data Types Used

| Collection | Used For                                              | Why |
|------------|--------------------------------------------------------|-----|
| **List**   | Stores all student records (`student_records`)         | Ordered, mutable — perfect for a growing/shrinking database |
| **Tuple**  | Stores `(Student ID, Date of Birth)` pairs              | Immutable — this pairing should never change once created |
| **Set**    | Stores unique subjects offered (`subjects_offered`)     | Automatically removes duplicate subject entries |
| **Dictionary** | Stores each individual student's details            | Key-value pairs make fields easy to access and update |

---

## 📋 Menu Options

```
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

## 📁 Project Structure

```
Student-Data-Organizer/
│
├── student_data_organizer.py   # Main application script
├── README.md                   # Project documentation (this file)
├── requirements.txt            # Dependencies (none required)
├── LICENSE                     # MIT License
├── .gitignore                  # Files/folders excluded from Git
└── screenshots/                # Sample output screenshots
    ├── menu.png
    ├── add_student.png
    ├── display_students.png
    ├── update_student.png
    ├── delete_student.png
    └── subjects.png
```

---

## ⚙️ Installation

This project uses **only the Python Standard Library** — no external
packages are required.

1. Ensure you have **Python 3.7+** installed. Check with:
   ```bash
   python3 --version
   ```
2. Clone or download this repository:
   ```bash
   git clone https://github.com/Panktipatel18/Collection-Manipulator.git
   cd Collection-Manipulator
   ```

---

## ▶️ How to Run

Run the script directly using Python:

```bash
python3 student_data_organizer.py
```

On Windows, you can use:

```bash
python student_data_organizer.py
```

---

## 🖥️ Sample Output

```
============================================================
      STUDENT DATA ORGANIZER (COLLECTION MANIPULATOR)
============================================================
Welcome to the Student Data Organizer!
This program helps you manage student records using Python's
core collection types: List, Tuple, Set, and Dictionary.
------------------------------------------------------------

============================================================
                         MAIN MENU
============================================================
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
------------------------------------------------------------
Enter your choice (1-6): 2

============================================================
                    ALL STUDENT RECORDS
============================================================
ID   Name           Age   Grade     DOB           Subjects
------------------------------------------------------------
1    Asha Patel     16    10th      05-08-2009    Math, Science, English
------------------------------------------------------------
Total Students: 1
------------------------------------------------------------
```

> See the `screenshots/` folder for full visual examples of each menu option.

---

## 📚 Learning Outcomes

By completing this project, a learner will understand:

- How to design and structure a menu-driven console application.
- Practical differences between mutable and immutable Python collections.
- How to validate user input robustly.
- How to organize code into small, reusable, well-documented functions.
- How to format console output for readability using multiple string
  formatting techniques.

---

## 📝 Assumptions

- The application stores data **in memory only**; records are not saved to
  a file or database and will reset each time the program is restarted.
- Student IDs are auto-generated sequentially starting from `1`.
- Date of Birth is accepted as plain text in `DD-MM-YYYY` format with basic
  validation (not a full calendar-date check).
- The program is intended for single-user, single-session console use.

---

## 🚀 Future Improvements

- Persist student records to a file (CSV/JSON) or a database (SQLite).
- Add search and filter functionality (by name, grade, or subject).
- Add sorting options (by name, age, or ID).
- Build a graphical user interface (GUI) using Tkinter.
- Add unit tests using `unittest` or `pytest`.
- Export student reports to PDF or Excel.

---

## 👩‍💻 Author

**Pankti Patel**
GitHub: [Panktipatel18](https://github.com/Panktipatel18)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE)
file for details.
