from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from case_study.crud.models import User


def user_crud(http: HttpRequest):
    user = User()
    user.username = "yanmastra"
    user.first_name = "Wayan"
    user.last_name = "Mastra"
    user = user.save()
    return user


