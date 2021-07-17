#### Django python
```bash
# guide: https://codelearn.io/sharing/web-step-by-step-voi-django
# https://www.howkteam.vn/course/lap-trinh-web-voi-python-bang-django/tao-mot-web-app-va-xu-ly-khi-nguoi-dung-yeu-cau-truy-cap-trong-python-django-1517
# debugging: https://www.youtube.com/watch?v=oOeR6VZiPtI

# install django
pip3 install django
# check django version
python3
>> import django
>> print(django.get_version())
3.2.5
# craete new project
django-admin startproject mysite
cd mysite
tree
.
├── README.md         -> my tutorial
├── db.sqlite3        -> database of SQLite
├── manage.py         -> interactive django by command line interface
└── mysite
    ├── __init__.py   -> this folder as a python package
    ├── asgi.py
    ├── settings.py   -> configure
    ├── urls.py       -> URL of projects
    └── wsgi.py
# start local server for develop
python3 manage.py runserver
#Django version 3.2.5, using settings 'mysite.settings'
#Starting development server at http://127.0.0.1:8000/
#Quit the server with CONTROL-C.

# create app in django, each app is a feature of a website
python3 manage.py startapp home
# update setting for new app home
python3 manage.py migrate

# make a test case in home app
# home/tests.py
python3 manage.py test home

# create a table Post(id, title, body, date) -> https://docs.djangoproject.com/en/3.2/topics/db/models/
# Django model data types -> https://www.webforefront.com/django/modeldatatypesandvalidation.html
# create new app blog -> https://www.howkteam.vn/course/lap-trinh-web-voi-python-bang-django/dung-model-tao-bang-database-trong-python-django-1521
python3 manage.py startapp blog
# using model and database
# updated -> blog/models.py
# make migrations -> model Post
python3 manage.py makemigrations blog
# run migration
python3 manage.py migrate

# using query directly the same tinker of Laravel
python3 manage.py shell
# in mod shell
>>> from blog.models import Post
>>> a = Post()
>>> a.title = 'First Title'
>>> a.body = 'Hello World'
>>> a.save()

>>> b = Post(title='Secondary Post', body='Hello Django')
>>> b.save()

>>> Post.objects.all()

>>> Post.objects.get(id=1)
>>> exit()

# admin
python3 manage.py createsuperuser
# admin/123456
# datdao/123strong
# modified -> blog/admin.py

# show list post
# modified -> blog/views.py

# add test case -> blog/tests.py
python3 manage.py test blog
# custom template 404

# update model -> image = models.ImageField(null = True)
pip3 install Pillow
python3 manage.py makemigrations
python3 manage.py migrate
# create from login, logout
# https://www.howkteam.vn/course/lap-trinh-web-voi-python-bang-django/tao-form-dang-ky-tai-khoan-trong-python-django-1530
```