class Lecture:
    def __init__(self, name, max_students, duration, professors):
        self.name = name
        self.max_students = max_students
        self.duration_minutes = duration
        self.professors = professors
    
    def print_name_and_duration(self):
        print(f"{self.name} - {self.duration_minutes} minutes")

    def add_professors(self, new_professor):
        self.professors.append(new_professor)


###Professor and Student inherit from Person class person.py

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def print_full_name(self):
        print(f"{self.first_name} {self.last_name}")


from person import Person

class Professor(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures

    def list_lectures(self):
        print("Teaches lectures:")
        for lecture in self.lectures:
            print(f"- {lecture.name}")
    
    def teach_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

    def remove_lecture(self, lecture):
        self.lectures.pop(lecture)

from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, lectures):
        super().__init__(first_name, last_name, age)
        self.lectures = lectures
    
    def list_lectures(self):
        print("Attends lectures:")
        for lecture in self.lectures:
            print(f"- {lecture.name}")

    def attend_lecture(self, new_lecture):
        self.lectures.append(new_lecture)

    def leave_lecture(self, lecture):
        self.lectures.pop(lecture)

#test your code in main file main.py
from professor import Professor
from student import Student
from lecture import Lecture

cs_lecture = Lecture("Computer science", 15, 45, [])
python_basics_lecture = Lecture("Python programming basics", 25, 90, [])
python_advanced_lecture = Lecture("Python advanced", 10, 90, [])
algorithms_lecture = Lecture("Algorithms and data sturctures", 30, 120, [])

new_professor = Professor("Maria", "Smith", 34, [cs_lecture, python_basics_lecture])
new_professor.print_full_name()
new_professor.teach_lecture(python_advanced_lecture)
new_professor.list_lectures()

cs_lecture.add_professors(new_professor)
python_basics_lecture.add_professors(new_professor)
python_advanced_lecture.add_professors(new_professor)

print("------------------------------")

new_student = Student("David", "Green", 25, [algorithms_lecture])
new_student.print_full_name()
new_student.attend_lecture(python_basics_lecture)
new_student.list_lectures()

print("------------------------------")

cs_lecture.print_name_and_duration()
python_basics_lecture.print_name_and_duration()



