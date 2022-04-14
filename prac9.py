# Name = Rajput Akshaykumarsing Virendra
# ID = 20cs069


class student:
    Name = ''
    idNumber = ''
    branch = ''
    department = ''

    def details(self, id, Name, branch, dept):
        self.Name = Name
        self.idNumber = id
        self.branch = branch
        self.department = dept

class exam(student):
    subMarks = {'Maths': 0, 'DBMS': 0, 'MCO': 0, 'PIP': 0, 'SGP': 0, 'HS':0}

    def marks(self, submarks):
        for i in self.subMarks.keys():
            self.subMarks[str(i)] = submarks[str(i)]
        


class result(exam):
    total_marks = 0
    def result_of_student(self, submarks):
        for item in submarks.values():
            self.total_marks += item
            

student1 = result()
sName = input("Enter the name: ")
sID = input("Enter the Roll Number: ")
sBranch = input("Enter your branch: ")
sDepartment = input("Enter department name: ")

student1.details(sID, sName,sBranch,sDepartment)

print(f"Enter 6 subjects marks of {student1.Name} : \n")
marks = dict()
for i in student1.subMarks.keys():
    marks[str(i)] = (int(input(f'{i}: ')))

student1.result_of_student(marks)
print(f"Total of {student1.Name} mark's is : {student1.total_marks}")