from django.shortcuts import render
from rest_framework.views import APIView

from Users.models import User


# Create your views here.
class UserViews(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        