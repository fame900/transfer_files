import os
import datetime as dt
import shutil

os.chdir(r'C:\python\file\123')  # переходим в директорию, где будем создавать архив
shutil.make_archive('archive', 'zip', root_dir=r'C:\python\file\archive') # создание архива
day = dt.date.today().strftime('%d.%m.%Y') # время в нужном формате
file = open('log.txt', 'w').write(day + ': logs') # создание log
