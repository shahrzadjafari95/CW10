import pickle


class Person:
    def __init__(self, name, age,address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

    def save_person_objects(persons, filename):
        with open(filename, 'wb') as file:
            pickle.dump(persons, file)


person_list = [
    Person("sina",23,"kish"),
    Person("ali",25,"tehran"),
    Person("sara",21,"tabriz"),
]

Person.save_person_objects(person_list, "persons.pkl")