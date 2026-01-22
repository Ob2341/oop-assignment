# שם הסטודנט: עומר
# קורס: תכנות מונחה עצמים
# נושא: Encapsulation (כימוס)

# מטרת הכימוס:
# למנוע גישה ישירה לנתונים פנימיים של המחלקה
# ולאפשר גישה אליהם רק דרך פונקציות ייעודיות.

# מימוש:
# - משתנה balance מוגדר כמשתנה פרטי
# - גישה ליתרה מתבצעת רק דרך פונקציה

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # משתנה פרטי (לא נגיש ישירות)

    def deposit(self, amount):
        # פעולה להוספת כסף לחשבון
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        # פעולה להחזרת היתרה
        return self.__balance


# בדיקה של המחלקה
account = BankAccount("Omer", 1000)
account.deposit(500)
print(account.get_balance())
