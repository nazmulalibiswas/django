# Index

- [Index](#Index)
  - [Start with Django Web Framework](#start-with-django-web-framework)
  - [What is Django?](#what-is-django)
  - [Why use Django?](#why-use-django)
  - [Key Features of Django](#key-features-of-django)
  - [History of Django](#history-of-django)
  - [The MVT Architecture](#the-mvt-architecture)
  - [Setup First Django Project](#setup-first-django-project)

# Start with Django Web Framework

## What is Django?

- Django is a high-level Python web framework
- It helps developers build secure and scalable web applications
- Comes with many built-in features

---
[⬆️ Go to Context](#Index)

## Why use Django?

- Fast development
- Built-in admin panel
- Secure - Protection against common attacks ( SQL injection, CSRF Protection,  Cross-Site Scripting (XSS Protection), etc.)
- Scalable for large applications
- Clean and readable code structure

---
[⬆️ Go to Context](#Index)

## Key Features of Django

- ORM (Object Relational Mapper)
- Built-in authentication system
- URL routing system
- Admin dashboard
- Form handling
- Middleware support

---
[⬆️ Go to Context](#Index)

## History of Django

- Django was invented by Lawrence Journal-World in 2003
- Initial release to the public was in July 2005
- Latest version of Django is 6.0.4 (April 7, 2026)

---
[⬆️ Go to Context](#Index)

## The MVT Architecture

> Django follows the MVT (Model-View-Template) architectural pattern, which is a variation of the traditional MVC (Model-View-Controller) design pattern used in web development. This pattern separates the application into three main components:

| Concept    | MVC                  | Django (MVT)                |
| ---------- | -------------------- | --------------------------- |
| Model      | Handles data & logic | Handles data & logic        |
| View       | UI layer             | **Template (HTML)**         |
| Controller | Handles user input   | **View (Python functions)** |
| Framework  | Passive              | **Active controller**       |

![Django Request Response Cycle](https://i.imgur.com/WvqUs8P.gif)

- Model (same as MVC): Manages the data — built using Django’s ORM. Defines the structure of your database.
- View (different from MVC): In Django, the “View” contains the business logic. It fetches data from the model and passes it to the template.
- Template: Responsible for rendering the final HTML — your front-end content.

---
[⬆️ Go to Context](#Index)

## Setup First Django Project

- Create virtual environment

  ```sh
  py -m venv .venv
  ```

- Activate `.venv`

  ```sh
  .venv\Scripts\activate
  ```

- Install [Django](https://pypi.org/project/Django/)

  ```sh
  pip install Django
  ```

- Create first project (passing `.` to create the project in the current directory)

  ```sh
  django-admin startproject firstProject .
  ```

- Run the server

  ```sh
  py manage.py runserver
  ```

  - now open http://127.0.0.1:8000/ in the browser

---
[⬆️ Go to Context](#Index)


## 🤝 Contributing

Contributions are always welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

## Author

- Md. Nazmul Ali Biswas
- Fullstack Engineer & Tech Enthusiast
- Contact: nazmulalibiswas.dev@gmail.com

## 📬 Contacts

- Web: www.nazmulalibiswas.com
- Email: nazmulalibiswas.dev@gmail.com
- Phone: +88 01518365796