from django.contrib import admin
from .models import Post #11 import your model

#12 Register your models here.
admin.site.register(Post)

#13 create adminuser - python manage.py createsuperuser
#14 go to site urls