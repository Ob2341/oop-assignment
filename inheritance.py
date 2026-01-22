# נושא: Inheritance (הורשה)

# מטרת ההורשה:
# לאפשר למחלקה אחת לרשת תכונות ופונקציות ממחלקה אחרת.

# מימוש:
# - מחלקת בסיס Person
# - מחלקת Student שיורשת מ-Person

class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is", self.name)


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def show_id(self):
        print("Student ID:", self.student_id)


# בדיקה
student = Student("Omer", 12345)
student.say_hello()
student.show_id()