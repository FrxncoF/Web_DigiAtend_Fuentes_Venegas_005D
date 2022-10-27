import imp
from django.urls import path
from .views import *

urlpatterns = [
    path('<clase>/', generar_codigo),
    
]