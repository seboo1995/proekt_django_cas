import re
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .models import Password
from .serializers import PasswordSerializer
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
        password_to_delete = Password.objects.get(url = request.GET['url']).delete() 

