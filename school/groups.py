import users

class Group:
    def __init__(self, group_id, supervisor):
        self.group_id = group_id
        self.supervisor = supervisor
        self.pupils = []
    def add_pupil(self):
        firstname = input('Podaj imię: ')
        lastname = input('Podaj nazwisko: ')
        pupil = Pupil(firstname=firstname, lastname=lastname)
        self.pupils.append(pupil)
    def add_teacher(self):
        firstname = input('Podaj imię: ')
        lastname = input('Podaj nazwisko: ')
        

