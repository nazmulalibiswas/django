# Index

- [Context](#index)
  - [Create Django project](#create-django-project)
  - [Project Structure](#project-structure)
  - [Hello World Show on Webpage](#hello-world-show-on-webpage)
  - [Create Superuser](#create-superuser)
  - [HttpResponse](#httpresponse)

# Create Django project

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
  django-admin startproject myproject .
  ```

- Run the server

  ```sh
  py manage.py runserver
  ```

  - now open http://127.0.0.1:8000/ in the browser

---
[⬆️ Go to Context](#index)


# Project Structure
## After Creating

- Project Folder:
--Project Structure without app

```sh
├── MyProject/             # প্রজেক্টের মেইন কনফিগারেশন ডিরেক্টরি (Core Configuration Folder)
│   ├── __pycache__/       # পাইথন কোড দ্রুত রান করার জন্য অটো-জেনারেটেড ক্যাশ ফাইল (এটি ডিলিট করলেও সমস্যা নেই)
│   ├── __init__.py        # এই ফোল্ডারটিকে পাইথন যেন একটি 'Package' হিসেবে চেনে, তাই এই খালি ফাইলটি থাকে
│   ├── asgi.py            # Asynchronous সার্ভার (যেমন: WebSockets, Chat app, Real-time notification) হ্যান্ডেল করার কনফিগারেশন
│   ├── settings.py        # পুরো প্রজেক্টের মেইন কন্ট্রোল প্যানেল (Database, Installed Apps, Middleware, Static files এর সব সেটিংস এখানে থাকে)
│   ├── urls.py            # প্রজেক্টের মেইন রাউটিং ফাইল (কোন ইউআরএল/লিংক এ হিট করলে কোন পেজ ওপেন হবে তা এখানে ঠিক করা হয়)
│   └── wsgi.py            # ট্র্যাডিশনাল ওয়েব সার্ভারে (যেমন: Apache, Nginx) প্রজেক্ট ডিপ্লয় বা লাইভ করার জন্য কনফিগারেশন
│
├── db.sqlite3             # Django ডিফল্ট ডাটাবেজ ফাইল (লোকাল ডেভেলপমেন্টের জন্য এটি অটোমেটিক তৈরি হয়)
└── manage.py              # Django মেইন কমান্ড-লাইন টুল (সার্ভার রান করা, ডাটাবেজ মাইগ্রেশন করা বা নতুন অ্যাপ তৈরি করার কমান্ড এটি দিয়ে দিতে হয়)
```

--Project Structure with app

  ```sh
├── ManageCash/                       # Django অ্যাপ ফোল্ডার (এখানে অ্যাপের মূল ফিচার ও লজিক থাকে)
│   ├── __pycache__/                  # পাইথন কোড দ্রুত রান করার জন্য অটো-জেনারেটেড ক্যাশ ফাইল
│   ├── migrations/                   # ডাটাবেজ টেবিল তৈরি বা পরিবর্তনের ইতিহাস (History) এখানে জমা থাকে
│   ├── static/bootstrap              # বুটস্ট্র্যাপের CSS, JS এবং ডিজাইন ফাইল রাখার ফোল্ডার
│   ├── templates/                    # এই অ্যাপের ভেতরের HTML ফাইলগুলো রাখার ফোল্ডার
│   ├── __init__.py                   # ফোল্ডারটিকে পাইথন প্যাকেজ হিসেবে চেনানোর জন্য খালি ফাইল
│   ├── admin.py                      # Django অ্যাডমিন প্যানেলে মডেল বা ডাটাবেজ টেবিল শো করার জন্য ফাইল
│   ├── apps.py                       # এই 'ManageCash' অ্যাপটির নিজস্ব কনফিগারেশন ফাইল
│   ├── forms.py                      # ইউজার ইনপুট বা ফর্ম ডিজাইন এবং ভ্যালিডেশন করার ফাইল
│   ├── models.py                     # ডাটাবেজের টেবিল বা স্কিমা (Schema) তৈরি করার মেইন ফাইল
│   ├── tests.py                      # অ্যাপের কোড ঠিকঠাক কাজ করছে কিনা তা পরীক্ষা (Unit Test) করার ফাইল
│   ├── urls.py                       # এই নির্দিষ্ট অ্যাপের ইউআরএল বা রাউটিং লিংকগুলো সেট করার ফাইল
│   └── views.py                      # ডাটা প্রসেস করে এইচটিএমএল পেজে পাঠানোর মূল লজিক লেখার ফাইল
│
├── nazmul_101_ManageCash/            # মেইন প্রজেক্ট কনফিগারেশন ফোল্ডার (Core Configuration Folder)
│   ├── __pycache__/                  # কনফিগারেশন ফাইলের পাইথন ক্যাশ ফোল্ডার
│   ├── __init__.py                   # এই মেইন ফোল্ডারটিকে পাইথন প্যাকেজ হিসেবে চেনানোর ফাইল
│   ├── asgi.py                       # রিয়েল-টাইম ফিচার (যেমন: চ্যাট, নোটিফিকেশন) হ্যান্ডেল করার Asynchronous সার্ভার কনফিগারেশন
│   ├── settings.py                   # পুরো প্রজেক্টের মেইন কন্ট্রোল প্যানেল (Database, Apps, Middleware এর সব সেটিংস এখানে থাকে)
│   ├── urls.py                       # পুরো প্রজেক্টের মেইন ইউআরএল ডিরেক্টরি (এখান থেকে বিভিন্ন অ্যাপের ইউআরএল-কে কানেক্ট করা হয়)
│   └── wsgi.py                       # প্রোডাকশন সার্ভারে (যেমন: Nginx, Apache) প্রজেক্ট লাইভ করার কনফিগারেশন ফাইল
│
└── .gitignore                        # গিটহাবে (GitHub) কোড পুশ করার সময় কোন কোন ফাইল/ফোল্ডার বাদ দিতে হবে (যেমন ক্যাশ ফাইল, লোকাল ডাটাবেজ) তার তালিকা
  ```
---
[⬆️ Go to Context](#index)

# Hello World Show on Webpage
  -  Create a file 'views.py' in the my project
    ```sh
  from django.http import HttpResponse

  def home_page(request):

      return HttpResponse("Hello, World!")

  def about_page(request):

      return HttpResponse("About Page")

  ```
  -  Now go to 'urls.py' in the my project & declare the url
    ```sh
  from django.contrib import admin
  from django.urls import path
  from myproject.views import home_page, about_page

  urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home_page, name='home'),
    path('about/',about_page, name='about'),
  ]

  - Now visit http://127.0.0.1:8000/ to see the output write on the url path:  http://127.0.0.1:8000/home/ directory or http://127.0.0.1:8000/about/
         
  ```
---
[⬆️ Go to Context](#index)

# Create Superuser

- For login build in admin panel we have to need create superuser. So we have to need createsuperuser

- By default database (db.sqlite3) need to ready first & detected all of changes create migrations file  
  ```sh
  py manage.py makemigrations
  ```
- To Create Superuser in new project first we need to migrate it for apply on the database

  ```sh
  py manage.py migrate
  ```
- Now go db.sqlite3 for see the database changes data but we need to install one VS code extensions:
"SQLite Viewer - Florian Klampfer" then we can see all of data on the database

- To Create Superuser in new project first we need to migrate it for apply on the database

  ```sh
  py manage.py createsuperuser
  ```

  - Setup username and password (Like this : username:nazmulalibiswas, email:nazmulalibiswas.dev@gmail.com, password: 1234 Password(again):1234 )
  - Now go to http://127.0.0.1:8000/admin and enter that username and password to login

---
[⬆️ Go to Context](#index)

# HttpResponse

- Simple *"Hello World"* text show using `HttpResponse`
  - Create [firstProject/views.py](./firstProject/views.py) file inside project directory

    ```py
    from django.http import HttpResponse

    def home_page(request):
      msg="Hello World"
      return HttpResponse(msg)
    ```

  - Now add this function in the [firstProject/urls.py](./firstProject/urls.py) file path list

    ```py
    from django.contrib import admin
    from django.urls import path
    from . import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.home_page,name='home')
    ]
    ```

  - Now visit http://127.0.0.1:8000/ to see the output
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