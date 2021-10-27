import os
import zipfile
import docx
import datetime as dt

os.chdir(r'C:\python\file\123')  # переходим в директорию, где будем создавать архив
zip_obj = zipfile.ZipFile('archive.zip', "w")  # Создаем архив
os.chdir(r'C:\python\file\12\test')  # переходим в директорию, где будем добавлять файл
zip_obj.write("test.docx")  # добавление файла в архив
zip_obj.close()

day = dt.date.today()
day_format = day.strftime('%d.%m.%Y')
print(type(day))

# Создание log
doc = docx.Document()
doc.add_paragraph('Тест  -  '+ day_format)
doc.save(r'C:\python\file\123\log.docx')
