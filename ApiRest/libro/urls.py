from django.urls import path
from .views import *

urlpatterns = [
    path('list', LibroList.as_view()),
    path('create', LibroCreate.as_view()),
    path('update/<int:pk>', LibroUpdate.as_view()),
    path('delete/<int:pk>', LibroDelete.as_view()),
]
