class School:
    def __init__(self):
        self.students = {}
        self.operations = []

    def add_student(self, name, grade):
        if name not in self.students.keys():
            self.students[name] = grade
            self.operations.append(True)
        else:
            self.operations.append(False)

    def roster(self):
        students = [(grade,student) for student, grade in self.students.items()]

        return [student[1] for student in sorted(students)]

    def grade(self, grade_number):
        students = [student for student, grade in self.students.items() if grade == grade_number]
        return sorted(students)

    def added(self):
        return self.operations


school = School()

school.add_student("Maria",2)
school.add_student("José",2)
school.add_student("Bianca",1)
school.add_student("Bianca",3)
school.add_student("Bianca",1)
school.add_student("Amanda",2)

print(school.grade(2))
print(school.added())
print(school.roster())