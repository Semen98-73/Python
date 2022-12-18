# 2)Нужно написать программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки.

class Student:
    def __init__(self):
        self.name = ''
        self.group = ''
        self.marks = ''
        self.progress = 'отлично'

    def get_student(self):
        for mark in ['1', '2', '3']:
            if mark in self.marks:
                self.progress = 'неудовлетворительно'
                break
        return self.name, self.group, self.marks, self.progress


students = []
for i in range(1, 4):
    student = Student()
    student.name = input(f"Фамилия студента № {i}: ")
    student.group = input("Группа:  ")
    student.marks = input("Оценка: ")
    students.append(student.get_student())

print(sorted(students))


def weak_students(li):
    for progress in li:
        if 'неудовлетворительно' in progress:
            return True


print('Список студентов с низкими оценками:')
print(list(filter(weak_students, students)))