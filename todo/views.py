from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, NewTodoForm


def index(request):
    todo_list = Todo.objects.order_by('id')
    # form = TodoForm()
    newtodoform = NewTodoForm()
    context = {'todo_list': todo_list, 'form': newtodoform}
    template = 'todo/index.html'
    return render(request, template, context)


@require_POST
def add_todo(request):
    # form = TodoForm(request.POST)

    newtodoform = NewTodoForm(request.POST)
    if newtodoform.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        new_todo = newtodoform.save()

    return redirect('todo:index')


def complete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo:index')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo:index')


def delete_add(request):
    Todo.objects.all().delete()

    return redirect('todo:index')



