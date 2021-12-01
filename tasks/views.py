from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.core import serializers

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET', 'POST', 'DELETE'])
def task_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        task = Task.objects.get(pk=pk)
        
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        all_tasks = Task.object.all()
        # serializer = TaskSerializer(all_tasks)
        json_response = serializers.serialize("json", all_tasks)
        return HttpResponse(json_response, content_type="application/json")

    elif request.method == 'POST':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)