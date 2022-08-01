from django.http import HttpRequest, Http404
from django.urls import path

from case_study.crud import views


def index(request: HttpRequest):
    raise Http404()

urlpatterns = [
    path('user', views.user, name='role'),
]
