# נושא: Polymorphism (פולימורפיזם)

# מטרת הפולימורפיזם:
# לאפשר לפונקציה עם אותו שם להתנהג בצורה שונה
# במחלקות שונות.

# מימוש:
# - מחלקת בסיס Animal עם פונקציה speak
# - מחלקות Dog ו-Cat שמממשות את הפונקציה בצורה שונה

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow")


# בדיקה
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()