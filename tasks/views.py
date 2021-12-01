from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
