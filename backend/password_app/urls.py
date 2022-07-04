from django.urls import path, include
from .views import home_screen, AllPasswords

urlpatterns = [
    path('',home_screen),
    path('api/passwords/',AllPasswords.as_view())

]
