from django.contrib import admin

# Register your models here.
from todoapp.models import TodolistItem
admin.site.register(TodolistItem)
