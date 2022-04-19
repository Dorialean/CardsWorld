from django.urls import path

import articles
from .views import *

urlpatterns =[
    path('', index),
    path('register/', register),
    path('profile/', profile),
]