import sys
from core import create_file, copy_file, create_folder, get_list, delete_file, save_info,change_dir
from random_number import game_number
save_info('Старт')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо выбрать команду. help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            delete_file(name)
    elif command == 'ch':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Необходимо ввести имя папки')
        else:
            change_dir(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Необходимо ввести название файла и название копии')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла и папки')
        print('copy - копирование файла и папки')
        print('game - игра "Угадай число"')
    elif command == 'game':
        game_number()
    save_info('Конец')
