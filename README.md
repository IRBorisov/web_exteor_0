# web_exteor_0

Начальная интерация сайта (дипломный проект) с функционалом по работе с родоструктым языком на основе ПО Exteor. 
На данный момент можно запустить локально через docker-compose с доступом по ссылке http://localhost:1337. 
Запускается 2 контейнера: один с django-приложением, другой - с сервером nginx. Сейчас можно только вносить/редактировать записи. 
Данные сохраняются в БД sqlite в томе за пределами docker - контенеров. 

MIPT net course

DRAFT Project Web_Exteor (Django-gunicorn-nginx server with web-app & sqlite-database in external volume) 

To start draft app: 

1. docker-compose up -d --build
2. Check http://localhost:1337
