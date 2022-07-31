# django-admin-persian-fonts
django-admin-persian-fonts is a Django app for fast and easy use of Persian fonts in the Django admin panel.
## Installation
- Run `pip install django-admin-persian-fonts`
- Add `admin_persian` to `settings.INSTALLED_APPS` **before** `django.contrib.admin`
```python
INSTALLED_APPS = (
    #...
    "admin_persian",
    #...
    "django.contrib.admin",
    #...
)

```
- Run `python manage.py migrate`
- Restart your application server
- Visit http://127.0.0.1:8000/admin/