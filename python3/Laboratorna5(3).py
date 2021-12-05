class Student:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.labs = [0.0] * (data['lab_num'])
        self.exam = 0.0

    def lab_add(self, m, n=None):
        if n == None:
            for i in range(self.data['lab_num']):
                if self.labs[i] == 0:
                    n = i
                    break
        if n >= self.data['lab_num']:
            return self
        if m > self.data['task_max']:
            m = self.data['task_max']
        self.labs[n] = m
        return self

    def task_add(self, m):
        if m >= self.data['task_max']:
            m = self.data['task_max']
            self.exam = m
            return self
        self.exam = m
        return self

    def is_certified(self):
        marks = 0.0
        course_max = self.data['task_max'] + self.data['lab_max'] * self.data['lab_num']
        for mark in self.labs:
            marks += mark
        marks += self.exam

        if float(marks) / float(course_max) < self.data['k']:
            return marks, False
        else:
            return marks, True


data = {'task_max': 40, 'lab_max': 5, 'lab_num': 10, 'k': 0.62}

student = input("ВВведіть фамілію студента: ")
stud = Student(student, data)
print("Введіть оцінки за лабораторні роботи: ")
stud.lab_add(int(input()), 1)
stud.lab_add(int(input()), 2)
stud.lab_add(int(input()), 3)
stud.lab_add(int(input()), 4)
stud.lab_add(int(input()), 5)
stud.lab_add(int(input()), 6)
stud.lab_add(int(input()), 7)
stud.lab_add(int(input()), 8)
stud.lab_add(int(input()), 9)
stud.lab_add(int(input()), 10)
print("Введіть оцінку за творчу роботу: ")
stud.task_add(int(input()))
print(stud.is_certified())