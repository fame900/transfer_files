import os
import zipfile
import docx
import datetime as dt
import shutil

os.chdir(r'C:\python\file\123')  # переходим в директорию, где будем создавать архив
shutil.make_archive('20211028', 'zip', root_dir=r'C:\python\file\20211028') # Создание архива

day = dt.date.today()
day_format = day.strftime('%d.%m.%Y')
print(type(day))

# Создание log
doc = docx.Document()
doc.add_paragraph('Тест  -  '+ day_format)
doc.save(r'C:\python\file\123\log.docx')
