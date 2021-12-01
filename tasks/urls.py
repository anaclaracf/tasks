from django.urls import include, path
from rest_framework import routers
from . import views
# from views import TaskViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>', views.task_detail, name="task"),
    path('all_tasks/', views.get_all_tasks, name="all_task")
]