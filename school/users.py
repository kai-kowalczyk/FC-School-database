class Supervisor:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.supervised_group = None

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class Student:
    
    def __init__(self, firstname, lastname, group):
        self.firstname = firstname
        self.lastname = lastname
        self.group = group

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'

class Teacher:
    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'