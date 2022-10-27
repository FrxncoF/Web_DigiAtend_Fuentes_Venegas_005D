from django.urls import path
from .views import *

urlpatterns = [
    path('',login),
    path('qrcode/',qrcode),
    path('register/',register)
]

