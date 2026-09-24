from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def task_index(request):
    return render(request, 'task/index.html')


@login_required
def task_create(request):
    pass


@login_required
def task_read(request, pk):
    pass


@login_required
def task_update(request, pk):
    pass


@login_required
def task_delete(request, pk):
    pass

