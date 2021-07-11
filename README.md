#### Django python
```bash
# guide: https://codelearn.io/sharing/web-step-by-step-voi-django
# https://www.howkteam.vn/course/lap-trinh-web-voi-python-bang-django/tao-mot-web-app-va-xu-ly-khi-nguoi-dung-yeu-cau-truy-cap-trong-python-django-1517

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
├── README.md
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-39.pyc
    │   ├── settings.cpython-39.pyc
    │   ├── urls.cpython-39.pyc
    │   └── wsgi.cpython-39.pyc
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
# start local server for develop
python3 manage.py runserver
#Django version 3.2.5, using settings 'mysite.settings'
#Starting development server at http://127.0.0.1:8000/
#Quit the server with CONTROL-C.

# create app in django, each app is a feature of a website
python3 manage.py startapp home
```