from django.urls import include, path
from rest_framework import routers
from . import views
# from views import TaskViewSet

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/<int:pk>', views.delete_task, name="delte"),
    path('all_tasks/', views.get_all_tasks, name="all_task"),
    path('post/', views.post_tasks, name="post"),
    # path('post/', views.post_tasks, name="post_task"),
    # path('delete/', views.delete_task, name="delete_task"),
]