from django.urls import path, include
from .views import home_screen, AllPasswords,Login,Signup

urlpatterns = [
    path('',home_screen),
    path('api/passwords/',AllPasswords.as_view()),
    path('login/',Login.as_view()),
    path('signup/',Signup.as_view())

]
