from django.contrib import admin

# Register your models here.
from .models import *

admin.register(User)
admin.register(Class)
admin.register(UserClass)
