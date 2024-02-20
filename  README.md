Программа отчета получения документов.
Микросервис позволяет отправлять письмо о загрузке документа на сервис и принимать или отклонять данный документ администратором.

Стек проекта:
Python -3.10
Django
DjangoREST

Документация redoc, swagger доступна после запуска проекта БД - Postgres
данные вынесены в .env

Перед запуском создать и заполнить СВОЙ файл .env СВОИМИ данными

Состав файла env.
DB_ENGINE=django.db.backends.postgresql
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=5432 (db - для докера)

Данные отправки писем

EMAIL_HOST = EMAIL_PORT = EMAIL_HOST_USER = EMAIL_HOST_PASSWORD = EMAIL_USE_SSL = True

Запуск в докер контейнере
Docker
docker-compose build
docker-compose up

Проект выполнил Носков Александр на IDE - PyCharm
