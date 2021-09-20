class Supervisor:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.supervised_groups = []

    def add_classes(self, group_id):
        if len(group_id) > 2:
            print('Złe oznaczenie klasy! (Prawidłowo: pierwszy znak to cyfra, drugi to litera.)')
        else:
            self.supervised_groups.append(group_id)

class Pupil:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Teacher:
    def __init__(self, firstname, lastname, subject):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject