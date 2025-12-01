class Person:
    "Base class"
    def __init__(self):
        pass

    def input(self):
        raise NotImplementedError("Subclasses must implement input().")

    def display(self):
        raise NotImplementedError("Subclasses must implement display().")


class Student(Person):
    def __init__(self, sid="", name="", dob=""):
        super().__init__()
        self.__sid = sid
        self.__name = name
        self.__dob = dob

    def get_id(self): return self.__sid
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob

    def input(self):
        self.__sid = input("ID: ")
        self.__name = input("Name: ")
        self.__dob = input("DoB: ")

    def display(self):
        print(f"{self.__sid} | {self.__name} | DoB: {self.__dob}")


class Course:
    def __init__(self, cid="", name=""):
        self.__cid = cid
        self.__name = name

    def get_id(self): return self.__cid
    def get_name(self): return self.__name

    def input(self):
        self.__cid = input("ID: ")
        self.__name = input("Name: ")

    def display(self):
        print(f"{self.__cid} | {self.__name}")


class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {} 

    def input_students(self):
        n = int(input("Number of students: "))
        for i in range(n):
            print(f"\nStudent {i+1}:")
            s = Student()
            s.input()
            self.students.append(s)

    def list_students(self):
        print("\nStudents:")
        for s in self.students:
            s.display()

    def input_courses(self):
        n = int(input("Number of courses: "))
        for i in range(n):
            print(f"\nCourse {i+1}:")
            c = Course()
            c.input()
            self.courses.append(c)

    def list_courses(self):
        print("\nCourses:")
        for c in self.courses:
            c.display()

    def input_marks(self):
        if not self.students or not self.courses:
            print("Add students and courses first")
            return

        print("\nCourses:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.get_id()} - {c.get_name()}")

        try:
            choice = int(input("Choose course: ")) - 1
            cid = self.courses[choice].get_id()
        except:
            print("Invalid")
            return

        if cid not in self.marks:
            self.marks[cid] = {}

        print("\nEnter marks:")
        for s in self.students:
            while True:
                try:
                    m = float(input(f"Mark for {s.get_id()} - {s.get_name()}: "))
                    break
                except:
                    print("Please enter a number")
            self.marks[cid][s.get_id()] = m

    def show_marks(self):
        print("\nCourses:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.get_id()} - {c.get_name()}")

        try:
            choice = int(input("Choose course: ")) - 1
            cid = self.courses[choice].get_id()
        except:
            print("Invalid")
            return

        print(f"\nMarks for {cid}:")
        if cid not in self.marks:
            print("No marks yet")
            return

        for s in self.students:
            sid = s.get_id()
            mark = self.marks[cid].get(sid, "No mark")
            print(f"{sid} - {s.get_name()}: {mark}")

    def run(self):
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

            if choice == "1": self.input_students()
            elif choice == "2": self.input_courses()
            elif choice == "3": self.list_students()
            elif choice == "4": self.list_courses()
            elif choice == "5": self.input_marks()
            elif choice == "6": self.show_marks()
            elif choice == "0":
                print("Terminated!")
                break
            else:
                print("Invalid")


if __name__ == "__main__":
    MarkManagement().run()
