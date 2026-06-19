# Index

- [Index](#index)
  - [Django Project Setup](#django-project-setup)
  - [Django App Setup](#django-app-setup)
  - [Django Model](#django-model)
  - [Django `makemigrations` vs `migrate`](#django-makemigrations-vs-migrate)
  - [Apply New Changes To Database](#apply-new-changes-to-database)
  - [Add Data From Admin Page](#add-data-from-admin-page)
  - [Show Data In Frontend](#show-data-in-frontend)

# Django Project Setup

- Create a project folder (like: School Project)
- Now 
  ```bash
    python venv .venv
  ``` 
  - Note: .venv is the skip method for `cd` when we using not need to change the directory. Because `manage.py` file is located in the main project folder (School Project).

- activate `.venv`
- Now 
  ```bash
    .venv\scripts\activate
  ``` 
- Install `django`
  ```bash
    pip install django
  ``` 
- Create a project `school_project`
  ```bash
    django-admin startproject school_project
  ```
  - Note: For standard method of project creation. Bassically app name is applying for the related name of project. But project name is always config:
  ```bash
  mkdir my_awesome_project
  cd my_awesome_project
  django-admin startproject config .
  ```
  - Note : To create a single new folder in your current location, type mkdir followed by the name you want to give the folder:
  mkdir my_new_folder.
- delete now `school_project`
  ```bash
    rd /s /q school_project
  ```
  -Note: This is delete command for windows.

- For root directory to make for `school_project`
  ```bash
    django-admin startproject school_project .
  ```
  -Note: Problem is Remember that this method is applying in the fixed or one project only. When you work a multiple apps project then this method is not for suitable. So, Follow now the `manage.py` file is comes into root project folder. So Benefit is now not need to use `cd` command.

- Setup Database (Initial Migration)

  ```sh
  py manage.py makemigrations
  py manage.py migrate
  ```
  - Note: After `migrate` the changes will be showing on `dbsqlite3` but before showing data need to install one extension name 'SQLite Viewer' by 'Florian Klampfer' installing for showing data into it.

- Note: If you forget any of command then

  ```sh
  py manage.py help
  ```
  - Note: Then all of importance command are showing there.

- Create superuser (admin user)

  ```sh
  py manage.py createsuperuser
  ```
  - Note: Here need to declare carefully `username:` and `Email address:` and `Password` and `Password (again)`
- After Creating a superuser we have to need run `runserver`
  ```sh
  py manage.py runserver
  ```

---
[⬆️ Go to Index](#index)

# Django App Setup

- Create an app

  ```sh
  py manage.py startapp school_app
  ```
  - Note: Benifit of apps using for time efficiency: You avoid the hassle of setting up the main project configurations repeatedly.
  - Benifit of apps using easy maintenance: Because the system's codebase is divided into independent apps (for example, creating separate apps like products, orders, and users for an e-commerce site), updating, debugging, or modifying a specific feature in the future becomes incredibly simple.
  - Simply reusable.

- Add this app name in [settings.py](./school_project/settings.py) within `INSTALLED_APPS`

  ```py
  INSTALLED_APPS = [
      ...
      'school_app',
  ]
  ```
- Now let's describing project & app structure with their work
  ```py
    SCHOOL PROJECT/            # Tomar main project folder (Root directory)
  │
  ├── .venv/                   # Virtual environment (Project-er isolated sandbox)
  │   ├── Include/             # C headers for Python packages (sadharonoto dorkar hoy na)
  │   ├── Lib/                 # Install kora shob packages (jemon Django) ekhane thake
  │   ├── Scripts/             # Environment activate ba deactivate korar scripts thake
  │   └── pyvenv.cfg           # Virtual environment-er configuration file
  │
  ├── school_app/              # Tomar Django application (kajer asol jayga)
  │   ├── migrations/          # Database e kono change korle tar history ekhane thake
  │   ├── __init__.py          # Python ke bujhay je ei folder ti ekti package
  │   ├── admin.py             # Django admin panel-e kon data dekhabe tar setup
  │   ├── apps.py              # Ei nirdishto app-er configuration thake
  │   ├── models.py            # Database-er table toiri korar code ekhane thake (Database Design)
  │   ├── tests.py             # Code thikmoto kaj korche kina ta check korar jonno test cases
  │   └── views.py             # Backend theke frontend-e ki data jabe tar logic ekhane thake
  │
  ├── school_project/          # Main project configuration folder (Project-er "Brain")
  │   ├── __pycache__/         # Python-er compiled files (eta automatically toiri hoy, ignore koro)
  │   ├── __init__.py          # Python ke bujhay je etao ekti package
  │   ├── asgi.py              # Asynchronous web server-er gateway (advance kajer jonno)
  │   ├── settings.py          # Project-er sob main settings (DB setup, timezone, app list)
  │   ├── urls.py              # Website-er shob links ba route (URL) ekhane define kora thake
  │   └── wsgi.py              # Project ke live server-e host korar jonno gateway
  │
  ├── db.sqlite3               # Django-er default database (tomar shob data ekhane save hobe)
  └── manage.py                # Command-line theke project control korar main tool (runserver, migrate etc.)
  ```
  -Note: `__init__` double underscore init double underscore aitake bole dandar method or magic method. Tomar Django Project-e er kaj ki?
  
  - Tomar school_app ebong school_project duti folder-ei `__init__`.py ache. Django automatically ei file-gulo toiri kore dey jate Python ei folder-guloke valid app/package hishebe chinte pare. Etar karonei `settings.py`-e `INSTALLED_APPS` er moddhe `school_app` likhle Django seta khuje pay.

  - TL;DR: `__init__`py hocche Python-er kache ekta "Identity Card". Eta chara Python tomar folder ke package hishebe chinbe na ebong kono code eke-oporer shathe import korte dibe na.
---
[⬆️ Go to Index](#index)

# Django Model

![Django Model](https://i.imgur.com/LBW8872.png)
![Django MVT](https://media.geeksforgeeks.org/wp-content/uploads/20251006115648957487/django_mvt_image_geeks_for_geeks.jpg)

- Django Model Concept and some keywords

  | Database Term  | Django Term       | What It Means                        | Example                      |
  | -------------- | ----------------- | ------------------------------------ | ---------------------------- |
  | Entity         | Model             | A real-world object                  | `StudentModel`               |
  | Attribute      | Field             | Property of an entity                | `name`, `age`                |
  | Table          | DB Table          | Stores all records of a model        | `student_table`              |
  | Record (Row)   | Model Instance    | One single data entry                | `StudentModel(name="TT")`    |
  | Primary Key    | `id` field        | Unique identifier for each record    | `id=1`                       |
  | Foreign Key    | `ForeignKey`      | Many-to-one relationship             | StudentModel → TeacherModel  |
  | Many-to-Many   | `ManyToManyField` | Many-to-many relationship            | StudentModel ↔ CourseModel   |
  | One-to-One     | `OneToOneField`   | One-to-one relationship              | UserModel ↔ ProfileModel     |
  | Query Language | ORM               | Python way to interact with database | `StudentModel.objects.all()` |
  | Schema Change  | Migration         | Updates DB structure                 | `makemigrations`             |
  | Validation     | `blank=True`      | Form-level optional field            | Empty allowed in form        |
  | DB Constraint  | `null=True`       | Database-level optional field        | NULL allowed in DB           |
  | Default Value  | `default=`        | Predefined value if none given       | `age=18`                     |
  | Metadata       | `Meta` class      | Model configuration                  | ordering, table name         |
  | Representation | `__str__()`       | Human-readable object name           | `"TT"`                       |

- Now we will create model in [school_app/models.py](./school_app/models.py)

  ```py
  from django.db import models

  class TeacherModel(models.Model):
      name = models.CharField(max_length=100)
      address = models.CharField(max_length=100) # we can use `TextField` here as address required more character
      email = models.EmailField()
  ```
- Note: project model diagram:
![Django MVT](https://drive.google.com/file/d/1vfoJ9qP4y8dw0JVW6tA5n1NfJqKVdNli/view?usp=drive_link)

- Register this model in [admin.py](./school_app/admin.py)

  ```py
  from django.contrib import admin
  from school_app.models import *

  # Register your models here.
  admin.site.register(TeacherModel)
  ```
- Note: `from school_app.models import *` aikhane beginner stage e direct model name take import kora valo star use na kore.
---
[⬆️ Go to Index](#index)

# Django `makemigrations` vs `migrate`

- **makemigrations**
  - Creates migration files based on model changes
  - Does NOT touch the database
  - Scans models.py
  - Detects changes (new model, field, delete, etc.)
  - Generates a migration file inside:
  - `app_name/migrations/`

- **migrate**
  - Applies migration files to the database
  - Reads migration files
  - Executes SQL queries
  - Updates database schema

---
[⬆️ Go to Index](#index)

# Apply New Changes To Database

- To see current migration status

  ```sh
  py manage.py showmigrations
  ```

- Apply migration

  ```sh
  py manage.py makemigrations school_app
  py manage.py migrate school_app
  ````

> [!IMPORTANT]
>
> - Each time we create a new model
> - Each time we change anything to an existing model(modify fields)
> - We have to run both `makemigrations` and `migrate` command with app name

---
[⬆️ Go to Index](#index)

# Add Data From Admin Page

- Login using `username` and `password` which is setup during `createsuperuser` command
- Now add data
-Note: In this project, superuser login info is `username:admin` and `password:admin`
---
- For django built in admin page design "https://django-jazzmin.readthedocs.io/". Amin page theme for modern admin page design.
- Into the superadmin administrations page the teacher info is showing about : 
  TeacherModel object (1)
  If you wanted to changes that:
  
  ```bash
  from django.db import models
  class TeacherModel(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)

  def __str__(self):
    return f'{self.name}-{self.email}'
  ```
  -Notes: Views or any of works we can using to functions or class But class is more powerfull. So into the class using method of def functions which is `def __str__` Here,  `__str__`  dandar method or magic method using for modify or changes the object of the admin page.  

[⬆️ Go to Index](#index)

# Show Data In Frontend

- Create [templates](./templates/) folder in project root directory where [manage.py](./manage.py) is
- Add template path in [settings.py](./school_project/settings.py)
  - Create files by following structure
    ```txt
    📁 templates
    ├── 📁 master
    │   ├── 🌐 base.html
    │   └── 🌐 nav.html
    ├── 🌐 home.html
    └── 🌐 teacher.html
    ```
  - Apply bootstrap in base.html
  
  - Here into nav.html:
  
  ```sh
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="{% url 'home_page' %}">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="{% url 'teacher' %}">Teacher</a>
        </li>
      </ul>
    </div>
  </div>
  </nav>
  ```
  - Create function in [views.py](./school_project/views.py)

  -Notes: If you want to quickly looking for function location then `ctrl`+ `click teacher_page(function name)` the `views.py` page is showing in the located function. 
  ```sh
  from django.contrib import admin
  from django.urls import path 
  from .views import home_page, teacher_page
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page, name='home_page'),
    path('teacher-page',teacher_page, name='teacher'),
  ]
  ```
  - Add `urlpatterns` in [urls.py](./school_project/urls.py)

- Now in teacher function which we created in [views.py](./school_project/views.py) we need to get data from the database

  ```py
  from django.shortcuts import render
  from school_app.models import TeacherModel

  def teacher_page(request):

    teacher_data=TeacherModel.objects.all()

    context={
      'teacher_data':teacher_data
    }

    return render(request,'teacher.html',context=context)
  ```

- In HTML page which is [teacher.html](./templates/teacher.html) we will use a bootstrap table where Django template `for loop` will be used to `iterate` over the data, and the values will be displayed using `{{ }}` syntax.

  ```jinja
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Email</th>
        <th scope="col">Address</th>
      </tr>
    </thead>
    <tbody>
      {% for teacher in teacher_data %}
      <tr>
        <td>{{teacher.name}}</td>
        <td>{{teacher.email}}</td>
        <td>{{teacher.address}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  ```
---
[⬆️ Go to Index](#index)

# 🤝 Contributing

Contributions are always welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

# Author

- Md. Nazmul Ali Biswas
- Fullstack Engineer & Tech Enthusiast
- Contact: nazmulalibiswas.dev@gmail.com

# 📬 Contacts

- Web: www.nazmulalibiswas.com
- Email: nazmulalibiswas.dev@gmail.com
- Phone: +88 01518365796