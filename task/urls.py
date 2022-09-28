from django.urls import path
from .views import TaskView

urlpatterns = [
    path('get/',TaskView.as_view(),name='get_task_list'),
    path('get/<int:pk>',TaskView.as_view(),name='get_task'),
    path('create/',TaskView.as_view(),name='create_task'),
    path('edit/<int:pk>',TaskView.as_view(),name='edit_task'),
    path('delete/<int:pk>',TaskView.as_view(),name='delete_task')
]
