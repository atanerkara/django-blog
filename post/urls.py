from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('create/', post_create, name='create'),
    path('<slug:slug>/disable/', post_disable, name='disable'),
    path('<slug:slug>/update/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete, name='delete'),
    path('<slug:slug>', post_detail, name='detail'),
]