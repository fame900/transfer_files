import os
import shutil
import logging

# логирование
logging.basicConfig(
    format="%(asctime)15s - %(levelname)s:  %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    filename=r"\\asu-videoservr2\Arhiv_docs\log.txt",
)

path_asu_nas = r"\\asu-nas\docserver"
path_archive_docx = r"\\asu-videoservr2\Arhiv_docs\docserver"

dir_list_asu_nas = [
    os.path.join(path_asu_nas, file) for file in os.listdir(path_asu_nas)
]  # получаем пути к файлам
dir_list_backup = [
    os.path.join(path_archive_docx, file) for file in os.listdir(path_archive_docx)
]

folders_asu = [i[-8:] for i in dir_list_asu_nas]
archives = [i[-12:-4] for i in dir_list_backup]
folders_noarchive = list(set(folders_asu) ^ set(archives))

try:
    if folders_noarchive != []:
        for folder_name in folders_noarchive:
            os.chdir(path_archive_docx)
            shutil.make_archive(
                folder_name, "zip", root_dir=f"""{path_asu_nas}\{folder_name}"""
            )
            logging.info(f"Архив {folder_name} создан успешно!")
except:
    logging.exception("Error")
