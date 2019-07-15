import os
import shutil


def making_dir(dirs):
    dir_path = os.path.join(os.getcwd(), dirs)
    try:
        os.mkdir(dir_path)
        print(f'Директория успешно создана - {dir_path}')
    except FileExistsError:
        print(f'{dir_path} - такая директория уже есть')


def remove_dir(dirs):
    dir_path = os.path.join(os.getcwd(), dirs)
    try:
        os.removedirs(dir_path)
        print(f'Директория успешно удалена - {dir_path}')
    except FileNotFoundError:
        print(f'{dir_path} - директория не существует')


def show_dir():
    print('Папки в текущей директории: ')
    current_path = os.getcwd()
    for i in os.listdir(current_path):
        if os.path.isdir(i):
            print(i)


def copy_file(file_name):
    if os.path.isfile(file_name):
        newfile = file_name + '.copy'
        shutil.copy(file_name, newfile)
        if os.path.exists(newfile):
            print(f'Файл {newfile} создан')
            return True
        else:
            print('Возникли проблемы с копированием')
            return False


def change_dir(dirs):
    try:
        os.chdir(dirs)
        print(f'Текущая директория {os.getcwd()}')
    except FileNotFoundError:
        print(f'Директории {dirs} не существует')
