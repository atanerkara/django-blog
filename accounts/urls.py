from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='signin'),
    path('signup/', register_view, name='signup'),
    path('logout/', logout_view, name='signout'),
    path('profile/<str:username>', profile_view, name='profile'),
]
