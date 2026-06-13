# Index

- [Index](#index)
  - [HTML Templates](#html-templates)
  - [Django Template Setup](#django-template-setup)
  - [Context Data](#context-data)
  - [Navigation Page using URL name](#navigation-page-using-url-name)

# HTML Templates

- Django has default templates language (DTL). Django Template Language is Django's built-in templating engine. It is designed to strike a balance between power and ease of use, allowing developers to cleanly separate the visual presentation layer (HTML) from the backend business logic (Python).

- 1. Variables
  Variables allow you to insert dynamic data into your HTML. They are passed from your Django view to the template via a dictionary known as a "context."
    - Syntax: {{ variable_name }}
    - Dot Notation: You can use a dot (.) to access dictionary keys, object attributes, method calls, or list indices.
  Example:
  ```py
    <h1>Welcome back, {{ user_name }}!</h1>
    <p>You are {{ profile.age }} years old.</p>
  ```
- 2. Tags
  Tags provide logic in the rendering process. They are used to execute control structures (like loops and conditionals), load external assets, or format text.
    - Syntax: {% tag_name %}

    - The if Statement
      Evaluates a condition. If it is true, the block is rendered.
  
    ```py
    {% if messages_count > 0 %}
      <p>You have {{ messages_count }} new messages.</p>
    {% elif is_admin %}
      <p>Welcome, Admin. No new messages.</p>
    {% else %}
      <p>Your inbox is empty.</p>
    {% endif %}
    ```

    - The for Loop
    Iterates over lists, arrays, or querysets.
    ```py
    <ul>
    {% for item in shopping_list %}
        <li>{{ item }}</li>
    {% empty %}
        <li>Your cart is empty!</li>
    {% endfor %}
    </ul>
    Note: The {% empty %} tag is an excellent built-in fallback that triggers if the list you are looping over is empty or does not exist.
    ```
- 3. Filters
  Filters transform or format the values of variables before they are rendered on the page.
    - Syntax: {{ variable_name|filter_name }}

    - Chaining: Filters can be chained sequentially (example: {{ text|lower|capfirst }}).
    - Arguments: Some filters take arguments, appended with a colon (example: {{ text|truncatewords:30 }}).
  
    ```py
    <p>{{ user_name|capfirst }}</p>

    <p>Status: {{ user_status|default:"Offline" }}</p>

    <p>Joined on: {{ join_date|date:"F j, Y" }}</p>
    ```
- 4. Comments
  Comments are used to leave notes for developers. The template engine ignores them, and they will not appear in the final HTML source code sent to the browser.
  - Single-line: {# This is a single-line comment #}
  
  Multi-line:
  ```py
    {% comment %}
    This is a multi-line comment.
    You can temporarily disable chunks of HTML or logic here.
    {% endcomment %}
  ```
- 5. Template Inheritance (The Most Powerful Feature)
  Template inheritance allows you to build a base "skeleton" document containing your site's common UI elements (headers, footers, navigation) and defines blocks that child templates can override. This prevents you from repeating the same HTML on every page.
  - Step 1: Create the Base Template (base.html)
  ```py
    <!DOCTYPE html>
    <html>
    <head>
        <title>{% block title %}My Default Website{% endblock %}</title>
    </head>
    <body>
        <nav>Navigation Bar</nav>

        <main>
            {% block content %}
            {% endblock %}
        </main>

        <footer>Copyright 2026</footer>
    </body>
    </html>
  ```

  - Step 2: Create the Child Template (about.html)
  ```py
    {% extends "base.html" %}

    {% block title %}About Us - My Website{% endblock %}

    {% block content %}
        <h1>About Our Company</h1>
        <p>We build awesome Django applications!</p>
    {% endblock %}
  ```
---
[⬆️ Go to Index](#index)

# Django Template Setup

- Create a folder [templates](./templates/) in project base directory where [manage.py](./manage.py) is
- Add this [templates](./templates/) path in [settings.py](./templates_render_project/settings.py)

  ```py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR,"templates"],
          ...
      },
  ]
  ```

- Now create a function inside [views.py](./templates_render_project/views.py) `home_page()` by importing `render` function from `django.shortcuts` using *selective import* and render [home.html](./templates/home.html)

  ```py
  from django.shortcuts import render

  def home_page(request):
    return render(request,'home.html')

  def about_page(request):
    return render (request, 'about.html')

  def contact_page(request):
    return render (request, 'contact.html')
  ```

- Add it inside `urlpatterns`

  ```py
  from django.contrib import admin
  from django.urls import path
  from .views import *

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', home_page, name='home'),
      path('about/', about_page, name='about'),
      path('contact/', contact_page, name='contact'),
  ]
  ```

  - Now visit http://127.0.0.1:8000/ to see the output

---
[⬆️ Go to Index](#index)

## Context Data

- Inside the `home_page()` function, create a dictionary and pass it to the template using `context`.

  ```py
  from django.shortcuts import render

  def home_page(request):
    info = {
      "name": "nazmulalibiswas",
      "address": "Dhaka"
    }
    return render(request, 'home.html', info)

  def about_page(request):
    return render (request, 'about.html')

  def contact_page(request):
    return render (request, 'contact.html')
  ```

- Now inside [home.html](./templates/home.html) use Django Template Language (DTL) to display data passed from the view.
- Variables are accessed using double curly braces `{{ }}`.

  ```jinja
  <h1>Hello {{ name }}</h1>
  <h1>from {{ address }}</h1>
  ```

---
[⬆️ Go to Index](#index)

## Navigation Page using URL name

- Create another function `about_page()` and `contact_page()`
- and render [about.html](./templates/about.html)

  ```py
  def about_page(request):
    return render(request,'about.html')

  def contact_page(request):
    return render (request, 'contact.html')
  ```

- Add it inside `urlpatterns` in [urls.py](./templates_render_project/urls.py)

  ```py
  from django.contrib import admin
  from django.urls import path
  from . import views

  urlpatterns = [
      ...
      path('about/',views.about_page,name='about'),
      path('contact/', contact_page, name='contact'),
  ]
  ```

- Use the URL name in the template for navigation

  ```jinja
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'about' %}">About</a>
  ```

> [!NOTE]
>
> - We will add this in both [home.html](./templates/home.html) and [about.html](./templates/about.html)
>
> - Note that we will do this in better way in future by learning template mastering

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