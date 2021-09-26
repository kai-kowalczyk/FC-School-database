from school.groups import School
import sys
from school.commands import ALLOWED_COMMANDS, MSG

phrase = sys.argv[1]

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
        pass

if phrase in school.group_dict.keys(): #phrase - nazwa klasy
    print(school.group_dict)

    
