# Django Demo App

## 🚀 Introduction
This is a simple Django web application with a modular structure. It includes an example `tasks` app that demonstrates basic routing, views, and URL mapping.

## 📁 Project Structure
```
django_demo/
│── django_demo/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── tasks/
│   │── migrations/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── tests.py
│   │── views.py
│   │── urls.py
│
│── manage.py
│── requirements.txt
│── README.md
```

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/anubhavanand1516/django_demo.git
cd django_demo_app
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate 
```

### 3️⃣ Install Dependencies
```bash
pip install django
```

### 4️⃣ Create a Django App
```bash
python manage.py startapp tasks
```

### 5️⃣ Register the App
Edit `settings.py` and add `'tasks'` to `INSTALLED_APPS`.

### 6️⃣ Define URLs
- Create `tasks/urls.py` and add:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

- Update `django_demo_app/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
```

### 7️⃣ Create a Simple View
Edit `tasks/views.py`:
```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Tasks App!")
```

### 8️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 9️⃣ Create a Superuser (For Admin Panel)
```bash
python manage.py createsuperuser
```

### 🔟 Run the Server
```bash
python manage.py runserver
```

## 🌐 Access the App
- **Home Page**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (Login using superuser credentials)

