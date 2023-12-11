class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}, {self.age}'

person1 = Person('Aivaras', '32')
person2 = Person('Judita', '26')
person3 = Person('Markas', '7')
people_list = []
people_list.extend([person1, person2, person3])
print(people_list)


def sorting_by_name(person):
    return person.name

sorted_people_list = sorted(people_list, key=sorting_by_name)

reverse_sorted_people_list = sorted(people_list, key=sorting_by_name, reverse=True)
print(reverse_sorted_people_list)
