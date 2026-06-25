# Index

- [Index](#index)
  - [Project Setup](#project-setup)
  - [Setup Everything Inside App](#setup-everything-inside-app)
  - [Model Create ](#model-create)
  - [Template Mastering](#template-mastering)

# Project Setup
- In a desktop place, Press (Windows+R) key then type `cmd` on run command press enter to open command prompt
- mkdir "Folder_name" like:nazmulalibiswas
- cd nazmulalibiswas
- Now setup here :
  ```bash
  python -m venv env
  ```
- Activate now 
  ```bash
  .\env\Scripts\activate
  ```
- After active virtual env type
  ```bash
  pip install django pillow
  ```
- Now setup django project
  ```bash
  django-admin startproject filter_get_project
  ```
- Now go to project directory
  ```bash
  cd fileter_get_project
  ```
- Now crete app into the project directory
  ```bash
  python manage.py startapp new_app
  ```
- Run the project for VS code
  ```bash
  code .
  ```
---
[⬆️ Go to Index](#index)

# Setup Everything Inside App
- Now go to settings.py file & makesure the app name inclding here
  ```bash
  INSTALLED_APPS = [
    'django.contrib.admin',
    .......................,

    #app
    'new_app'
  ]
  ```
- Now creates a `templates` folder into your new_app folder 
- Now creates a master folder into templates file for base.html & nav.html file.

---
[⬆️ Go to Index](#index)

# Model Create
- Create `studentModel` model inside [models.py](./new_app/models.py)
  ```bash
  from django.db import models

  class StudentInfoModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/student_img')
    department = models.CharField()
  ```
- Now declare choice field first
  ```bash
  from django.db import models

  class StudentInfoModel(models.Model):
    DEPT_TYPES = [
      ('cse', 'CSE'),
      ('eee', 'EEE'),
      ('civil', 'CIVIL'),
    ]
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    image = models.ImageField(upload_to='media/student_img')
    department = models.CharField()
  ```
-Notes: When we are using choice field for model into the left one is machine readable. So In database user searching CSE then not understanding beacuse its not small letter word which is declare already so must need to searching 'cse'. When we are using that for logic or calculation then using for left one. And using right one is for human readable so that it will be showing admin page.

- Now department types declare
 ```bash
    department = models.CharField(choices=DEPT_TYPES, max_length=10)
  ```
- Finally declare the str function
 ```bash
    department = models.CharField(choices=DEPT_TYPES, max_length=10)

    def __str__(self):
      return f'{self.name}-{self.department}'
  ```
- Now database model is ready so that now needed for 
  ```bash
    python manage.py makemigrations
  ```
- Notes: here makemigrations works for which I created model into the database, these changes creates and detect for makemigrations & make a migrations files.
- Second time makemigrations need to mentions app name for safe zone 
  ```bash
    python manage.py makemigrations new_app
  ```
- Now changes and create are need to confirmation for use migrate 
  ```bash
    python manage.py migrate
  ```
- Finally need to create superuser for superadmin
  ```bash
    python manage.py createsuperuser
  ```
- Here need to declare some of the command like these
  ```bash
    username: nazmulalibiswas
    Email address: nazmulalibiswas.dev@gmail.com
    password: 1234
    confirm password: 1234
  ```
- Finally run the runserver
  ```bash
    python manage.py runserver
  ```
- Now when youre visiting the superadmin page there are not showing updated or created model beacuse need to register it into `admin.py` file
  ```bash
    from django.contrib import admin
    from new_app.models import * # Here need to import model which we are already creating into the models.py file

    admin.site.register(StudentInfoModel)
  ```
- Now go and check the superadmin page to the model are showing properly.

---
[⬆️ Go to Index](#index)

# Template Mastering

- Go [templates](./new_app/templates/) folder inside create folder [master](./new_app/templates/master)
- Into the master folder create the file base.html and nav.html
- Now go to bootstrap 5 and go the startep template now copy it and paste into base.html file.
```bash
  <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    -->
  </body>
</html>
```
- And searching `nav` in the bootstrap search icon then copy the navbar which one is youre wanted to use - copy now and paste it into `nav.html`file
```bash
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
  </nav>
```
- Now connect nav with `base.html`
```bash
  <!doctype html>
  <html lang="en">
    <head>

      <title>Hello, world!</title>
    </head>
    <body>
      {% include 'master/nav.html' %}

      {% blcok content %}

      {% endblock content %}

      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    </body>
  </html>
```
- To show `StudentInfoModel` data we will create an HTML page [student-info.html](./new_app/templates/student-info.html)

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base.html
  │   └── 🌐 nav.html
  └── 🌐 student-info.html
  ```
- Now update `student-info.html`
```bash
{% extends 'master/base.html' %} 
{% block content %}
<h1> Student List</h1>

{% endblock content %}
```
- Now Show the student list, we have need to create functions into `views.py`
  ```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model

  def student_info_view(request):

    return render(request, 'student-info.html')
  ```
- Now connect function with urls so create into new_app directory to create `urls.py` files
  ```bash
  from django.urls import path
  from new_app.views import *

  urlpatterns = [
    path('', student_info_view, name = 'student_info_view'),
  ]
  ```
- Now using name parameter into `nav.html`
  ```bash
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" aria-current="page" href="{% url 'student_info_view' %}">Students</a>
        </li>
      </ul>
    </div>
  </div>
  </nav>
  ```
- Now go to the project and connect with app with the project `urls.py`
  ```bash
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('new_app.urls')),
  ]
- Now complete the template inheritance. Showing data need to table so go now bootstrap and copy table calss `class="table table-striped` and go now `student-info.html`
- Now crate a table tag and into the tag paste the class
```bash
{% extends 'master/base.html' %} 
{% block content %}
<h1> Student List</h1>

<table class="table table-striped">
    <thead>
      <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Image</th>
      <tr>
    </thead>
</table>
```
- Notes: In the frontend page we are showing data so first check the url `path('', student_info_view, name = 'student_info_view'),` here click (CTRL + FUNCTION NAME like : student_info_view) then it goes into `views.py` file now where make a logic to passing data on frontend. 
- In this `student-info.html` page showing data must need to logic this relevant functions for passing data.
  ```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model

  def student_info_view(request):
  
  # first work is all data need to fetch and bring from database
  # Beacuse What is ORM? ORM-Object Relational Mapping. ORM benefit is SQL Query has a system like raw sql into (*Select, *Insert, *Start *Into). So ORM is a method which have all of framework and does it internally set or raw sql but we are only calling it like (object.all) but this sql method is (select start from table_name) So In this Backend working raw SQL. So what we are use like filter(), get() all of built in django ORM. When we searching anything from database then need to query.
  
  student_data = StudentInfoModel.objects.all()

  # why using context or make dictionary. Because of when passing data on html, know that html is load from render and passing data must be send it like dictionary  
  context = {
    'student_data': student_data # here key is 'student_data' and value is student_data
  }


    return render(request, 'student-info.html', context)
  ```
- Data passing is now over, showing data on `student-info.html` page go and 
```bash
{% extends 'master/base.html' %} 
{% block content %}
<h1> Student List</h1>

<table class="table table-striped">
    <thead>
      <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Image</th>
      <tr>
    </thead>
    #Here now write loop for showing data on the page
  <tbody>
    {% for student in student_data %} #student_data is come to `key` of the dictionary from `views.py`
      <tr>
        <td>{{student.name}} </td>
        <td>{{student.department}}</td>
        <td>
        <img src ="/{{student.image}}" alt="" width="50px"/>
        </td>
      </tr>
    {% endfor %}
  <tbody>
</table>
```
- Here image are not showing so that go to the web of `https://docs.djangoproject.com/en/6.0/howto/static-files/` and copy the `+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)` and paste it into the app `urls.py` and copy the `from django.conf import settings`and `from django.conf.urls.static import static` add the first import zone:
```bash
  from django.urls import path
  from new_app.views import *
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
    path('', student_info_view, name = 'student_info_view'),
  ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  ```
- Now add some data from django super admin page and check it work properly or not.

- Now in the frontend page need to bring dropdown method added which is showing the deparment related data only
- Go to the bootstrap and search `form` and copy then paste it `student-info.html`
```bash
{% extends 'master/base.html' %}
{% block content %}
<h1> Student List</h1>
# paste here the form
# <div class="row g-3 align-items-center">
#   <div class="col-auto">
#     <label for="inputPassword6" class="col-form-label">Password</label>
#   </div>
#   <div class="col-auto">
#     <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
#   </div>
#   <div class="col-auto">
#     <span id="passwordHelpInline" class="form-text">
#       Must be 8-20 characters long.
#     </span>
#   </div>
# </div>
# Now changes the unnessesary data
<form action=""> #here form is using for data post, create, search, filter etc
  <div class="row g-3 align-items-center">
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
  <div class="col-auto">
    <button type= "submit" class="btn btn-primary">Filter</button>
  </div>
</div>
</form>
<table class="table table-striped">
    <thead>
      <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Image</th>
      <tr>
    </thead>
    #Here now write loop for showing data on the page
  <tbody>
    {% for student in student_data %} #student_data is come to `key` of the dictionary from `views.py`
      <tr>
        <td>{{student.name}} </td>
        <td>{{student.department}}</td>
        <td>
        <img src ="/{{student.image}}" alt="" width="50px"/>
        </td>
      </tr>
    {% endfor %}
  <tbody>
</table>
```
- Now needed `select` tag for go to the bootstrap and search select then copy it and paste it into the replace of input
```bash
<select class="form-select" aria-label="Default select example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```
- Lets now: 
```bash
{% extends 'master/base.html' %}
{% block content %}
<h1> Student List</h1>
<form action=""> #here form is using for data post, create, search, filter etc
  <div class="row g-3 align-items-center">
  <div class="col-auto">
  #paste here for dropdown panel now change it the subject name
  <select class="form-select" aria-label="Default select example">
  <option selected>All</option>
  <option value="1">CSE</option>
  <option value="2">EEE</option>
  <option value="3">Civil</option>
  </select>

  </div>
  <div class="col-auto">
    <button type= "submit" class="btn btn-primary">Filter</button>
  </div>
</div>
</form>
<table class="table table-striped">
    <thead>
      <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Image</th>
      <tr>
    </thead>
    #Here now write loop for showing data on the page
  <tbody>
    {% for student in student_data %} #student_data is come to `key` of the dictionary from `views.py`
      <tr>
        <td>{{student.name}} </td>
        <td>{{student.department}}</td>
        <td>
        <img src ="/{{student.image}}" alt="" width="50px"/>
        </td>
      </tr>
    {% endfor %}
  <tbody>
</table>
```
- Now the data are showing but margin and padding problem fixing for go to the base and type container
```bash
  <!doctype html>
  <html lang="en">
    <head>

      <title>Hello, world!</title>
    </head>
    <body>
      {% include 'master/nav.html' %}

      <div class="container">
      {% blcok content %}

      {% endblock content %}
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    </body>
  </html>
```
- Now we are showing specific data on the Student List so using filter() to resolve it
- ```bash
  student_data = StudentInfoModel.objects.all()
  student_data = StudentInfoModel.objects.filter(department='cse') # .all() to .filter()
  ```
- Now go to the student-info.html and edit into form tag for data get method:
  ```bash
  <form method='POST'>
  ......................
    <select class='form-select' name='dept_name' aria-label='Default select example'> #here need to given at name attributes
  ```
- now go to view and get() name attributes:
```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model


  def student_info_view(request):
  
  student_data = StudentInfoModel.objects.all()
  student_data = StudentInfoModel.objects.filter(department='cse') # .all() to .filter()
  filter_option = request.GET.get('dept_name')

  
  student_data = StudentInfoModel.objects.all()

  context = {
    'student_data': student_data # here key is 'student_data' and value is student_data
  }


    return render(request, 'student-info.html', context)
```

- Value are showing 2 beacuse need to changing value so that the:
```bash
<select class="form-select" aria-label="Default select example">
  <option value="all">All</option>
  <option value="cse">One</option> #change the value="1" to value="cse" and value="2" to value="eee" and value="3" to value="civil"
  <option value="eee">Two</option>
  <option value="civil">Three</option>
</select>
```
- now go to view and get() name attributes:
```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model


  def student_info_view(request):
  
  student_data = StudentInfoModel.objects.all()
  student_data = StudentInfoModel.objects.filter(department='filter_option') # change it to filter option

  
  student_data = StudentInfoModel.objects.all()

  context = {
    'student_data': student_data 
  }
  return render(request, 'student-info.html', context)
```

- now go all are not filtering so that we are now using conditions and lets create a logic now :
```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model


  def student_info_view(request):
  filter_option = request.GET.get('dept_name')

  student_data = StudentInfoModel.objects.all()
  
  student_data = StudentInfoModel.objects.all()
  if filter_option:
    if filter_option == 'all':
        student_data = StudentInfoModel.objects.all()
    else:
        student_data = StudentInfoModel.objects.filter(department=filter_option)
        
  context = {
    'student_data': student_data 
  }
  return render(request, 'student-info.html', context)
```
- Now,
```bash
{% extends 'master/base.html' %}
{% block content %}
<h1> Student List</h1>
<form action=""> #here form is using for data post, create, search, filter etc
  <div class="row g-3 align-items-center">
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
  <div class="col-auto">
    <button type= "submit" class="btn btn-primary">Filter</button>
  </div>
  <div class= 'auto'>
  <a href="{% url 'student_info_view' %}" class="btn btn-danger">Clear</a> # create a clear button for reset data & call it from name parameter to declare the url into href
  </div>
</div>
</form>
<table class="table table-striped">
    <thead>
      <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Image</th>
      <tr>
    </thead>
    #Here now write loop for showing data on the page
  <tbody>
    {% for student in student_data %} #student_data is come to `key` of the dictionary from `views.py`
      <tr>
        <td>{{student.name}} </td>
        <td>{{student.department}}</td>
        <td>
        <img src ="/{{student.image}}" alt="" width="50px"/>
        </td>
      </tr>
    {% endfor %}
  <tbody>
</table>
```
- If we want to the selected department data is on selecting then :
```bash
  from django.shortcuts import render
  from new_app.models import * # here are must need to import the model


  def student_info_view(request):
  filter_option = request.GET.get('dept_name')

  student_data = StudentInfoModel.objects.all()
  
  student_data = StudentInfoModel.objects.all()
  if filter_option:
    if filter_option == 'all':
        student_data = StudentInfoModel.objects.all()
    else:
        student_data = StudentInfoModel.objects.filter(department=filter_option)
        
  context = {
    'student_data': student_data
    'filter_option': filter_option,
  }
  return render(request, 'student-info.html', context)
```
- Now go to `student-info.html` and 
```bash
<h1> Student List of {{filter_option}}</h1>
```
- For option selected need to
```bash
<option value='cse'
{% if filtered_option == 'cse' %}
  selected
{% endif %}
>

<option value='eee'
{% if filtered_option == 'eee' %}
  selected
{% endif %}
>

<option value='civil'
{% if filtered_option == 'civil' %}
  selected
{% endif %}
>
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