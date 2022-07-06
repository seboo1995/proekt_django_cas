import re
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .models import Password
from .serializers import PasswordSerializer,UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.



def home_screen(request):
    return HttpResponse('Welcome to Password Manager API')


class AllPasswords(APIView):
    
    def get(self,request):
        all_passwords_for_user = Password.objects.filter(user_id = request.GET['userId'])
        password_serializer = PasswordSerializer(all_passwords_for_user,many=True)
        try:
            return Response(password_serializer.data)
        except Exception as e:
            return Response({'info':f'{e}'})

    def post(self,request):
        new_password_serializer = PasswordSerializer(data=request.data)
        if new_password_serializer.is_valid():
            new_password_serializer.save()
            return Response(new_password_serializer.data)
        else:
            return Response(new_password_serializer.errors)

    def delete(self,request):
        ## todo: Delete password  
        password_to_delete = Password.objects.get(url = request.GET['url']).delete() 


class Login(APIView):
    def get(self,request):
        username=request.GET['username']
        password=request.GET['password']
        user=authenticate(username=username,password=password)
        if user:
            return Response({'info':'success','userId':user.id})
        else:
            print("ERRRRRROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOR")
            return Response({'info':'error'})

class Signup(APIView):
    def post(self,request):
        new_user_serializer = UserSerializer(data=request.data)
        if new_user_serializer.is_valid():
            new_user_serializer.save()
            return Response(new_user_serializer.data)
        else:
            return Response(new_user_serializer.errors)


