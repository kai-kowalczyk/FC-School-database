from school.groups import School
import sys
from school.commands import ALLOWED_COMMANDS, MSG

phrase = sys.argv[1] #nazwa klasy, wychowawca, nauczyciel, uczeń

school = School()

while True:
    command = input('Podaj typ użytkownika ("uczen", "nauczyciel", "wychowawca") lub komendę "koniec".')
    if command not in ALLOWED_COMMANDS:
        print(f'{MSG} Wybierz z: {ALLOWED_COMMANDS}')
        continue
    if command == 'koniec':
        break

    if command == 'wychowawca':
        school.add_supervisor()

    if command == 'uczen':
        school.add_student()

    if  command == 'nauczyciel':
        school.add_teacher()


if phrase == 'klasa':
    klasa = input('Nazwa klasy: ')
    if klasa in school.group_dict.keys(): #phrase - nazwa klasy
        print(school.group_dict)

if phrase == 'wychowawca':
    wychowawca = input('Imię i nazwisko: ')
    for group_id, data in school.group_dict.items(): #phrase - wychowawca
        supervisor = data['supervisor']
        if wychowawca == f'{supervisor.firstname} {supervisor.lastname}':
            print(data['students'])

'''print(school.group_dict)
print(school.teachers_dict)'''

    