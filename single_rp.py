"""
What is SOLID
SOLID is an abbreviation that stands for five software design principles compiled by Uncle Bob:

S - Single responsibility Principle
O - Open-closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle


The single responsibility principle (SRP) states that:
    - Your class or method should have only one reason to change.
    - It should have only one responsibility to take care of.
"""

class Student:
    """
    Class responsible to store, fetch patients data and do some operations.
    - store_details
    - get_details
    - get_total
    - get_percentage
    """

    def __init__(self, name, roll, phy, math) -> None:
        self.roll = roll
        self.name = name
        self.phy = phy
        self.math = math

    def store_details(self):
        # store data to the db
        print("store to db.....")

    def get_details(self):
        # fetch the data of the student from db
        return {
            "Roll no": self.roll,
            "Name": self.name,
            "Physics": self.phy,
            "Maths": self.math
        }

    def get_total(self):
        total = self.phy + self.math
        return total

    def get_percentage(self, n):
        percent = (self.get_total()/(n*100))*100
        return percent

    def __str__(self) -> str:
        return f"Roll: {self.roll}\nName: {self.name}\nTotal Marks: {self.get_total()}\nPercentage: {self.get_percentage(2)}%"


class ResultManager():

    @staticmethod
    def write_marksheet(student):
        file = open('mark.txt', 'w')
        file.write(str(student))
        file.close()


student_inst = Student("Jon", 16, 88, 89)

student_inst.store_details()
print(student_inst.get_details())
# print(student_inst.get_total())
# print(student_inst.get_percentage(n=2))

print('marksheet....')
result_inst = ResultManager()
result_inst.write_marksheet(student_inst)
# student_inst.write_marksheet()

with open('mark.txt') as f:
    print(f.read())
