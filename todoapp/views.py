from django.shortcuts import render
from .models import TodolistItem
from django.http import HttpResponseRedirect

# Create your views here.


def todoappView(request):
    all_todo_items = TodolistItem.objects.all()
    return render(request, 'todoapp/todolist.html', {'all_items': all_todo_items})


def addTodoView(request):
    x = request.POST['content']
    new_item = TodolistItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp')
