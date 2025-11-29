students = []
courses = []
marks = {}

def input_students():
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\nStudent {i + 1}: ")
        sid = input("ID: ")
        sname = input("Name: ")
        sdob = input("DoB: ")
        students.append((sid, sname, sdob))

def input_courses():
    n = int(input("\nEnter number of courses: "))
    for i in range(n):
        print("\nCourse {i + 1}: ")
        cid = input("ID: ")
        cname = input("Name: ")
        courses.append((cid, cname))

def input_marks():
    if len(courses) <= 0 or len(students) <= 0:
        print("You must input valid students/courses first")
        return

    print("\nCourses:")
    for i, (cid, cname) in enumerate(courses):
        print("{i+1}. {cid} - {cname}")

    try:
        choice = int(input("Select a course (number): ")) - 1
        if choice < 0 or choice >= len(courses):
            print("Invalid course selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    course_id = courses[choice][0]

    if course_id not in marks:
        marks[course_id] = {}

    print("\nEnter marks: ")
    for sid, sname, sdob in students:
        while True:
            try:
                m = float(input("Mark for {sid} - {sname}: "))
                break
            except ValueError:
                print("  Please enter a valid number.")
        marks[course_id][sid] = m

def list_students():
    print("\nStudents: ")
    if not students:
        print("No students yet.")
        return
    for sid, sname, sdob in students:
        print("{sid} | {sname} | DoB: {sdob}")

def list_courses():
    print("\nCourses: ")
    if not courses:
        print("No courses yet.")
        return
    for cid, cname in courses:
        print("{cid} | {cname}")

def show_marks():
    if len(courses) == 0:
        print("No courses available.")
        return

    print("\nCourses: ")
    for i, (cid, cname) in enumerate(courses):
        print("{i+1}. {cid} - {cname}")

    try:
        choice = int(input("Select a course (number): ")) - 1
        if choice < 0 or choice >= len(courses):
            print("Invalid course selection.")
            return
    except ValueError:
        print("Invalid input.")
        return

    course_id = courses[choice][0]

    print("\nMarks for course {course_id}:")
    if course_id not in marks:
        print("No marks entered yet.")
        return

    for sid, sname, sdob in students:
        if sid in marks[course_id]:
            print("{sid} - {sname}: {marks[course_id][sid]}")
        else:
            print("{sid} - {sname}: No mark")

def main():
    while True:
        print("\nStudents' mark management: ")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks for a course")
        print("6. Show marks")
        print("0. Exit")

        print("\nCurrent students:", len(students))
        print("Current courses:", len(courses))
        print("Current mark records:", len(marks))

        c = input("\nChoose: ").strip()

        if c == "1":
            input_students()
        elif c == "2":
            input_courses()
        elif c == "3":
            list_students()
        elif c == "4":
            list_courses()
        elif c == "5":
            input_marks()
        elif c == "6":
            show_marks()
        elif c == "0":
            print("Terminated!")
            break
        elif c == "":
            continue
        else:
            print("Invalid choice")

main()
