# This is a python file for url of Hive Music project

from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('join', index),
    path('create', index)
]

# End of project
