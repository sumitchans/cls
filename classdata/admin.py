from django.contrib import admin

# Register your models here.
from .models import UserClass, User, Class

admin.site.register(User)
admin.site.register(Class)
admin.site.register(UserClass)
