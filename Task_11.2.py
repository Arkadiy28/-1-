class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return ''.join(
            [
                f'"{self.name} {self.surname}"'.title()
            ]
        )

class Student(Person):
    def __init__(self, name, surname, group, *set_test_score):
        super().__init__(name, surname)
        self.set_test_score = list(set_test_score)
        self.group = group
        self.appraisals = self.set_test_score


    def __str__(self):
        return ''.join(
            [
                f'Студент: {self.name} {self.surname}, группа {self.group} оценки {self.appraisals}'
            ]
        )


d = Student('Alex', 'Fedorov', 'G-5', 5, 4, 4)
print(d)

u = Student('Нина', 'Кортынова', 'Г-5', 2, 5, 4)
print(u)
