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
    group_id = input('Nazwa klasy: ')
    if group_id in school.group_dict.keys():
        print(school.group_dict[group_id])

if phrase == 'wychowawca':
    supervisor_id = input('Imię i nazwisko wychowawcy: ')
    for group_id, data in school.group_dict.items():
        supervisor = data['supervisor']
        if supervisor_id == f'{supervisor.firstname} {supervisor.lastname}':
            print(data['students'])

if phrase == 'uczen':
    student_id = input('Imię i nazwisko ucznia: ')
    for group_id, data in school.group_dict.items():
        for student in data['students']:
            if student_id == f'{student.firstname} {student.lastname}':
                group = group_id
                break
        break
    for teacher_id, data in school.teachers_dict.items():
        for group_id in data['groups']:
            if group_id == group:
                print(data['subject'], ':', teacher_id)

if phrase == 'nauczyciel':
    teacher_id = input('Imię i nazwisko nauczyciela: ')
    for teacher, data in school.teachers_dict.items():
        if teacher_id == f'{teacher.firstname} {teacher.lastname}':
            for group_id in data['groups']:
                for group, data in school.group_dict.items():
                    if group == group_id:
                        print(group_id, ':', data['supervisor'])
                    
        break

    