## Описание программы.

Целью данной программы является создание архивных копий файлов Документооборота c  `\\asu-nas\docserver`
Веб сервер построен на базе микро фреймворка [flask](https://flask.palletsprojects.com/en/2.0.x/) 
и предназначен для управления вентилятором.<br/> 
Есть возможность ручного включения и выключения, а
также работы по расписанию.

![](WebServer/ui/pic/fan_control_pic.png)

## Подготовка к запуску проекта
1. **Уcтановить git**<br/>
``` 
$ sudo apt install git
```
    

2. **Склонировать репозиторий в нужную директорию**<br/>
```
$ git clone git@asu-gitlab.marbum.ru:vasilev_sr/fan-control.git
```
   

3. **Установить библиотеки**
```
$ sudo apt-get update
$ sudo apt install mc
$ pip3 install flask 
$ sudo apt-get -y install python3-rpi.gpio
```

4. **Добавить файл **main.py** в автозагрузку**
   
выполнить команду:<br/>
```
$ nano /etc/xdg/autostart/FanControl.desktop
```

прописать в файле **FanControl** и сохранить:<br/>
```
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Fan_conrol
Comment=
Exec=sudo python3 /home/pi/App/fan-control/WebServer/main.py
Terminal=true
Type=Application
```

>ВАЖНО<br/>
> * Библиотека **rpi.gpio** работает только на raspberry, для отладки кода на вашем компьютере
> необходимо закомментировать все ее вызовы.<br/>
> * Не забудьте поменять путь расположения файла main.py в **FanControl > Exec**
> * Название файла в папке **autostart** обязательно должно заканчиваться **.desktop**.<br/>
    Например: fan_control.desktop. Иначе скрипт не запустится после перезагрузки.











