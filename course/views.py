# from django.db import models
# from django.db.models import fields
# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Course
from .serializers import GetAllCourseSerializers

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer

# Create your views here.



class GetAllCoursesApiView(APIView):
  def get(self, request):
    all = Course.objects.all()
    myData = GetAllCourseSerializers(all, many = True)
    return Response(status=status.HTTP_200_OK, data=myData.data)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]