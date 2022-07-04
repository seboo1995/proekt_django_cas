from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Password(models.Model):
    username = models.CharField(max_length=100,null=False)
    pswd = models.CharField(max_length=100)
    url = models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(null=True)
    notes = models.TextField(null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')

    def __str__(self):
        return (f'{self.username} : {self.url}')

