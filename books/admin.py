from django.contrib import admin
from .models import Resource, User, Category

# Register your models here.
admin.site.register(Resource)
admin.site.register(User)
admin.site.register(Category)
