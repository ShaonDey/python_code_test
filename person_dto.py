class Person:

    def __init__(self, first_name: str, last_name: str, father):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.person_father: Person = father
