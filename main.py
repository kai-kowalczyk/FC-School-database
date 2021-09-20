import sys
from school.commands import ALLOWED_COMMANDS, MSG


while True:
    command = input('Podaj typ użytkownika ("uczen", "nauczyciel", "wychowawca") lub komendę "koniec".')
    if command not in ALLOWED_COMMANDS:
        print(f'{MSG} Wybierz jedno z: {ALLOWED_COMMANDS}')
        continue
    if command == 'koniec':
        break

    if command == 'wychowawca':
        pass

    if command == 'uczen':
        pass

    if  command == 'nauczyciel':
        pass

    
