from django.http import HttpResponse, JsonResponse, Http404
from .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers

# Create your views here.




def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

@api_view(['GET'])
def get_all_tasks(request):
    all_tasks = Task.objects.all()
    json_response = serializers.serialize("json", all_tasks)
    return HttpResponse(json_response, content_type="application/json", status=status.HTTP_200_OK)

@api_view(['POST'])
def post_tasks(request):
    data = JSONParser().parse(request)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # json_response = serializers.serialize("json", serializer)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.delete()
    except Task.DoesNotExist:
        raise Http404("Task não existe")

    return HttpResponse("Task deletada com sucesso")
    

# @api_view(['POST', 'DELETE'])
# def task_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         task = Task.objects.get(pk=pk)
        
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(request.data,  content_type="application/json", status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         task.delete()
#         json_response = serializers.serialize("json", task)
#         return HttpResponse(json_response, content_type="application/json", status=status.HTTP_204_NO_CONTENT)