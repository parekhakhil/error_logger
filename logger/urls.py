from django.urls import path
from .views import ErrorView

urlpatterns = [
    path('get/',ErrorView.as_view(),name='get_error_list'),
    path('get/<int:pk>',ErrorView.as_view(),name='get_error'),
    path('create/',ErrorView.as_view(),name='create_error'),
    path('edit/<int:pk>',ErrorView.as_view(),name='update_error'),
    path('delete/<int:pk>',ErrorView.as_view(),name='delete_error')
]
