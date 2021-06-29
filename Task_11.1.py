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

a = Person('сургей', 'жуков')

b = Person('Анна', 'сергеева')

print(a)

print(b)
