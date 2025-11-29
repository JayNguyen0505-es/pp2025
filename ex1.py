students = []
courses = []
marks = {}

def input_students():
    n = int(input("Number of students: "))
    for i in range(n):
        print(f"\nStudent {i + 1}:")
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("DoB: ")
        students.append((sid, name, dob))

def input_courses():
    n = int(input("Number of courses: "))
    for i in range(n):
        print(f"\nCourse {i + 1}:")
        cid = input("ID: ")
        cname = input("Name: ")
        courses.append((cid, cname))

def input_marks():
    if not students or not courses:
        print("Add students and courses first!")
        return

    print("\nCourses:")
    for i, (cid, cname) in enumerate(courses):
        print(f"{i+1}. {cid} - {cname}")

    try:
        choice = int(input("Choose course: ")) - 1
        cid = courses[choice][0]
    except:
        print("Invalid choice.")
        return

    if cid not in marks:
        marks[cid] = {}

    print("\nEnter marks:")
    for sid, name, dob in students:
        while True:
            try:
                m = float(input(f"Mark for {sid} - {name}: "))
                break
            except:
                print(" Enter a number!")
        marks[cid][sid] = m

def list_students():
    print("\nStudents:")
    for sid, name, dob in students:
        print(f"{sid} | {name} | DoB: {dob}")

def list_courses():
    print("\nCourses:")
    for cid, cname in courses:
        print(f"{cid} | {cname}")

def show_marks():
    print("\nCourses:")
    for i, (cid, cname) in enumerate(courses):
        print(f"{i+1}. {cid} - {cname}")

    try:
        choice = int(input("Choose course: ")) - 1
        cid = courses[choice][0]
    except:
        print("Invalid choice.")
        return

    print(f"\nMarks for {cid}:")
    if cid not in marks:
        print("No marks yet.")
        return

    for sid, name, dob in students:
        mark = marks[cid].get(sid, "No mark")
        print(f"{sid} - {name}: {mark}")

def main():
    while True:
        print("\nMenu:")
        print("1. Input students")
        print("2. Input courses")
        print("3. List students")
        print("4. List courses")
        print("5. Input marks")
        print("6. Show marks")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1": input_students()
        elif choice == "2": input_courses()
        elif choice == "3": list_students()
        elif choice == "4": list_courses()
        elif choice == "5": input_marks()
        elif choice == "6": show_marks()
        elif choice == "0":
            print("Terminated!")
            break
        else:
            print("Invalid option.")

main()
