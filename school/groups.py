from .users import *

class School:

    def __init__(self):
        self.group_dict = {}

    def add_student(self):
        firstname = input('Imię: ')
        lastname = input('Nazwisko: ')
        group = input('Klasa: ')
        student = Student(firstname=firstname, lastname=lastname, group=group)
        if group in self.group_dict.keys():
            self.group_dict[group]['students'].append(student)
        if group not in self.group_dict.keys():
            self.group_dict[group] = {'students': [student]}

    def add_supervisor(self):
        firstname = input('Imię: ')
        lastname = input('Nazwisko: ')
        group = input('Klasa prowadzona: ')
        supervisor = Supervisor(firstname=firstname, lastname=lastname)
        if group in self.group_dict.keys():
            self.group_dict[group]['supervisor'] = supervisor
        if group not in self.group_dict.keys():
            self.group_dict[group] = {'supervisor': supervisor}

class Group:

    def __init__(self, group_id, supervisor):
        self.group_id = group_id
        self.supervisor = supervisor

    def add_teacher(self):
        firstname = input('Imię: ')
        lastname = input('Nazwisko: ')
        subject = input('Przedmiot prowadzony: ')
        teacher = Teacher(firstname=firstname, lastname=lastname, subject=subject)
        while True:
            group = input('Nauczana klasa: ')
            if len(group) > 0:
                self.taught_groups.append(group)
            else:
                break




