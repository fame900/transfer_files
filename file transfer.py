import os
import datetime as dt
import shutil

path_asu_nas = r'C:\python\afile\asu-nas'
path_backup = r'C:\python\afile\backup'

 # Путь к вашей папке

# Получим список имен всего содержимого папки
# и превратим их в абсолютные пути
dir_list = [os.path.join(path_asu_nas, x) for x in os.listdir(path_asu_nas)]

if dir_list:
    # Создадим список из путей к файлам и дат их создания.
    date_list = [[x, os.path.getctime(x)] for x in dir_list]
    print(date_list)

    # Отсортируем список по дате создания в обратном порядке
    sort_date_list = sorted(date_list, key=lambda x: x[1])
    print(sort_date_list)

    last_file=sort_date_list[0][0].replace('\\', '\\\\')
    # Выведем первый элемент списка. Он и будет самым последним по дате
    file_name = last_file[-8:]
    print(last_file)

    os.chdir(path_backup)  # переходим в директорию, где будем создавать архив
    print('Please wait')
    shutil.make_archive(file_name, 'zip', root_dir=last_file) # создание архива
    print('Ready')
    day = dt.date.today().strftime('%d.%m.%Y') # время в нужном формате