import os
import shutil
import logging

# логирование
logging.basicConfig(format='%(asctime)15s - %(levelname)s:  %(message)s', datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,filename=r'\\asu-videoservr2\Arhiv_docs\log.txt')

path_asu_nas = r'\\asu-nas\docserver'
path_archive_docx = r'\\asu-videoservr2\Arhiv_docs'
print('Please wait')

dir_list = [os.path.join(path_asu_nas, file) for file in os.listdir(path_asu_nas)] # получаем пути к файлам
if dir_list:
    date_list = [[x, os.path.getctime(x)] for x in dir_list]  # Создадим список из путей к файлам и дат их создания.
    # Отсортируем список по дате создания в обратном порядке
    sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)[0][0]
    file_name = sort_date_list[-8:]  # создание имени для zip-файла
    os.chdir(path_archive_docx)  # переходим в директорию, где будем создавать архив
    archive = shutil.make_archive(file_name, 'zip', root_dir=sort_date_list)  # создание архива
    if archive[-12:] == file_name + '.zip':
        print('Ready')
        logging.info(f'Архив № {file_name} создан успешно!')
    else: logging.info(f'Архив № {file_name} не создан')